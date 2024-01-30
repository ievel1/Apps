#include <stdio.h>

int main() {
    
    int cc, pc;
    while ((cc = getchar()) != EOF) {
        if (!(pc == ' ' && cc == ' ')) {
            putchar(cc);
        }
        pc = cc;
    }
}