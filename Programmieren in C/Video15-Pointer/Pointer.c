#include <stdio.h>
#include <stdlib.h>

int main()
{
    int b = 5;
    int *a;
    a = &b;

    printf("Speicheraddresse von b %d\n", b);
    printf("Speicheraddresse von a %d\n", *a);

    return 0;
}
