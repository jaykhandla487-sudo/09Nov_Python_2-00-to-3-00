#include <iostream>
using namespace std;

int globalVar = 10;

void show() {
    int localVar = 5;
    cout << "Local Variable = " << localVar << endl;
}

int main() {

    cout << "Global Variable = " << globalVar << endl;

    show();

    return 0;
}