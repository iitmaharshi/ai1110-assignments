#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void non_uniform(char *str, int len)
{
int i;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
double x = (double)rand()/RAND_MAX;
double temp = -2*log(1-x);
fprintf(fp,"%lf\n",temp);
}
fclose(fp);
}

int main(){

non_uniform("non_uniform.dat",1000000);

return 0;
}


