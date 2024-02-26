#include <stdio.h>
#include <stdlib.h>

int main() {

    int age = 30;
    int *pAge = &age;

    printf("age: %d\n", *pAge);
    printf("Memory address: %p\n", pAge);
    printf("dereferencing: %d\n", &*&*&*&*&*&age);


    return 0;
}