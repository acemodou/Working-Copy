#include <iostream>
#include <string>
using namespace std;


int main()
{
    string s1 {"This is a string"};

    // size & length 
    cout << "Length is same as size in C++: " <<s1.length() <<endl;
    cout << "Length is same as size in C++ :" <<s1.size() <<endl;

    // + for concatenation 
    cout <<"Concatenated strings: ";
    string s2 = s1 + ":" + "This is also a string";
    cout <<s2 << endl;

    s1.insert(s1.begin() + 5, 'X');
    cout <<s1 << endl;

    // replace 
    s1.replace(5, 2, "ain't");
    cout <<"s1 after replace: " <<s1;




}