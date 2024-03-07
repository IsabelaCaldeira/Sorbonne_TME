#include <stdio.h>

int indiceInsert(int tab[], int el, int nb, int taille){
    int i;
    if (nb == taille) return -1;
    for (i = 0; i < nb; i++){
        if (tab[i] == el) return -1;
        else if (el < tab[i]) return i;
    }
    if (el > tab[nb - 1]) return nb;
    return 0;
}

int insertElt(int* tab, int val, int* nbEL, int taille) {
    int indice = indiceInsert(tab, val, *nbEL, taille);
    if (indice != -1){
        if (*nbEL < taille){
            int i;
            for (i = *nbEL; i > indice; i--){
                   tab[i] = tab[i -1];
            }       
            tab[indice] = val;
            (*nbEL)++;
            return 1;
        }
    }
    return 0;
}

void affiche_tab(int tab[], int taille) {
    int i;
    for (i = 0; i < taille; i++) {
        printf("%d  ", tab[i]);
    }
    printf("\n");
}

int main() {
   int tab[6];
   int i, inser_OK, nbEl, val;
   
   scanf("%d", &nbEl);
   for (i = 0; i < nbEl; i++) {
      scanf("%d", tab + i);
   }
   scanf("%d", &val);
 
   inser_OK = insertElt(tab, val, &nbEl, 6);
   printf("insertion OK ? %d\n", inser_OK);
   affiche_tab(tab, nbEl);
   return 0;
}