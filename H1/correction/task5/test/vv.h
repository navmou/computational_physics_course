/*

  Created by Navid

*/

extern void write_to_file(char *fname,  double *kinE , double *potE , double *totE , double *Pressure , double *Temperature, double *L_list , int n_timesteps);

extern void velocity_verlet(int n_timesteps, int n_particles, double v[][3], double pos[][3],double dt, double m , double L , double *potE , double *kinE , double *totE , double *Pressure, double *Temperature, double k_b, double T_eq , double P_eq , double tau ,double check_particles[][5] , double *L_list);

extern void pair_distance(double pos[][3], double *distances, int n_particles);
