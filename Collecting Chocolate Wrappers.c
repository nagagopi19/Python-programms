#include <stdio.h>
int main() {
int n,i,k=0,sum=0,s1=0,t,temp=0,j;
long c[200007],s[200007];
scanf("%d",&t);
for(int l=0;l<t;l++)
{
scanf("%d",&n);
for(i=0;i<n;i++)
scanf("%ld",&c[i]);
for(i=0;i<n;i++)
{
for(j=i+1;j<n;j++)
{
if(c[i]>c[j])
{
temp=c[i];
c[i]=c[j];
c[j]=temp;
}
}
}
sum=0;
k=0;
for(i=0;i<n;i++)
{
sum=sum+c[i];
s[k]=sum;
k++;
}
s1=0;
for(i=1;i<k;i++)
s1=s1+s[i];
printf("%d",s1);
}
return 0;
}