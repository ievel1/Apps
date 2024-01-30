#include <stdio.h>

int main() {

    int cc, pc = EOF;
    while ((cc = getchar()) != EOF) {
        if (cc == '\t') {
            putchar('\\');
            putchar('t');
        } else if (cc = '\b') {
            putchar('\\');
            putchar('b');
        } else if (cc = '\\') {
            putchar('\\');
            putchar('\\');            
        }
        pc = cc;
    }
}