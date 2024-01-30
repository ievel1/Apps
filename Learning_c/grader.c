#include <stdio.h>

#define LOWER 0 /*lower limit of table*/
#define UPPER 300 /*upper limit*/
#define STEP 20 /*step size*/

/*print Fahrenheit-Celcsius table
    For fahr = 0, 20, ..., 300 */

int main()
{
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;
    upper = 300;
    step = 20;

    fahr = lower;
    while (fahr <= upper) {
        celsius =  (5.0/9.0) * (fahr-32.0);
        printf("%3.0f %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
}