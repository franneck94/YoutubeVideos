#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *eingabe(char *str)
{
    char input[100];
    printf("Bitte \"%s\" eingeben: ", str);
    fgets(input, 100, stdin);
    return strtok(input, "\n");
}

int main()
{
    char *ptr;

    ptr = eingabe("Vorname");
    printf("Hallo %s\n", ptr);
    ptr = eingabe("Nachname");
    printf("%s, interessanter Nachname\n", ptr);
    return 0;
}
