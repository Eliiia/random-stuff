#include <stdio.h>

int main()
{
    int c;
    char l = EOF;

    while ((c = getchar()) != EOF) 
    {
        if (!(c == ' ' && l == ' ')) printf("%c",c);
        l = c;
    }

    return 0;
}