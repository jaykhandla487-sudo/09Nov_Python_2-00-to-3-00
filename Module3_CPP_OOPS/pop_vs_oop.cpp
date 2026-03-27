#include <iostream>
using namespace std;

// POP style
int areaPOP(int l, int w) {
    return l * w;
}

// OOP style
class Rectangle {
public:
    int l, w;

    int area() {
        return l * w;
    }
};

int main() {
    cout << "POP Area: " << areaPOP(5,3) << endl;

    Rectangle r;
    r.l = 5;
    r.w = 3;

    cout << "OOP Area: " << r.area();

    return 0;
}