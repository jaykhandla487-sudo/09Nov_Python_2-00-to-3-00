#include <iostream>
using namespace std;

class Person {
public:
    string name;
};

class Student : public Person {
public:
    int roll;

    void display(){
        cout<<"Name: "<<name<<endl;
        cout<<"Roll: "<<roll;
    }
};

int main() {

    Student s;

    s.name = "Yash";
    s.roll = 101;

    s.display();

    return 0;
}