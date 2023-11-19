#include <stdio.h>
#include <stdlib.h>

int main()
{
    int zahl1 = 10;
    int zahl2 = 5;

    int zahl3 = zahl1 * zahl2;
    int zahl4 = zahl1 / zahl2;
    int zahl5 = zahl1 + zahl2;
    int zahl6 = zahl1 - zahl2;

    printf("%d\n", zahl3);
    printf("%d\n", zahl4);
    printf("%d\n", zahl5);
    printf("%d\n", zahl6);

    int zahl7 = 7;
    int zahl8 = 8;

    int zahl9 = zahl8 % zahl7;

    printf("%d\n", zahl9);

    int zahl10 = 10;
    zahl10 = zahl10 + 1;
    printf("%d\n", zahl10);

    return 0;
}
