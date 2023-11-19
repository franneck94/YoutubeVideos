#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fp;
    int i; int temp;

    fp = fopen("C:\\Users\\Jan\\Desktop\\kurt.txt", "r");

    if (fp == NULL)
    {
        printf("Datei konnte nicht geoeffnet werden. \n");
    }
    else
    {
        for (i = 0; i < 10; i++) {
            facanf(fp, "%d\n", &temp);
            printf("gelesen: %d\n", temp);
        }
        fclose(fp);
    }

    return 0;
}
