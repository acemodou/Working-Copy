#include <iostream>
#include <stack>
#include <tuple>
#include <type_traits>

std::stack<uint16_t> data;

template <typename T>
constexpr uint64_t zero_pad(T value, int bits) {
    return (bits == 64) ? static_cast<uint64_t>(value) : (static_cast<uint64_t>(value) << (64 - bits));
}

// Helper function for creating a tuple from variadic arguments
//Call std make_tuple
// pack expansions
template <typename... Args>
auto make_tuple_helper(Args... args) {
    return std::tuple<Args...>(args...);
}

// if constexpr to check the size and shift mask the values 

// Helper function for parameter pack expansion
template <size_t N, typename... Args>
void write_helper(const std::tuple<Args...>& argsTuple) {
    if constexpr (N < sizeof...(Args)) {
        uint64_t value = static_cast<uint64_t>(std::get<N>(argsTuple));

        // Split the value into 16-bit chunks and push them into the stack
        //
        while (value > 0) {
            uint16_t chunk = static_cast<uint16_t>(value & 0xFFFF); // Extract the lowest 16 bits
            data.push(chunk);

            // Right shift the value to get the next 16 bits
            value >>= 16;
        }

        // Recursively call write_helper for the remaining arguments
        write_helper<N + 1>(argsTuple);
    }
}
//todo: I need a function is called write_hw and it takes a template parameter which is integer 0 until 3
template <typename... Args>
void write(Args... args) {
    // Ensure that T is an integral type
    static_assert((std::is_integral_v<Args> && ...), "All arguments must be integral types");

    // Check if the size of arguments exceeds 64 bits
    //TODO: 8 bit should be change to 16 bits 
    static_assert((sizeof(Args) + ...) <= 8, "Total size of arguments can't be greater than 64 bits!!!");

    // Create a tuple from the arguments
    const auto argsTuple = make_tuple_helper(args...);

    // Start recursion with the arguments tuple
    write_helper<0>(argsTuple);
}

void print_and_pop() {
    while (!data.empty()) {
        uint16_t value = data.top();
        data.pop();

        // Print the 16-bit value in hexadecimal format
        std::cout << "write HW: 0x" << std::hex << static_cast<int>(value) << std::endl;
       
    }
}

int main() {
    // Test the write function with example values
    write(static_cast<uint8_t>(0x12), static_cast<uint32_t>(0x34567890), static_cast<uint16_t>(0xdead));

    // Print values stored in the stack
    print_and_pop();

    return 0;
}
