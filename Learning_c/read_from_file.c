#include <stdio.h>
#include <stdlib.h>

int main() {

    char line[255];
    FILE * fpointer = fopen("employess.txt", "r");

    fgets(line, 255, fpointer);
    fgets(line, 255, fpointer);
    fclose(fpointer);
    printf("%s", line);


    return 0;
}