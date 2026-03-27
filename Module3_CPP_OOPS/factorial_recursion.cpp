#include <iostream>
using namespace std;

int add(int a,int b){ return a+b; }
int sub(int a,int b){ return a-b; }
int mul(int a,int b){ return a*b; }

int main() {

    int a,b;

    cout<<"Enter two numbers: ";
    cin>>a>>b;

    cout<<"Addition: "<<add(a,b)<<endl;
    cout<<"Subtraction: "<<sub(a,b)<<endl;
    cout<<"Multiplication: "<<mul(a,b)<<endl;

    return 0;
}