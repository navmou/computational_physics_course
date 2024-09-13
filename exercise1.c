#include <stdio.h>

int main () {
  int m = 2;
  int n = 5;
  double x = 5.6;
  printf("m/n = %d\n",m/n );
  printf("x/n = %d\n",m/n );
  double y = m;
  printf("double y = m --->  %f\n",y);
  int k = x;
  printf("int k = x ----> %d\n",k );
  k = x-n ;
  printf("k = x-n ----> = %d\n",k );
  return 0;
}
