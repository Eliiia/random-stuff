#include <stdio.h>

/* not finiiisheeed */

#define IN 1
#define OUT 0

#define MAXWORDS 5
#define MAXWORDLENGTH 10

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

    for (i = MAXWORDLENGTH; i >= 0; i--) {
        /* loop for y axis (potential characters) */

        /* loop for x axis (words) */
        for (j = 0; j < MAXWORDS; j++) {
            if (aword[j] > i) printf("██"); /* if has enough characters, print block */
            else printf("  "); /* if doesnt have enough, put a space */
        }

        printf("\n");
    }

    return 0;
}