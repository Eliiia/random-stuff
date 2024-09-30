#include <stdio.h>

#define IN  1 /* inside a word!!! */
#define OUT 0 /* outside a word!!!!!! */

int main()
{
    int c, n1, nw, nc, state;

    state = OUT;
    n1 = nw = nc = 0;
    
    while ((c = getchar()) != EOF) {
        ++nc; /* character counter: shown at end */
        if (c == '\n') ++n1; /* line counter: shown at end */
        if (c == ' ' || c == '\n' || c == '\t') state = OUT; /* if the character is a gap, you've left a word */
        else if (state == OUT) { 
            /* if the character is not a gap and it's not in a word, entered a new word */
            state = IN;
            ++nw; /* count new word: shown at end */
        }
    }

    printf("%d %d %d\n", n1, nw, nc); /* lines, words, characters */

    return 0;
}