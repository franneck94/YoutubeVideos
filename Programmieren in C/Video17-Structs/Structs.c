#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Adresse
{
    char Name[200];
    char Ort[200];
    int Anzahl_der_Eintraege;
    char Geburtsdatum[100];
};

int main()
{
    struct Adresse Namen;
    Namen.Anzahl_der_Eintraege = 1;
    strcpy(Namen.Name, "Jan");
    strcpy(Namen.Ort, "Deutschland");
    strcpy(Namen.Geburtsdatum, "01.01.1900");

    printf("Anzahl: %d\n", Namen.Anzahl_der_Eintraege);
    printf("Name: %s\n", Namen.Name);
    printf("Ort: %s\n", Namen.Ort);
    printf("Geburtsdatum %s\n", Namen.Geburtsdatum);

    return 0;
}
