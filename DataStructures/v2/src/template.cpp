#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

template <typename T>
T maxof(T a, T b)
{
    return a > b ? a : b;
}


int main()
{
    // int x {47};
    // int y {73};
    std::string x {"foo"};
    std::string y {"bar"};
    auto z = maxof(x, y);
    cout <<z;
    return 0;
}