#include <stdio.h>
#include <stdlib.h>

int bignum(int a, int b) {
    if (a > b)
        return a;
    else if (a < b)
        return b;
    else
        return 0;
}

int main()
{
    int wert1, wert2, big;
    printf("Zahl eingeben ");
    scanf("%d", &wert1);
    printf("Zahl eingeben ");
    scanf("%d", &wert2);

    big = binum(wert1, wert2);
    if (big != 0)
        printf("%d is die größer der beiden Zahlen\n", big);
    else
        printf("Beide Zahlen haben denselben Wert\n");

    return 0;
}
