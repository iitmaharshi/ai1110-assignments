#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include"coeffs.h"

double mean_square(char *str)
{
int i=0,c;
FILE *fp;
double x, temp=0.0;

fp = fopen(str,"r");
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//Add all numbers in file
temp = temp+x*x;
}
fclose(fp);
temp = temp/(i-1);
return temp;

}

int main(void)
{
//generating random numbers between 0 and 1
gaussian("gau.dat", 1000000);

//finding mean of numbers
double mean_numbers = mean("gau.dat");

//finding mean of square of numbers
double mean_squares_numbers = mean_square("gau.dat");

double variance = mean_squares_numbers - mean_numbers*mean_numbers;
printf("mean: %lf", mean_numbers);
printf("variance: %lf", variance);
return 0;
}

