#include<stdio.h>
int main() {
int a[2000],s,i,j,t,l1,l2,c=0;
scanf("%d",&s);
scanf("%d",&t);
for(i=0;i<s;i++)
scanf("%d",&a[i]);
for(i=0;i<t;i++)
{
scanf("%d %d",&l1,&l2);
for(j=0;j<s;j++)
{
  if((a[j]>=l1)&&(a[j]<=l2))
  c++;
}
printf("%d ",c);
c=0;
}
return 0;
}