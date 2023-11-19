#include <stdio.h>
#include <stdlib.h>

int main()
{
    int zahl1;
    printf("Geben Sie Zahl1 ein");
    scanf("%d", &zahl1);

    if (zahl1 > 4)
    {
        printf("Die Zahl ist groesser 4");
    }
    else if (zahl1 < 4)
        printf("Die Zahl ist kleiner 4");
    else
        printf("Die Zahl ist gleich 4");

    return 0;
}
