#include <stdio.h>
#include <stdlib.h>

int main() {
    double num1;
    double num2;

    char op;

    printf("Enter operator: ");
    scanf(" %c", &op);

    printf("Enter first number: \n");
    scanf("%lf", &num1);

    printf("Enter second number: \n");
    scanf("%lf", &num2);


    if(op == '+') {
    printf("Answer: %f\n", num1 + num2);
    } else if(op == '-') {
        printf("Answer: %f\n", num1 - num2);
    }else if(op == '*') {
        printf("Answer: %f\n", num1 * num2);
    }else if(op == '/') {
        printf("Answer: %f\n", num1 / num2);
    } else {
        printf("Invalid operator\n");
    }
    return 0;
}