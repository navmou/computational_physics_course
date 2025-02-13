#include <stdlib.h>
#include "func.h"
#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>
#include <time.h>

void gaussian_generator(int size , double *arr){
  const gsl_rng_type *T;
  gsl_rng *q;
  gsl_rng_env_setup();
  T = gsl_rng_default;
  q = gsl_rng_alloc(T);
  gsl_rng_set(q, time(NULL));

  for (int i = 0 ; i < size; ++i) {
    arr[i] = gsl_ran_gaussian(q , 1);
  }
  
}


void write_file(char * file_name , double *arr , int len){
  FILE *outputfile;
  outputfile = fopen(file_name , "w");
  for(int i = 0 ; i <  len ; ++i){
    fprintf(outputfile, "%f\n", arr[i]);
  }
  fclose(outputfile);
}
