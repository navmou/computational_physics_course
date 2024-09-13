#include <math.h>
#include "func.h"


double scalar_prod(double *x, double *y , int size){
  double result = 0.;
  for(int i = 0 ; i < size ; ++i){
    result += x[i] * y[i];
  }
  return result;
}

double distance(double coordinates[][3] , int point1 , int point2){
  double dist;
  for(int i = 0 ; i < 3 ; ++i){
    dist += (coordinates[point1][i]-coordinates[point2][i])*(coordinates[point1][i]-coordinates[point2][i]);
  }
  dist = sqrt(dist);
  return dist;
}
