#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>
#include <math.h>
#include <sys/time.h>

struct timeval tv;

//Potential calculation 
double get_potentail(double walkers[][6] , int index)
{
  double potential = 0.0;
  double r1 = 0.0 , r2 = 0.0 , r12 = 0.0;

  //Calculation of the distances r1 , r2 , r12
  for (int i = 0; i < 3; ++i) {
    r1 += walkers[index][i]*walkers[index][i];
  }
  r1 = sqrt(r1);
  for (int i = 3; i < 6; ++i) {
    r2 += walkers[index][i]*walkers[index][i];
  }
  r2 = sqrt(r2);
  for (int i = 0; i < 3; ++i) {
    r12 += (walkers[index][i]-walkers[index][i+3])*(walkers[index][i]-walkers[index][i+3]);
  }
  r12 = sqrt(r12);
  
  potential = (-2.0/r1) + (-2.0/r2) + 1.0/r12 ;
  return potential;
}

int main ()
{
  gettimeofday(&tv, NULL);	
  // Initial values
  int N0 = 500 , N = N0 , new_N = N0;
  int iter = 50000;
  double E_T = 0.0 , alpha = 0.001 , potential;
  double (*walkers)[6] = malloc(sizeof (double[N][6]));
  double *weights = malloc(sizeof(double) * N);
  int *N_list = malloc(sizeof(int) * iter);
  double delta_t = 0.001 , sqrt_delta_t = sqrt(delta_t);
  int *what_to_do = malloc(sizeof(double) * N0);
  double (*new_walkers)[6] = malloc(sizeof (double[new_N][6]));
  double *E_Ts = malloc(sizeof(double) * iter);
  int m , new_i;  
  const gsl_rng_type *T;
  gsl_rng *q;
  gsl_rng_env_setup();
  T = gsl_rng_default;
  q = gsl_rng_alloc(T);
  gsl_rng_set(q, 2);

  //initialization of walkers
  for (int i = 0 ; i < N; ++i)
    {
      for (int j = 0; j < 6; ++j)
	{
	  walkers[i][j] = 0.0; 
	}
    }
  
  N_list[0] = N0;
  E_Ts[0] = E_T;

  //time loop
  for (int t = 1; t < iter; ++t)
    {
      
      //displace
      for (int i = 0 ; i < N; ++i)
	{
	  for (int j = 0; j < 6; ++j)
	    {
	      walkers[i][j] +=  sqrt_delta_t * gsl_ran_gaussian(q,1); 
	    }
	}
      
      //calculate the weight
      for (int i = 0; i < N; ++i)
	{
	  potential = get_potentail(walkers , i );
	  weights[i] = exp(-1.0*delta_t*(potential - E_T));	
	}
      

      //check what should be done with each walker based on the weight function
      for (int i = 0 ; i < N; ++i) {
	m = (int) (weights[i]+gsl_rng_uniform(q));
	what_to_do[i] = m;
      }
      

      //check the number of new walkers
      new_N = 0;
      for (int i = 0; i < N; ++i) {
	new_N += what_to_do[i];
      }
      
      //reallocation of the new walkers array.
      new_walkers = realloc(new_walkers , sizeof (double[new_N][6]));
      new_i = 0;
      for (int i = 0; i < N; ++i) {
	for (int j = 0; j < what_to_do[i] ; ++j)
	  {
	    for (int k = 0; k < 6; ++k)
	      {
		new_walkers[new_i][k] = walkers[i][k];
	      }
	    new_i++;
	  }    
      }


      //Updating values
      weights = realloc(weights , new_N*sizeof(double));
      what_to_do = realloc(what_to_do , new_N*sizeof(int));
      walkers = realloc(walkers , sizeof (double[new_N][6]));
      for (int i = 0; i < new_N; ++i)
	{
	  for (int j = 0; j < 6; ++j)
	    {
	      walkers[i][j] = new_walkers[i][j];	      
	    }
	}
      N = new_N;
     
      //updating E_T
      double E_T_avg = 0.0;
      for (int j = 0; j < t ; ++j) {
	E_T_avg += E_Ts[j];
      }
      E_T_avg = E_T_avg/ (double) t;
      E_T = E_T_avg - (alpha/delta_t)*log((double) N/ (double) N0);
      E_Ts[t] = E_T;
      N_list[t] = new_N;
      
      //printf("t = %d - E_T = %f - N = %d - new_N = %d - done!\n",t, E_T , N, new_N);
    }

  //writing into file
  FILE *f = fopen("E.txt","w");
  FILE *p = fopen("N.txt","w");
  for (int i = 0; i < iter; ++i) {
    fprintf(f, "%f\n", E_Ts[i]);
    fprintf(p, "%d\n", N_list[i]);
  }
  fclose(f);
  fclose(p);
  
  free(walkers)	; walkers = NULL;
  free(new_walkers); new_walkers = NULL;
  free(what_to_do); what_to_do = NULL;
  free(weights); weights = NULL;
  free(N_list); N_list = NULL;
  free(E_Ts); E_Ts = NULL;
  gsl_rng_free(q);
	
  return 0;
}
