#include <stdio.h>

#define LOWER 0
#define UPPER 300
#define STEP 20

int main()
{
    int fahr;

    printf("Celcius to Fahrenheit conversion table!");

    for (fahr = UPPER; fahr >= LOWER; fahr = fahr - STEP) 
        printf("%5dF\t%3.1fC\n", fahr, (5.0/9.0) * (fahr-32.0));

    return 0;
}