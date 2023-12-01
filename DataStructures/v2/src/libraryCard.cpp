#include <iostream>
using namespace std; 
struct LibraryCard
{
 const char* title {};
 const char* author {};
 const char* publisher {};
 const char* subject {};
 const char* ISBN {};
 const char* OCLC {};
 float deweyDecimal {};
 short int yearPublished {};
 short int yearAcquired {};
 short int stockQuanity {};

};

int main()
{
    LibraryCard Catalog = {"Stories", "Modou", "ISBN", "Philosophy", "tea123","ocl", 13.4, 2000, 2021, 40};
    cout << Catalog.title;
    Catalog.title = {"NO"};
    cout << Catalog.title;
}