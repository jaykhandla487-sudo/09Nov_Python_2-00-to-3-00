#include <stdio.h>

int main() {
    int num, rev = 0, rem, original;

    printf("Enter number: ");
    scanf("%d", &num);

    original = num;

    while(num != 0) {
        rem = num % 10;
        rev = rev * 10 + rem;
        num /= 10;
    }

    if(original == rev)
        printf("Palindrome Number");
    else
        printf("Not Palindrome");

    return 0;
}