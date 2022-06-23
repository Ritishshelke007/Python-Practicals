#include <stdio.h>

//Compiler version gcc  6.3.0

int main()
{
  int h, m, s,i;
  
  printf("Enter the time in hours ,minutes and seconds\n");
  scanf("%d%d%d",&h,&m,&s);
  printf("Enter the incremented seconds\n");
  scanf("%d",&i);
  s = s + i;
  if(s>=60)
  {
  m=m+1;
  s = s-60;
  if (m>=60)
  {
      h = h+1;
      m = m-60;
  }

  
  
  }
  printf("New time in hours, minutes and seconds is: %d : %d : %d",h,m,s);
  return 0;
  }
