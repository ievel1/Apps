#include <stdio.h>
#include <stdlib.h>

int main() {

    int secretNumber = 5;
    int guess;
    int guessCount = 0;
    int guessLimit = 3;
    int outofGuesses = 0;

    while(guess != secretNumber && outofGuesses == 0) {
        if(guessCount < guessLimit){
            printf("Guess the number: ");
            scanf("%d", &guess);
            printf("Wrong number\n");
            guessCount++;
        } else {
            outofGuesses = 1;
        }
    }
    if(outofGuesses == 1){
        printf("Out of guesses\n");
    } else {
        printf("You Win!\nThe number was 5!\n");
    }
    return 0;
}