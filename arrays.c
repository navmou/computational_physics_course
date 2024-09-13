#include <stdio.h>
#include <stdlib.h>

void print_array(double arr[] , int len);
void write_array(char *file_name , double arr[] , int len);
void matrix_multiply(double A[3][3] , double B[3][3] , double C[3][3]);
int main(){

  srand(20);
  int size = 10;
  double test[size];

  for(int i = 0 ; i < size ; ++i){
    test[i] = (double)rand()/(double)RAND_MAX;
  }
  
  print_array(test , size);
  char file_name[] = "array.txt";
  write_array(file_name , test , size);


  double A[3][3] = {{1.,1.,1.},{1.,1.,1.},{1.,1.,1.}};
  double B[3][3] = {{2.,2.,2.},{2.,2.,2.},{2.,2.,2.}};
  double C[3][3];
  matrix_multiply(A,B,C);
  for(int i = 0 ; i < 3 ; ++i){
    for(int j = 0 ; j < 3 ; ++j){
      printf("%f\t",C[i][j] );
    }
    printf("\n");
  }


  
  return 0;
}

void print_array(double arr[] , int len){
  for(int i = 0 ; i < len ; ++i){
    printf("%f\n",arr[i] );
  }
}

void write_array(char *file_name , double arr[] , int len){
  FILE *outputfile;
  outputfile = fopen(file_name , "w");
  for(int i = 0 ; i < len ; ++i){
    fprintf(outputfile, "%f\n", arr[i]);
  }
  fclose(outputfile);
}

void matrix_multiply(double A[3][3] , double B[3][3] , double C[3][3]){
  for(int i = 0 ; i < 3 ; ++i){
    for(int j = 0 ; j < 3 ; ++j){
      C[i][j] = 0.;
	for(int k = 0 ; k < 3 ; ++k){
	  C[i][j] += A[i][k]*B[k][j];
	}
      }
    }
  }

