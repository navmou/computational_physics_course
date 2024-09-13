#include <stdio.h>
#include <math.h>

void increment(double *x , double val);
double f(double x , double y);
int main(){
  printf("f(1,1) = %f\n", f(1,1));
  printf("f(2,2.3) = %f\n", f(2,2.3));
  printf("f(1.5,2) = %f\n", f(1.5,2));
  printf("f(3.5,5.5) = %f\n", f(3.5,5.5));
  int a = 1;
  int b = 1;
  printf("f(a,b) = %f\n", f(a,b));
  double x = 2;
  increment(&x,2);
  printf("increment(2,2) = %f\n", x);
  return 0;
}

double f(double x , double y){
  return x*x*x + sqrt(y);
}

void increment(double *x , double val){
  *x = *x+val;
}
