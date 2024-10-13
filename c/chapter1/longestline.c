#include <stdio.h>
#define MAXLINE 1000 /* the maximum input line length!!! */

int getline(char line[], int maxline);
void copy(char to[], char from[]);

int main () 
{
    int len; /* current line length */
    int max; /* maximum length seen so far */
    char line[MAXLINE]; /* current input line */
    char longest[MAXLINE]; /* longest line saved here */

    max = 0;
    /* as long as lines are being received */
    while ((len = getline(line, MAXLINE)) > 0)
        if (len > max) { /* if line is longer than seen before, */
            max = len; /* copy its length into max */
            copy(longest, line); /* and copy its value into longest */
        }
    if (max > 0) /* there was a line */
        printf("%s", longest);

    return 0;
}

/* getline: read a line into s and return the length! */
int getline(char s[], int lim) /* lim is maximum input line length */
{
    int c, i;

    for (i = 0; i < lim-1 && (c = getchar()) != EOF && c != '\n'; i++)
        /* add new character into s (array of chars) */
        s[i] = c; 
    if (c == '\n') {
        /* if end of line, add this end of line and ++i so the \0 also gets saved */
        s[i] = c;
        ++i;
    }

    s[i] = '\0';
    return i;
}

/* copy "from" into "to"; assume to is big enough */
void copy(char to[], char from[])
{
    int i;

    i = 0;
    while ((to[i] = from[i]) != '\0')
        ++i;
}
