#include <stdio.h>
#include <stdlib.h>

typedef struct Date{
    int jour;
    int mois;
    int annee;
} Date;

void afficher_mois(char *mois[], int jours[]){
    for(int i = 0; i < 12; i++) printf("%d %s: %d jours\n",i, mois[i], jours[i]);
}

void afficher_date(Date d){
    printf(" %d/%d/%d ",d.jour, d.mois, d.annee);
}

int cmp_date(Date d1, Date d2){
    if(d2.annee < d1.annee) return 1;
    if(d2.annee > d1.annee) return -1;
    if(d2.mois < d1.mois) return 1;
    if(d2.mois > d1.mois) return -1;
    if(d2.jour < d1.jour) return 1;
    if(d2.jour > d1.jour) return -1;
    return 0;
}

int main() {
    int jours[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
    char * mois[12] = {"janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"};
    afficher_mois(mois, jours);
    afficher_date((Date){1,1,2022});
    return 0;
}

