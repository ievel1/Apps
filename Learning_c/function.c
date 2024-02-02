#include <stdio.h>
#include <stdlib.h>

void sayHi();

int main() {

    char nameF[20];
    char nameM[20];
    char nameL[20];

    printf("Enter a name: ");
    scanf("%s%s%s", nameF,nameM, nameL);
    sayHi(nameF, nameM, nameL);
    return 0;

}


void sayHi(char nameF[],char nameM[], char nameL[]) {

    printf("Hello %s %s %s\n", nameF, nameM, nameL);
}