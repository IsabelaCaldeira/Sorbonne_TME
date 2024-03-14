#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#define SEPARATOR "#<ab@17943918#@>#"

#define NB_JOURS 7
#define NB_AMIS 4

void init_zero(float tab[][NB_JOURS], int taille) {
   int i, j;
   
   for (i = 0; i < taille; i++) {
      for (j = 0; j < NB_JOURS; j++) {
         tab[i][j] = 0;
      }
   }
}

void affecte_depenses(float tab[][NB_JOURS], int jour, float montant, int id) {
   int i;
   
   tab[id][jour] = montant - ((montant * 1.0) / NB_AMIS);   
   for (i = 0; i < NB_AMIS; i++) {
      if (i != id) {
         tab[i][jour] = - ((montant * 1.0) / NB_AMIS);
      }
   }
}

float calcul_solde(float tab[][NB_JOURS], int id)
{
    float res = 0;
    for (int i = 0; i < NB_JOURS; i++)
    {
        res += tab[id][i];
    }
    return res;
}

void affiche_soldes(float tab[][NB_JOURS])
{

    /* format d'affichage a respecter pour chaque membre
    du groupe */
    for (int i = 0; i < NB_AMIS; i++)
    {
        printf("Solde pour %d : %.2f\n", i, calcul_solde(tab, i));
    }
}

int main()
{
    {
        float depenses[NB_AMIS][NB_JOURS];
        init_zero(depenses, NB_AMIS);
        affecte_depenses(depenses, 0, 50.0, 2);
        affiche_soldes(depenses);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        float depenses[NB_AMIS][NB_JOURS];
        init_zero(depenses, NB_AMIS);
        affecte_depenses(depenses, 0, 50.0, 2);
        affecte_depenses(depenses, 1, 40.0, 3);
        affiche_soldes(depenses);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        float depenses[NB_AMIS][NB_JOURS];
        init_zero(depenses, NB_AMIS);
        affecte_depenses(depenses, 0, 37.0, 1);
        affecte_depenses(depenses, 1, 32.0, 2);
        affecte_depenses(depenses, 2, 43.0, 0);
        affecte_depenses(depenses, 3, 39.0, 2);
        affecte_depenses(depenses, 4, 38.0, 1);
        affecte_depenses(depenses, 5, 36.0, 1);
        affecte_depenses(depenses, 6, 30.0, 2);
        affiche_soldes(depenses);
        ;
    }
    return 0;
}