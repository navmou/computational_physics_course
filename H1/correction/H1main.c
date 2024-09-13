#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include "H1lattice.h"
#include "H1potential.h"
#include "vv.h"

/* Main program */
int main()
{
  /*setting the random seed to time*/
  srand(time(NULL));
  double random_value;
  double mag;
  
  /* defining the necessary variables */
  /* [L]:angstrom - [T]:ps - [M]:m_asu - [Pres.]:GPa - [Temp.]:K*/
  int Nc = 4, N = 256 , n_timesteps = 1000;
  double (*pos)[3] = malloc(sizeof(double [N][3]));
  double *potE = malloc(sizeof(double) * n_timesteps);
  double *kinE = malloc(sizeof(double) * n_timesteps);
  double *totE = malloc(sizeof(double) * n_timesteps);
  double *Pressure = malloc(sizeof(double) * n_timesteps);
  double *Temperature = malloc(sizeof(double) * n_timesteps);
  double (*check_particles)[5] = malloc(sizeof(double [n_timesteps][5]));
  double *distances = malloc(sizeof(double) * (N*(N-1)/2.0));
  double *L_list = malloc(sizeof(double) * n_timesteps);

  double (*v)[3] = malloc(sizeof(double [N][3]));
  double a0 = 4.04 , dt = 0.001 , tau = 300*dt , m = 0.002796;
  double L = Nc*a0 , T_eq = 500.0+273.15 , P_eq = 0.0001;
  /*L:lattice size , T_eq: [K],  P_e:[GPa] */
  double k_b = 0.0000861733; /*Boltzamnn constant [eV/K] */


  /* Initialize the positions*/
  init_fcc(pos, Nc, a0);

  /* adding noise to positions */
  for (int i = 0; i < N; ++i)
    {
      for (int j = 0; j < 3; ++j)
	{
	  mag = a0*0.065; /* setting the magnitude of the maximum noise to 6.5% of the position value */
	  random_value = ((double) rand() / (double) RAND_MAX)*(2.0*mag) - mag;
	  pos[i][j] += random_value;
	}
    }

  /* Initializing velocity*/
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < 3; ++j) {
      v[i][j] = 0.0;
    }
  }

  /* Calling velocity_verlet to calculate the time evolution of the system*/
  velocity_verlet(n_timesteps , N , v , pos , dt , m , L , potE , kinE , totE ,
		  Pressure , Temperature , k_b , T_eq , P_eq, tau , check_particles , L_list);

  /* writing to file the energies, pressure, temperature*/
  write_to_file("energies.txt", kinE , potE , totE , Pressure , Temperature ,  L_list , n_timesteps);

  /*wrting to file the positions to check the solid or liquid phase*/
  FILE *f = fopen("positions.txt", "w");
  for (int i = 0; i < n_timesteps ; ++i) {
    for (int j = 0 ; j < 5; ++j) {
      fprintf(f, "%f\t", check_particles[i][j]);      
    }
    fprintf(f, "\n");
  }
  fclose(f);

  /* calling the pair distance calculator and writing the result to file  */
  pair_distance(pos , distances , N);
  FILE *g = fopen("pair-dist.txt", "w");
  for (int i = 0; i < N*(N-1)/2 ; ++i) {
    fprintf(g, "%f\n", distances[i]);
  }
  fclose(g);

  printf("No problems!\n");
  /*releasing the memory*/
  free(pos); pos = NULL; free(potE) ; potE = NULL; free(kinE); kinE = NULL;
  free(totE); totE = NULL; free(v) ; v = NULL;
  free(check_particles); check_particles= NULL; free(Temperature); Temperature= NULL;
  free(Pressure); Pressure = NULL; free(distances); distances = NULL;
  free(L_list); L_list = NULL;
  
  return 0;  
}
