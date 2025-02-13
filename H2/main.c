#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <gsl/gsl_rng.h>
#include <math.h>

/*
  void nn(int n_neighbours ,int n_atoms,  double nn[n_atoms][n_neighbours])
  {




  }
*/

void initialize(int n_cells , int states[2*n_cells][2*n_cells][2*n_cells] , gsl_rng *q){
  int counter = 0;
  /*initialization of spins randomly*/
  for(int i = 0 ; i < 2*n_cells ; ++i){
    if(i%2 == 0){
      for (int j = 0; j < 2*n_cells ; ++j){
	if(j%2 == 0){
	  for (int k = 0; k < 2*n_cells; ++k) {
	    if(k%2 == 0){
	      states[i][j][k] = 1;
	    }else {
	      states[i][j][k] = 0;
	    }
	  }
	}else{
	  for (int k = 0; k < 2*n_cells; ++k) {
	    states[i][j][k] = 0;
	  }
	}
      }
    }else{
      for (int j = 0; j < 2*n_cells ; ++j){
	if(j%2 != 0){
	  for (int k = 0; k < 2*n_cells; ++k) {
	    if(k%2 != 0){
	      states[i][j][k] = -1;
	    }else {
	      states[i][j][k] = 0;
	    }
	  }
	}else{
	  for (int k = 0; k < 2*n_cells; ++k) {
	    states[i][j][k] = 0;
	  }
	}
      }
    }
  }
}



void rand_initialize(int n_cells , int states[2*n_cells][2*n_cells][2*n_cells] , gsl_rng *q){
  int counter = 0;
  /*initialization of spins randomly*/
  for(int i = 0 ; i < 2*n_cells ; ++i){
    if(i%2 == 0){
      for (int j = 0; j < 2*n_cells ; ++j){
	if(j%2 == 0){
	  for (int k = 0; k < 2*n_cells; ++k) {
	    if(k%2 == 0){
	      if(gsl_rng_uniform(q) < 0.5){
		states[i][j][k] = 1;
	      }
	      else {
		states[i][j][k] = -1;
	      }
	    }else {
	      states[i][j][k] = 0;
	    }
	  }
	}else{
	  for (int k = 0; k < 2*n_cells; ++k) {
	    states[i][j][k] = 0;
	  }
	}
      }
    }else{
      for (int j = 0; j < 2*n_cells ; ++j){
	if(j%2 != 0){
	  for (int k = 0; k < 2*n_cells; ++k) {
	    if(k%2 != 0){
	      if(gsl_rng_uniform(q) < 0.5){
		states[i][j][k] = 1;
	      }
	      else {
		states[i][j][k] = -1;
	      }
	    }else {
	      states[i][j][k] = 0;
	    }
	  }
	}else{
	  for (int k = 0; k < 2*n_cells; ++k) {
	    states[i][j][k] = 0;
	  }
	}
      }
    }
  }
}

/*






  for (int k = 0 ; k < 2*n_cells ; k+=2) {
  
  }
  }
  for (int j = 1; j < 2*n_cells ; j+=2) {
  for (int k = 1 ; k < 2*n_cells ; k+=2){
  states[i][j][k] = 0;
  }
  }
  }

  else{
  for (int j = 1; j < 2*n_cells ; j+=2) {
  for (int k = 1 ; k < 2*n_cells ; k+=2) {
  if(gsl_rng_uniform(q) < 0.5){
  states[i][j][k] = -1;
  }
  else {
  states[i][j][k] = -1;
  }
  }
  }
  for (int j = 0; j < 2*n_cells ; j+=2) {
  for (int k = 0 ; k < 2*n_cells ; k+=2){
  states[i][j][k] = 0;
  }
  }
  }
  //
  }
*/





void get_N_ij(int states[20][20][20] , int n_cells , int *N_aa , int *N_bb , int *N_ab)
{
  
  for (int i = 0; i < 2*n_cells; ++i) {
    for (int j = 0 ; j < 2*n_cells; ++j) {
      for (int k = 0 ; k < 2*n_cells; ++k) {
	if(states[i][j][k] != 0)
	  {
	    int x , y , z;
	    if(states[i][j][k] == 1)
	      {
		x=i+1; y=j+1; z=k-1;
		if(x == 20){ x = 0; }
		if(y == 20){ y = 0; }
		if(z == -1){ z = 19; }
		if(states[x][y][z] == 1) {
		  *N_aa += 1;
		}
		else{
		  *N_ab +=1;
		}
		x=i+1; y=j+1; z=k+1;
		if(x == 20){ x = 0; }
		if(y == 20){ y = 0; }
		if(z == 20){ z = 0; }
		if(states[x][y][z] == 1){
		  *N_aa += 1;
		}else{
		  *N_ab +=1;
		}
		x=i+1; y=j-1; z=k-1;
		if(x == 20){ x = 0; }
		if(y == -1){ y = 19; }
		if(z == -1){ z = 19; }
		if(states[x][y][z] == 1){
		  *N_aa+=1;
		}else{
		  *N_ab+=1;
		}
		x=i+1; y=j-1; z=k+1;
		if(x == 20){ x = 0; }
		if(y == -1){ y = 19; }
		if(z == 20){ z = 0; }
		if(states[x][y][z] == 1){
		  *N_aa+=1;
		}else{
		  *N_ab+=1;
		}
		x=i-1; y=j+1; z=k-1;
		if(x == -1){ x = 19; }
		if(y == 20){ y = 0; }
		if(z == -1){ z = 19; }
		if(states[x][y][z] == 1){
		  *N_aa+=1;
		}else{
		  *N_ab+=1;
		}
		x=i-1; y=j+1; z=k+1;
		if(x == -1){ x = 19; }
		if(y == 20){ y = 0; }
		if(z == 20){ z = 0; }
		if(states[x][y][z] == 1){
		  *N_aa+=1;
		}else{
		  *N_ab+=1;
		}
		x=i-1; y=j-1; z=k-1;
		if(x == -1){ x = 19; }
		if(y == -1){ y = 19; }
		if(z == -1){ z = 19; }
		if(states[x][y][z] == 1){
		  *N_aa+=1;
		}else{
		  *N_ab+=1;
		}
		x=i-1; y=j-1; z=k+1;
		if(x == -1){ x = 19; }
		if(y == -1){ y = 19; }
		if(z == 20){ z = 0; }
		if(states[x][y][z] == 1){
		  *N_aa+=1;
		}else{
		  *N_ab+=1;
		}
	      }
	    else
	      {
		x=i+1; y=j+1; z=k-1;
		if(x == 20){ x = 0; }
		if(y == 20){ y = 0; }
		if(z == -1){ z = 19; }
		if(states[x][y][z] == 1) {
		  *N_ab+=1;
		}
		else{
		  *N_bb+=1;
		}
		x=i+1; y=j+1; z=k+1;
		if(x == 20){ x = 0; }
		if(y == 20){ y = 0; }
		if(z == 20){ z = 0; }
		if(states[x][y][z] == 1){
		  *N_ab+=1;
		}else{
		  *N_bb+=1;
		}
		x=i+1; y=j-1; z=k-1;
		if(x == 20){ x = 0; }
		if(y == -1){ y = 19; }
		if(z == -1){ z = 19; }
		if(states[x][y][z] == 1){
		  *N_ab+=1;
		}else{
		  *N_bb+=1;
		}
		x=i+1; y=j-1; z=k+1;
		if(x == 20){ x = 0; }
		if(y == -1){ y = 19; }
		if(z == 20){ z = 0; }
		if(states[x][y][z] == 1){
		  *N_ab+=1;
		}else{
		  *N_bb+=1;
		}
		x=i-1; y=j+1; z=k-1;
		if(x == -1){ x = 19; }
		if(y == 20){ y = 0; }
		if(z == -1){ z = 19; }
		if(states[x][y][z] == 1){
		  *N_ab+=1;
		}else{
		  *N_bb+=1;
		}
		x=i-1; y=j+1; z=k+1;
		if(x == -1){ x = 19; }
		if(y == 20){ y = 0; }
		if(z == 20){ z = 0; }
		if(states[x][y][z] == 1){
		  *N_ab+=1;
		}else{
		  *N_bb+=1;
		}
		x=i-1; y=j-1; z=k-1;
		if(x == -1){ x = 19; }
		if(y == -1){ y = 19; }
		if(z == -1){ z = 19; }
		if(states[x][y][z] == 1){
		  *N_ab+=1;
		}else{
		  *N_bb+=1;
		}
		x=i-1; y=j-1; z=k+1;
		if(x == -1){ x = 19; }
		if(y == -1){ y = 19; }
		if(z == 20){ z = 0; }
		if(states[x][y][z] == 1){
		  *N_ab+=1;
		}else{
		  *N_bb+=1;
		}
	      }
	    /////////
	  }
      }
    }
  }

  *N_aa /= 2; *N_bb /= 2; *N_ab /= 2; 
}


/*function to randomly choose an atom*/
void choose_atom(int *x , int *y, int *z , gsl_rng *q){
  if(gsl_rng_uniform(q) >= 0.5){
    *x = 2*floor(gsl_rng_uniform(q)*10);
    *y = 2*floor(gsl_rng_uniform(q)*10);
    *z = 2*floor(gsl_rng_uniform(q)*10);
  }else{
    *x = 2*floor(gsl_rng_uniform(q)*10)+1;
    *y = 2*floor(gsl_rng_uniform(q)*10)+1;
    *z = 2*floor(gsl_rng_uniform(q)*10)+1;
  }

}


/*Main function*/
int main()
{  
  int n_cells = 10 , n_trials = 1500000 , n_discard = 500000;
  int states[2*n_cells][2*n_cells][2*n_cells];
  double Temp = 0.0 , T_max = 1500.0 , E0 , E1 , delta_E , k_B = 0.0000861733034 /* eV/K*/;
  int N_aa = 0, N_bb = 0 , N_ab = 0;
  const double E_aa  = -0.433, E_bb = -0.113 , E_ab = -0.294; /*in meV units*/
  int x1 , y1 , z1 , x2 , y2 , z2 , x;
  int n_temp_steps = 30;
  char buffer[32]; // The filename buffer

  double *E = malloc(sizeof(double) * n_trials);
  int *N_aa_list = malloc(sizeof(int) * n_trials);
  int *N_ab_list = malloc(sizeof(int) * n_trials);
  int *N_bb_list = malloc(sizeof(int) * n_trials);
  int *n_list = malloc(sizeof(int) * n_trials);
  int *temp_list = malloc(sizeof(int) * n_temp_steps);

  double *E_T = malloc(sizeof(double) * n_temp_steps);
  double *E_sq_T = malloc(sizeof(double) * n_temp_steps);
  double *Naa_T = malloc(sizeof(double) * n_temp_steps);
  double *Nbb_T = malloc(sizeof(double) * n_temp_steps);
  double *Nab_T = malloc(sizeof(double) * n_temp_steps);
  double *Nab_sq_T = malloc(sizeof(double) * n_temp_steps);
  double *n_T = malloc(sizeof(double) * n_temp_steps);
  double *n_sq_T = malloc(sizeof(double) * n_temp_steps);

  
  /*initialization of random number generator*/
  const gsl_rng_type *T;
  gsl_rng *q;
  gsl_rng_env_setup();
  T = gsl_rng_default;
  q = gsl_rng_alloc(T);
  gsl_rng_set(q , time(NULL));

  int temp_counter = 0;
  while (Temp <= T_max)
    {
      temp_list[temp_counter] = (int) Temp;
      printf("Temperature: %f is running\n",Temp );

      for (int i = 0 ; i < n_trials ; ++i) {
	E[i] = 0; N_aa_list[i] = 0; N_bb_list[i] = 0; N_ab_list[i] = 0;
      }
      
      initialize(n_cells , states , q);      
      N_aa = 0; N_ab = 0 ; N_bb = 0;
      get_N_ij(states , n_cells , &N_aa , &N_bb , &N_ab);
      E0 = E_aa*N_aa + E_bb*N_bb + E_ab*N_ab;


      for (int trial = 0; trial < n_trials ; ++trial)
	{

	  choose_atom(&x1 , &y1, &z1 , q);
	  choose_atom(&x2 , &y2, &z2 , q);
	  while(states[x1][y1][z1] == states[x2][y2][z2]){
	    choose_atom(&x2 , &y2, &z2 , q);
	  }

    
	  x = states[x2][y2][z2];
	  states[x2][y2][z2] = states[x1][y1][z1];
	  states[x1][y1][z1] = x;
    
	  N_aa = 0; N_ab = 0 ; N_bb = 0;
	  get_N_ij(states , n_cells , &N_aa , &N_bb , &N_ab);
	  E1 = E_aa*N_aa + E_bb*N_bb + E_ab*N_ab;
	  delta_E = E1-E0;

	  if(delta_E < 0)
	    {
	      E0 = E1;
	    }
	  else
	    {
	      if(gsl_rng_uniform(q) <= exp(-delta_E/(k_B*Temp)))
		{
		  E0 = E1;
		}
	      else
		{
		  x = states[x2][y2][z2];
		  states[x2][y2][z2] = states[x1][y1][z1];
		  states[x1][y1][z1] = x;
		}
	    }

	  E[trial] = E0;
	  N_aa_list[trial] = N_aa; N_bb_list[trial] = N_bb; N_ab_list[trial] = N_ab;

	  int n = 0;
	  for (int i = 0; i < 2*n_cells; i+=2) {
	    for (int j = 0; j < 2*n_cells; j+=2) {
	      for (int k = 0; k < 2*n_cells; k+=2) {
		if(states[i][j][k] == 1)
		  {
		    n++;
		  }
	      }
	    }
	  }

	  n_list[trial] = n;
	  
	}
      
      /*writing equilibration phase data into file*/
      snprintf(buffer, sizeof(char) * 32, "Temp_%d.txt", (int) Temp);
      FILE *fp = fopen(buffer,"wb");
      for (int i = 0; i < n_discard; ++i) {
	fprintf(fp, "%d\t%d\t%d\t%f\t%d\n", N_aa_list[i] , N_bb_list[i] , N_ab_list[i] , E[i] , n_list[i]);  
      }
      fclose(fp);

      
      /*writing equilibration phase data into file*/
      snprintf(buffer, sizeof(char) * 32, "Temp_%d_EQ.txt", (int) Temp);
      FILE *f = fopen(buffer,"wb");
      for (int i = n_discard ; i < n_trials; ++i) {
	fprintf(f, "%d\t%d\t%d\t%f\t%d\n", N_aa_list[i] , N_bb_list[i] , N_ab_list[i] , E[i] , n_list[i]);  
      }
       
      /*saving average of energy, n , N_aa , N_bb , and N_ab,  after equilibration*/
      double summ1 = 0 , summ2 = 0 , summ3 = 0 , summ4 = 0 , summ5 = 0;
      double summ6 = 0 , summ7 = 0 , summ8 = 0 , summ9 = 0;
      for(int i = n_discard; i < n_trials ; ++i)
	{
	  summ1 += E[i]; summ2 += E[i]*E[i];
	  summ3 += N_aa_list[i];
	  summ4 += N_bb_list[i];
	  summ5 += N_ab_list[i]; summ6 += N_ab_list[i]*N_ab_list[i];
	  summ7 += n_list[i] ; summ8 += n_list[i]*n_list[i];
	  
	}
       
      E_T[temp_counter] = summ1/(n_trials-n_discard);
      E_sq_T[temp_counter] = summ2/(n_trials-n_discard);
      Naa_T[temp_counter] = summ3/(n_trials-n_discard);
      Nbb_T[temp_counter] = summ4/(n_trials-n_discard);
      Nab_T[temp_counter] = summ5/(n_trials-n_discard);
      Nab_sq_T[temp_counter] = summ6/(n_trials-n_discard);
      n_T[temp_counter] = summ7/(n_trials-n_discard);
      n_sq_T[temp_counter] = summ8/(n_trials-n_discard);

      fclose(f);
      if(Temp < 400){Temp += 100;}
      else if (Temp >= 400 && Temp < 700){Temp += 50;}
      else if (Temp >= 700 && Temp < 800) {Temp += 10;}
      else if (Temp >= 800 && Temp < 1000){Temp += 50;}
      else{Temp += 100;}
      temp_counter++;
      
    }

  FILE *nf = fopen("average_values.txt","w");
  for (int i = 0; i < n_temp_steps; ++i) {
    fprintf(nf, "%d\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n", temp_list[i] , E_T[i], E_sq_T[i] , n_T[i] , n_sq_T[i] , Naa_T[i] , Nbb_T[i] , Nab_T[i] , Nab_sq_T[i]);

  }
  
  // printf("Now printing to file!\n");
  
  free(E); free(N_aa_list); free(N_ab_list); free(N_bb_list);
  E = NULL; N_aa_list = NULL; N_bb_list = NULL; N_ab_list = NULL;

  gsl_rng_free(q);q = NULL;
  return 0;

}
