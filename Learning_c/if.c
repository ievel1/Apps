#include <stdio.h>
#include <stdlib.h>

int max(int num1, int num2, int num3) {

    int result;

    if(num1>=num2 && num1>=num3){
        result = num1;
    }else if(num2>=num1 && num2>=num3){
        
        result = num2;
    } else {
        result = num3;
    }

}


int main() {

    printf("the biggest number is: %d\n", max(30, 10, 3));
    if (3<1 || 5 < 10) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    

    return 0;
} 