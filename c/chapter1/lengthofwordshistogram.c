#include <stdio.h>

/* not finiiisheeed */

#define IN 1
#define OUT 0

#define MAXWORDS 5

int main() 
{
    int state = OUT;
    int wi = 0; /* word index! which word it is. */
    int aword[MAXWORDS];

    int c, i, j;

    for (i = 0; i < MAXWORDS; i++) {
        aword[i] = 0;
    }

    while ((c = getchar()) != EOF && (wi < MAXWORDS))  
    /* get characters! limit to MAXWORDS words total */
    { 
        if (c == ' ' || c == '\n' || c == '\t') {
            state = OUT;
            wi++;
        }
        else {
            if (state == IN) {
                aword[wi]++;
            }
            if (state == OUT) {
                aword[wi]++;
                state = IN; 
            }
        }
    }

    printf("\n"); /* empty line for formatting's sake */

    for (i = 0; i < MAXWORDS; i++) { /* per word */
        printf("%d", aword[i]);
        for (j = 0; j < aword[i]; j++) { /* print number of chars */
            printf("█");
        }
        printf("\n");
    }

    return 0;
}