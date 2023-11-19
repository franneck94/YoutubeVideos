#include <stdio.h>
#include <stdlib.h>

int main()
{
    int zahl1 = 6;

    do
    {
        zahl1++;
        printf("Ich bin zwichen 5 und 10\n");
    } while (zahl1 > 5 && zahl1 < 10);

    return 0;
}
