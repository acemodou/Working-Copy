#include <iostream>
#include <fstream>

int main() {
    static int lineo {};
    static const char * filename {"C:/Personal/Working-Copy/DataStructures/v2/src/test.txt"};
    static const char * textstring {"This is the test file"};

    // write a file
    std::cout << "Write this file\n";
    std::ofstream ofile(filename);
    ofile << ++lineo << " " << textstring << "\n";
    ofile.close();
    
    // read a file 
    static char buf[128];
    std::cout << "Read the file: \n";
    std::ifstream infile(filename);
    while (infile.good())
    {
        infile.getline(buf, sizeof(buf));
        std::cout << buf << "\n";
    }
    infile.close();

    // delete file
    std::cout << "delete file: \n";
    remove(filename);
    return 0; // Added to indicate successful execution to the operating system.
}
