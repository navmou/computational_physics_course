#include <stdlib.h>
#include "func.h"

int main(){

  int size = 100000;
  double *x = malloc(sizeof(double) * size);
  gaussian_generator(size , x);
  char file_name[] = "random.txt";
  write_file(file_name , x , size);
  free(x) ; x = NULL;
  return 0;
}
