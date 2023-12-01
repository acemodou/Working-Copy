#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
#include <stdio.h>

const size_t maxstring {1024};
const char * filename {"C:/Personal/Working-Copy/DataStructures/v2/src/items.txt"};
const char tab_char {'\t'};

class Item
{
    int _sku {};
    string _name {};
    string _desc {};
public:
 Item() {reset();}
 Item(int sku, string& name, string& desc): _sku(sku), _name(name), _desc(desc) {}
 Item(const Item& rhs);
 Item & operator = (const Item& rhs);
 ~Item() {reset();}
 void reset() {_sku = 0; _name=_desc = "unk";}
 void setSku(int sku){_sku = sku;}
 int getSku() const {return _sku;}
 void setName(const string& name){_name = name;}
 string getName() const {return _name;}
 void setDesc(const string desc){_desc = desc;}
 string getDesc() const {return _desc;}

};
Item::Item(const Item& rhs)
{
    _sku = rhs._sku;
    _name = rhs._name;
    _desc = rhs._desc;
}

Item &Item::operator = (const Item& rhs)
{
    if(this != &rhs)
    {
        _sku = rhs._sku;
        _name = rhs._name;
        _desc = rhs._desc;
    }
    return *this; 
}

// split a string 
vector<string> strsplit(const string& s){
    vector<string> strs_v;
    size_t start_loc {};
    size_t sep_loc {};
    while (true)
    {
        sep_loc = s.find(tab_char, start_loc);
        strs_v.push_back(s.substr(start_loc, sep_loc - start_loc));
        if (sep_loc == string::npos) break;
        start_loc = sep_loc + 1;
    }
    return strs_v;
}


int main()
{
    char buf[maxstring];

    // open the file string 
    std::ifstream infile(filename);

    // read the file 
    while (infile.good())
    {
        // get the line 
        infile.getline(buf, sizeof(buf));
        if(!*buf) break;

        // split the string 
        vector<string> split_v {strsplit(buf)};
        if (split_v.size() < 3) continue;

        // consturct the object 
        Item current_item {std::stoi(split_v[0]), split_v[1], split_v[2]};
        cout << "SKU: " << current_item.getSku() << ", Name: " << current_item.getName() << ", Desc: " << current_item.getDesc() << endl;
    }
    infile.close();
}
