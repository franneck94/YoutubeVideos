#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int Array[] = { 1,2,3,4,5,6,7,8,9 };
    printf("anzahl der Elemente: %d \n", sizeof(Array) / sizeof(int));

    return 0;
}
