#include <stdio.h>
#include <stdlib.h>

int main()
{
    int zahl1;
    printf("Gib zahl ein");
    scanf("%d", &zahl1);

    switch (zahl1)
    {
    case 1: printf("EINS"); break;
    case 2: printf("ZWEI"); break;
    case 3: printf("DREI"); break;
    default: printf("NICHTS");
    }

    return 0;
}
