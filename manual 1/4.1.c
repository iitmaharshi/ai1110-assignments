#include<stdio.h>
#include<stdlib.h>

void generate(char *str, int len)
{
int i,j;
double temp;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
temp = 0;
for (j = 0; j < 2; j++)
{
temp += (double) rand()/RAND_MAX;
}
fprintf(fp,"%lf\n",temp);
}
fclose(fp);

}
int main(){

generate("generate.dat",1000000);

return 0;
}
