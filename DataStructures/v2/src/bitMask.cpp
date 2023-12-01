#include <stdio.h>



int main()
{
  const char c = 'A';
  int mask = 0b10000000;

  // for(int i = 0; i < 8; i++)
  // {
  //   printf("%c", c & mask ? '1' :'0');
  //   mask >>= 1;
  // }
  // printf("\nc'%c' is %d\n", c, c);

  for ( int mask = 0b10000000;  mask != 0; mask >>= 1)
  {
    printf("%c", (c & mask) ? '1' : '0');
  }
  printf("\n%c is %d\n", c, c);


}