#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>


void read_data(char *fname, double *signal)
{
  FILE *fp = fopen(fname, "r");

  /* if file no found
   * error out and exit code 1
   */
  if(fp == NULL){
    perror("error: File not found!");
    exit(1);
  }

  /* skip header */
  //fseek(fp, strlen("time, signal\n"), SEEK_SET);
  char line[128] = {0};
  char *token;
  int i = 0;
  while(fgets(line, sizeof(line), fp) != NULL){
    token = strtok(line,"\n");
    signal[i] = strtod(token, NULL);
    i++;
    memset(line, 0, sizeof(line));
    token = NULL;
  }
  fclose(fp);
}


void correlation(int N , double *signal , double mean , double mean_sq, int Temp){
  char buffer[32]; // The filename buffer
  snprintf(buffer, sizeof(char) * 32, "corr_%d.txt", Temp);
  FILE *fp = fopen(buffer,"w");
  double corr_mean , phi;
  for (int i = 0; i < N; ++i) {
    signal[i] -= mean;
  }
  
  mean = 0.0 ;
  mean_sq = 0.0 ;
  for (int i =0 ; i < N; ++i) {
    mean += signal[i];
    mean_sq += signal[i]*signal[i];
  }
  mean = mean/N;
  mean_sq = mean_sq/(N);
  printf("new mean %f\t new var%f\n",mean , mean_sq-mean*mean);
  
  for (int k = 0; k < 700000 ; k+=100) {
    corr_mean = 0.0;
    phi = 0.0;
    for (int i = 0; i < N-k; ++i) {
      corr_mean += signal[i+k]*signal[i];
    }
    corr_mean = corr_mean/(N-k);
    phi = (corr_mean - mean*mean)/(mean_sq - mean*mean);
    fprintf(fp, "%d\t%f\n", k , phi);

    //printf("phi = %f\t corr_mean = %f\t mean_sq = %f\t mean = %f\n", phi, corr_mean , mean_sq , mean );
    if(phi <= 0.135){
      printf("s = %d\n", k);
      break;
    }
  }
  fclose(fp);
}


void block_avg(double mean_sq , double mean , int N , double *signal , int Temp){
  char buffer[32]; // The filename buffer
  snprintf(buffer, sizeof(char) * 32, "block_%d.txt", Temp);
  FILE *f = fopen(buffer,"w");
  double F_j , mean_F , mean_F_sq , var_F , var_f;
  var_f = mean_sq - mean*mean;
  for (int B = 10; B < 500000; B+=100) {
    double *F = malloc(sizeof(double) * N/B);
    for (int j = 0; j < N/B ; ++j) {
      F_j = 0.0;
      for (int i = 0; i < B; ++i) {
	F_j += signal[i+(j)*B];
      }
      F[j] = F_j/(double) B;
    }
    mean_F = 0.0;
    mean_F_sq = 0.0;
    for (int i = 0 ; i < N/B; ++i) {
      mean_F += F[i];
      mean_F_sq += F[i]*F[i];
    }
    mean_F = mean_F/(double) (N/B);
    mean_F_sq = mean_F_sq/(double) (N/B);
    var_F = mean_F_sq - mean_F*mean_F;
    fprintf(f, "%f\t%f\t%f\t%f\n", var_F , var_f , sqrt(B) , B*(var_F)/(var_f));
    //printf("block size %d is done!\n",B );
    free(F); F=NULL;
    
  }

  fclose(f);
}


int main()
{
  char buffer[32]; // The filename buffer
  int N = 1000000;
  double *signal = malloc(sizeof(double) * N);
  int Temp_list[30] = {0,100,200,300,400,450,500,550,600,650,700,710,720,730,740,
		       750,760,770,780,790,800,850,900,950,1000,1100,1200,1300,1400,1500};
  int Temp;
  for (int i = 0; i < 30; ++i)
    {
      Temp = Temp_list[i];
      /*reading the file*/
      snprintf(buffer, sizeof(char) * 32, "new_data/energy_%d.0.txt", Temp);
      read_data(buffer, signal);

      double mean = 0.0 ;
      double mean_sq = 0.0 ;
      for (int i =0 ; i < N; ++i) {
	mean += signal[i];
	mean_sq += signal[i]*signal[i];
      }
      mean = mean/N;
      mean_sq = mean_sq/(N);
      printf("mean %f\t var%f\n",mean , mean_sq-mean*mean);

      correlation(N , signal , mean , mean_sq , Temp);
      block_avg(mean_sq , mean , N , signal, Temp);

      /*Cleaning the signal array*/
      for (int i = 0; i < N ; ++i) {
	signal[i] = 0;
      }
      
    }
  free(signal); signal = NULL;
  return 0;
}
