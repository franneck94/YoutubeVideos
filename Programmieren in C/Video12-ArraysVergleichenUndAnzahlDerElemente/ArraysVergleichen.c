#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int i; int array1[10], array2[10];

    for (i = 0; i < 10; i++)
    {
        array1[i] = i;
        array2[i] = 1;
    }

    for (i = 0; i < 10; i++)
    {
        if (array1[i] == array2[i])
            continue;
        else {
            printf("Unterschied an Position %d\n", i);
            break;
        }
    }

    return 0;
}
