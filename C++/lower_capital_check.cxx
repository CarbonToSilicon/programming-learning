#include <iostream>
using namespace std;

int main() {
    char c;
    cout << "Type a character: ";
    cin >> c;
    if (c >= 'a' && c <= 'z') {
        cout << "     " << c << ": is lower case.";
    } else if (c >= 'A' && c <= 90) {
        cout << "     " << c << ": is capital case";
    } else {
        cout << "Is invalid input!\n";
    }
    return 0;
}

        