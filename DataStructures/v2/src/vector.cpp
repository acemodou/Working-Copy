#include <vector>
using namespace std;
#include <iostream>


int main()
{
    cout << "Vector from initializer list:\n";
    vector<int> vi1 {1,2,3,4,5,6,7,8,9,10};

    cout <<"Size is: " << vi1.size() <<endl;
    cout <<"front: " << vi1.front() <<endl;
    cout <<"back: " << vi1.back() <<endl;

    // iterator
    cout <<"\n";
    auto itbegin = vi1.begin();
    auto itend = vi1.end();
    for (auto it = itbegin; it < itend; ++it)
    {
        cout << *it <<" "; 
    }
    cout <<endl;

    cout <<"Element 6: " << vi1[5] <<endl;
     cout <<"Element 6: " << vi1.at(5) <<endl;

     cout << "range based for loop: \n";
     for (auto& i : vi1)
     {
        cout << i << " \n";
     }
     cout <<"Insert 42 at begining  + 5: \n";
     vi1.insert(vi1.begin() + 5, 42);
     cout <<"Element 5: " << vi1.at(5) <<endl;
     cout <<"Erase at begin + 5: \n";
     vi1.erase(vi1.begin() + 5);

     cout << "Push back 47: \n";
     vi1.push_back(47);
    
    // from C array
    const size_t size {10};
    int ia[size] {1,2,3,4,5,6,7,8,9,10};
    vector<int> vi2(ia, ia+size);
    for (const auto& i: vi2)
    {
        cout <<i << " ";
    }
    cout << "\n";
    return 0;
}