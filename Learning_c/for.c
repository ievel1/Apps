#include <stdio.h>
#include <stdlib.h>

int main() {

    int luckyNumbers[] = {4, 8, 12, 18, 20, 27, 30, 33, 66};

    int i;

    for(i = 8; i >= 0; i--) {
        printf("%d\n", luckyNumbers[i]);
    }
    printf("\n\n");
    for(i = 0; i <= 8; i++) {
        printf("%d\n", luckyNumbers[i]);
    }


    return 0;
}