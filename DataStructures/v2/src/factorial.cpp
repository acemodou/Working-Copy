#include <iostream>
using namespace std;

template<typename T>
T factorial(T n)
{
   T result = n;
   while (n > 1)
   {
    result *= --n;
   }
   return result;
}

int main()
{
    cout <<factorial(5.0);
}