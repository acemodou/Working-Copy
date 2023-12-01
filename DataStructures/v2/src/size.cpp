#include <iostream>
#include <typeinfo>
using namespace std;

// a byte is 8 bits
const size_t byte_ {8};

int func()
{
    static int x {7};
    return x++;
}

int main()
{
    float f {};
    double df {};
    long double ldf {};

    cout << "size of float is " << sizeof(f) * byte_ << " bytes" << endl;
    cout << "size of double is " << sizeof(df) * byte_ << " bytes" << endl;
    cout << "size of long double is " << sizeof(ldf) * byte_ << " bytes" << endl;

    string s {"This is a string"};
    auto x = s;
    cout << "x is " << x << endl;
    cout << "type of x is " << typeid(x).name() << endl;

    cout << func() << endl;
    cout << func() << endl;
    cout << func() << endl;
    return 0;
}
