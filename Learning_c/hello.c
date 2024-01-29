#include <stdio.h>
#include "plus.h"


int main(int argc, char * argv[])
{
    printf("Hello, ");
    printf("world %s %d", argv[0], plus(2, 2));
    printf("you are: %s %d", argv[1], minus(4, 8));
    printf("\n");
    
    return 42;
}

