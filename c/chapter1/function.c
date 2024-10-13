#include <stdio.h>

#define LOWER 0
#define UPPER 300
#define STEP 20

float convert(int f) {
    return (5.0/9.0) * (f-32.0);
}

int main()
{
    int fahr;

    printf("Celcius to Fahrenheit conversion table!");

    for (fahr = UPPER; fahr >= LOWER; fahr = fahr - STEP) 
        printf("%5dF\t%3.1fC\n", fahr, convert(fahr));

    return 0;
}