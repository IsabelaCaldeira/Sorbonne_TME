#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#define SEPARATOR "#<ab@17943918#@>#"

int recherche_iter(int *tab, int taille, int elem){
    int i;
    for(i = 0; i<taille; i++){
        if (tab[i] == elem) return i;
    }
    return -1;
}

int recherche_rec_aux(int tab[], int taille, int indice, int elem){
    if(tab[indice] == elem) return indice;
    else{
        if(indice == taille) return -1;
        else return recherche_rec_aux(tab, taille, indice + 1, elem);
    }
}

int recherche_rec1(int *tab, int taille, int val){
    if(tab[taille-1] == val) return -1;
    if(taille == 0) return -1;
    return recherche_rec1(tab, taille-1, val);
}

int recherche_rec(int *tab, int taille, int elem){
    return recherche_rec_aux (tab, taille, 0, elem);
}

int main() {
   {
    int tab[]={1,1,1,1,1,1,1};
printf("%d\n",recherche_rec(tab,7,1));;
   }
    printf("%s\n", SEPARATOR);   {
    int tab[]={1,1,1,1,1,1,1};
printf("%d\n",recherche_rec(tab,7,5));;
   }
    printf("%s\n", SEPARATOR);   {
    int tab[]={1,2,3,4,5,6,7,8,9,10};
printf("%d\n",recherche_rec(tab,10,1));;
   }
    printf("%s\n", SEPARATOR);   {
    int tab[]={10,9,8,7,6,5,4,3,2,1};
printf("%d\n",recherche_rec(tab,10,6));;
   }
    printf("%s\n", SEPARATOR);   {
    int tab[]={1,2,1,2,1,2,1,2,1,2,1,2};
printf("%d\n",recherche_rec(tab,12,2));;
   }
    printf("%s\n", SEPARATOR);   {
    int tab[]={10,2,9,3,8,1,7,4,6,5};
printf("%d\n",recherche_rec(tab,10,5));;
   }
        return 0;
}