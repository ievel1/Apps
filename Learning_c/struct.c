#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student {
    char name[50];
    char major[50];
    int age;
    double gpa;
};

int main() {
    struct Student student1;
    student1.age = 25;
    student1.gpa = 10.8;
    strcpy(student1.name, "William");
    strcpy(student1.major, "IT-programmer");

    struct Student student2;
    student2.age = 23;
    student2.gpa = 11.00;
    strcpy(student2.name, "Tuie");
    strcpy(student2.major, "IT-programmer");


    printf("%f", student1.gpa);
    

    return 0;
}
