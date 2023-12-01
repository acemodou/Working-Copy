#include <string>
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
// cout <<"Hello \n";
// string instr {};
// cout << "prompt: ";
// cin >> instr; // one word at a time 
// cout <<" input: " << instr << "\n";


char buf[128] {};
cout << "prompt: ";
cin.getline(buf, sizeof(buf));// one word at a time 
cout <<" input: " << buf << "\n";

}