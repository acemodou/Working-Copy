#include <iostream>
#include <format>
#include <cstdint>
#include <stdio.h>
using namespace std;

using int_type = uint16_t;

void printp(const int_type* p)
{
    printf("Pointer is %d, value is %d ", p, *p);
}

int main()
{
    int_type arr[] = {1, 2, 3, 4, 5};
    int_type *p = arr;
    printp(p++);
    printp(p++); 
    printp(p++); 
}