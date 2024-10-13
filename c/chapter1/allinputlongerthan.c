#include <stdio.h>

#define LONGERTHAN 80

int main() 
{
    int i = 0; /* character in line counter */
    int c;
    char line[LONGERTHAN];

    while ((c = getchar()) != EOF) {
        if (c == '\n') {
            i = 0;
        }
        if (i > LONGERTHAN) {
            line[i] = c;
            printf("%s\n", line);
            i = 0;
            continue;
        }
        else {
            line[i] = c;
            i++;
        }
    }

    return 0;
}