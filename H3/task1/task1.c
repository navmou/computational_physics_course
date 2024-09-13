#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>
#include <math.h>
#include <sys/time.h>

struct timeval tv;


int main ()
{
  gettimeofday(&tv, NULL);	
  // Initial values
  int N0 = 500 , N = N0 , new_N = N0;
  int iter = 50000;
  double E_T = 1.0 , alpha = 0.0005;
  double *walkers = malloc(sizeof(double) * N);
  double *weights = malloc(sizeof(double) * N);
  int *N_list = malloc(sizeof(int) * iter);
  double delta_t = 0.01 , sqrt_delta_t = sqrt(delta_t);
  int *what_to_do = malloc(sizeof(double) * N0);
  double *new_walkers = malloc(sizeof(double) * new_N);
  double *E_Ts = malloc(sizeof(double) * iter);
  int m , new_i;  
  const gsl_rng_type *T;
  gsl_rng *q;
  gsl_rng_env_setup();
  T = gsl_rng_default;
  q = gsl_rng_alloc(T);
  gsl_rng_set(q, 2);

  for (int i = 0 ; i < N; ++i) {
    walkers[i] = 0.0;
  }

  int lenght_counter = 0;
  N_list[0] = N0;
  E_Ts[0] = E_T;

  //time loop
  for (int t = 1; t < iter; ++t)
    {
      //displace and calculate the weight
      for (int i = 0 ; i < N; ++i) {
	walkers[i] += sqrt_delta_t * gsl_ran_gaussian(q,1);
	weights[i] = exp(-1.0*delta_t*(0.5*walkers[i]*walkers[i] - E_T));
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
      new_walkers = realloc(new_walkers , new_N * sizeof(double));
      new_i = 0;
      for (int i = 0; i < N; ++i) {
	for (int j = 0; j < what_to_do[i] ; ++j)
	  {
	    new_walkers[new_i] = walkers[i];
	    new_i++;
	  }    
      }


      //Updating values
      weights = realloc(weights , new_N*sizeof(double));
      what_to_do = realloc(what_to_do , new_N*sizeof(int));
      walkers = realloc(walkers , new_N * sizeof(double));
      for (int i = 0; i < new_N; ++i) {
	walkers[i] = new_walkers[i];
      }
      N = new_N;
     
      //updating E_T
      lenght_counter = 0;
      double E_T_avg = 0.0;
      for (int j = 0; j < t ; ++j) {
	E_T_avg += E_Ts[j];
	lenght_counter++;
      }
      E_T_avg = E_T_avg/ (double) t;
      E_T = E_T_avg - (alpha/delta_t)*log((double) N/ (double) N0);
      E_Ts[t] = E_T;
      N_list[t] = new_N;
      
      //printf("t = %d - E_T = %f - N = %d - new_N = %d - done!\n",t, E_T , N, new_N);
    }

  /*
    for (int i = 0 ; i < iter; ++i) {
    printf("%d\n",N_list[i] );
    }
  */

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
