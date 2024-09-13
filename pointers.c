#include <stdio.h>

int main(){
  int m = 2;
  int *pm = &m;
  printf("m+1 = %d\n",m+1 );
  printf("*pm +1 = %d\n",*pm+1 );
  printf("pm = %d\n",pm );
  printf("&m = %d\n",&m );
  printf("*(&m)+1 = %d\n",*(&m)+1 );
  int n = pm;
  printf("int n = pm ---> %d\n",n );

  

  return 0;
}
