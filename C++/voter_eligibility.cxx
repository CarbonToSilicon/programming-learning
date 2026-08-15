#include <iostream>
using namespace std;

int main() {
	int h;
	cout << "Type a number: ";
	cin >> h;
	if (h >= 18 && h < 120) {
	    cout << "You can vote!\n";
	} else if (h < 18 && h >= 0) {
	    cout << "You cannot vote.\n";
	} else {
	    cout << "Invalid number!";
	}
	return 0;
}