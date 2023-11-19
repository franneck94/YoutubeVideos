#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void String_Vergleichen(char s1[], char s2[]) {
    int ret = strcmp(s1, s1);
    if (ret == 0)
        printf("%s == %s\n", s1, s2);
    else
        printf("sind nicht gleich\n");
}

int main(void)
{
    char str1[] = "aaa";
    char str2[] = "aab";
    char str3[] = "bba";

    String_Vergleichen(str1, str2);
    String_Vergleichen(str1, str3);
    String_Vergleichen(str3, str2);
    String_Vergleichen(str1, str1);

    return 0;
}
