#include <stdio.h>
#include <stdlib.h>

int main()
{
    int zahl1;
    int zahl2;

    printf("Geben Sie eine Zahl ein!");
    scanf("%d", &zahl1);
    printf("Geben Sie eine Zahl ein!");
    scanf("%d", &zahl2);

    int zahl3 = zahl1 + zahl2;

    printf("%d", zahl3);

    return 0;
}
