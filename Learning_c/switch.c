#include <stdio.h>
#include <stdlib.h>

int main() {

    char grade = 'F';

    switch(grade){
        case 'A' :
            printf("You did a great job! ");
            break;
        case 'B' :
            printf("You did allright ");
            break;
        case 'C' :
            printf("You did poorly ");
            break;
        case 'D' :
            printf("You did very bad ");
            break;
        case 'F' :
            printf("You Failed! ");
            break;
        default :
            printf("Invalid Grade");
    }

    return 0;
}