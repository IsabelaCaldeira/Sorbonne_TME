#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#define SEPARATOR "#<ab@17943918#@>#"

#define NB_JOURS 8
#define NB_AMIS 4

void afficheTableau(float tab[][NB_JOURS], int taille)
{
    int j, i;

    for (i = 0; i < taille; i++)
    {
        printf("AMI %d : ", i + 1);
        for (j = 0; j < NB_JOURS; j++)
        {
            printf(" Jour %d : %3.2f", j + 1, tab[i][j]);
        }
        printf("\n");
    }
}

void init_zero(float tab[][NB_JOURS], int taille){   
    for (int i = 0; i < taille; i++){
        for (int j = 0; j < NB_JOURS; j++){
            tab[i][j] = 0.0;
        }
    }
}

void affecte_depenses(float tab[][NB_JOURS], int jour, float montant, int id) {
    for (int i = 0; i < NB_AMIS; i++){
        for (int j = 0; j < NB_JOURS; j++){
            if (j == jour){
                if(i == id) tab[i][j] = montant - montant/NB_AMIS;
                else tab[i][j] = -montant/NB_AMIS;
            }
        }
    }
}

int main()
{
    {
        float depenses[NB_AMIS][NB_JOURS];
        init_zero(depenses, NB_AMIS);
        afficheTableau(depenses, NB_AMIS);
        ;
    }
    return 0;
}
