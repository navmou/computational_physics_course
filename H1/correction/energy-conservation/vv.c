/* 
File containing the functions velocity_verlet, 
pair_distance calculator and write_to_file used in the main
*/

#include <stdio.h>
#include <stdlib.h>
#include "H1potential.h"
#include <math.h>


/* function responsible for equilibrating Temperature and Pressure*/
void equilibrate(double pos[][3] , double v[][3], double P_eq , double T_eq ,
		 double T ,double P,double tau , double dt , int n_particles, double *L)
{
  double alpha_T , alpha_P;
  /*scaling the velocity*/
  alpha_T = 1+(2.0*dt/tau)*((T_eq - T)/T);
  for (int i = 0 ; i < n_particles; ++i)
    {
      for (int j = 0; j<3; ++j)
	{
	  v[i][j] *= sqrt(alpha_T);
	}
    }
  /*scaling position*/
  alpha_P = 1-(0.01385*dt/tau*(P_eq - P));
  for (int i = 0 ; i < n_particles; ++i)
    {
      for (int j = 0; j < 3; ++j)
	{
	  pos[i][j] *= cbrt(alpha_P);
	}
    }
  /*scaling the lattice lenght*/
  *L *= cbrt(alpha_P);
 
}

/*velocity_verlet function to calculate the time evolution of the systme*/
void velocity_verlet(int n_timesteps, int n_particles, double v[][3], double pos[][3],
		     double dt, double m , double L , double *potE , double *kinE ,
		     double *totE , double *Pressure , double *Temperature , double k_b ,
		     double T_eq , double P_eq , double tau , double check_particles[][5] , double *L_list)
{

    
  printf("No problem\n");
  double s1 , s2 , r;
  /*array to store forces on each particle*/
  double (*forces)[3] = malloc(sizeof(double [n_particles][3]));
  /*calling potential function*/
  potE[0] = get_energy_AL(pos , L , n_particles);
  kinE[0] = 0.0;
  totE[0] = potE[0];
  L_list[0] = L;
  
  get_forces_AL(forces , pos , L , n_particles);
  /* Time step loop*/
  for (int t = 1; t < n_timesteps + 1; ++t)
    {
      /* v(t+dt/2) */
      for (int i = 0; i < n_particles; i++)
	{
	  for (int j = 0 ; j < 3; ++j) {
	    v[i][j] += dt * 0.5 * forces[i][j]/m;
	  }
	}
      /* q(t+dt) */
      for (int i = 0; i < n_particles ; ++i)
	{
	  for (int j = 0; j < 3; ++j) {
	    pos[i][j] += dt * v[i][j];
	  }
	}
      /* a(t+dt) */
      get_forces_AL(forces , pos , L , n_particles);
      
      /* v(t+dt) */
      for (int i = 0; i < n_particles ; ++i)
	{
	  for (int j = 0; j < 3; ++j) {
	    v[i][j] += dt * 0.5 * forces[i][j]/m;
	  }
	}
      /*new potential */
      potE[t] = get_energy_AL(pos , L , n_particles);

      /* sum(v^2) */
      s2 = 0.0;
      for (int i = 0; i < n_particles; ++i) {
	s1 = 0.0;
	for (int j = 0; j < 3; ++j) {
	  s1 += v[i][j]*v[i][j];
	}
	s2 += s1;
      }
      /*kinetic energy*/
      kinE[t] = 0.5*s2*m;
      totE[t] = potE[t] + kinE[t];
      
      /*calling virial to calculate Pressure*/
      double W = get_virial_AL(pos , L , n_particles);
      Pressure[t] = (1.0/(L*L*L))*(W+m*s2/3.0)*(160.2) /* in GPa units */;
      //printf("%f\n", L*L*L); /*printing volume*/
      /*instantaneous Temperature*/
      Temperature[t] = 2.0/(3*n_particles*k_b)*kinE[t];
      /*equilibrate if time step was less than 10tau*/
      //      if(t < 10000){
      //      equilibrate(pos , v , P_eq , T_eq ,Temperature[t] , Pressure[t] ,  tau , dt , n_particles, &L);

      /*Updating forces after position scaling*/
      // get_forces_AL(forces , pos , L , n_particles);
      //}
      L_list[t] = L;
      
    }
  free(forces); forces=NULL;
}



/*write_to_file function to print the energies and pressure and temperature */
void write_to_file(char *fname,  double *kinE , double *potE ,
		   double *totE , double *Pressure ,
		   double *Temperature , double *L_list , int n_timesteps)
{
  FILE *fp = fopen(fname, "w");
  for(int i = 0; i < n_timesteps; ++i){
    fprintf(fp, "%f\t%f\t%f\t%f\t%f\t%f\n", kinE[i] , potE[i] , totE[i], Pressure[i] , Temperature[i] , L_list[i]);
  }
  fclose(fp);
}

/* calculating the pair distance for all pairs of atoms and saving in distances*/
void pair_distance(double pos[][3], double *distances, int n_particles)
{
  double d;
  int ind = 0; //index to pair (N(N-1)/2 pairs)
  for (int i = 0 ; i < n_particles; ++i)
    {
      for (int j = i+1; j < n_particles; ++j)
	  {
	    d = 0.0;
	    for (int k = 0 ; k < 3; ++k)
	      {
		d += (pos[i][k]-pos[j][k])*(pos[i][k]-pos[j][k]);	  
	      }
	    distances[ind] = sqrt(d);
	    ind++;
	  }
      }
  }
