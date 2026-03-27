#include <iostream>
using namespace std;

class BankAccount {

private:
    float balance;

public:

    void deposit(float amount){
        balance += amount;
    }

    void withdraw(float amount){
        balance -= amount;
    }

    void show(){
        cout << "Balance = " << balance;
    }
};

int main() {

    BankAccount b;

    b.deposit(1000);
    b.withdraw(200);

    b.show();

    return 0;
}