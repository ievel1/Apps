#include <stdio.h>

int main() {

    char c;
    int index = 0;
    char array[1000];

    while ((c = getchar()) != EOF && c != '\n') {
        array[index++] = c;
    }
    array[index] = '\0';

    printf("The copied text: %s\n", array);
}

