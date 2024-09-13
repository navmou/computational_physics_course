#include <stdio.h>
#include <stdlib.h>
#include "func.h"

int main(){
  int size;
  printf("Please enter the size: \n" );
  scanf("%d" , &size);
  double *x = malloc(size * sizeof (double));
  double *y = malloc(size * sizeof (double));
  for(int i = 0 ; i < size ; ++i){
    x[i] = 1; y[i] = 2;
  }
  printf("The result is:  %f\n",scalar_prod(x , y , size));
  free(x); x = NULL;
  free(y); y = NULL;

  double (*points)[size] = malloc(sizeof (double[size][3]));
  for(int i = 0 ; i < size ; ++i){
    for(int j = 0 ; j < 3 ; ++j){
      points[i][j] = (double) rand() / (double) RAND_MAX;
    }
  }
  
  printf("%f\n",distance(points , 0 , 1));
  free(points); points = NULL;
  return 0;
}




