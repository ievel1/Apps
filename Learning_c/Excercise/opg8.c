#include <stdio.h>

int main() {
    int c, blanks, tabs, newlines;

    blanks = 0, tabs = 0, newlines = 0;
    printf("Enter some tekst (Ctrl + D to end onLinux, Ctrl + Z to end on windows):\n");
    while ((c = getchar()) != EOF) {
        if(c == ' ') {
            ++blanks;
        }else if (c == '\t') {
            ++tabs;
        } else if (c == '\n') {
            ++newlines;
        }
    }
    printf("Number of blanks: %d\n", blanks);
    printf("Number of tabs: %d\n", tabs);
    printf("Number of newlines: %d\n", newlines);
}