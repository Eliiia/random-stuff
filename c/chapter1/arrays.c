#include <stdio.h>

int main() {
    int c, i, nwhite, nother;
    int ndigit[10]; /* 10-long array of ints */

    nwhite = nother = 0; /* number of whitespace, number of other */
    for (i = 0; i < 10; ++i)
        ndigit[i] = 0; /* set all values in array to 0 */

    while ((c = getchar()) != EOF) {
        if (c >= '0' && c <= '9') /*  */
            ++ndigit[c-'0']; 
            /* take away '0' byte value (lowest out of them all)
               which will give a 0-9 value (as required by the array) 
               this is possible as char values as stored as ints */
        else if (c == ' ' || c == '\n')
            ++nwhite; /* count whitespace! */
        else
            ++nother; /* count anything else */
    }

    printf("digits =");
    for (i = 0; i < 10; ++i) 
        printf(" %d", ndigit[i]);

    printf(", whitespace: %d, other: %d\n", nwhite, nother);
}