#include <iostream>

int main() {
    long long num;
    num = 1000;
    for (int i = 1; i <= num; i += 1) {
        std::cout << i << "  ";
    }
    std::cout << "Done";
}