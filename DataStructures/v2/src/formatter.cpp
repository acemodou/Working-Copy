#include <iostream>
#include <format>
#include <string_view>
using namespace std;

// format specialization
template <typename... Args>
constexpr void print(const string_view str_fmt, Args&&... args) {
    fputs(format(str_fmt, std::forward<Args>(args)...).c_str(), stdout);
}

int main() {
    const int a{47};
    print("a is {}\n", a);
}

