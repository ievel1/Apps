#include <stdio.h>
#include <stdlib.h>

int main() {

    FILE * fpointer = fopen("employess.txt", "a");

    fprintf(fpointer, "\nWilliam, software engineer");

    fclose(fpointer);
    return 0;
}