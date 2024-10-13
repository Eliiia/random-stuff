#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) 
{
    int val;

    val = atoi(argv[1]);

    printf("The value %d is ", val);

    if (val % 2 == 0)
        printf("even.\n");
    else printf("odd.\n");

    return 0;
}