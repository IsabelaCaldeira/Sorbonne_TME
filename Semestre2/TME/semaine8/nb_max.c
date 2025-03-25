#include <stdio.h>

typedef struct _cellule_t cellule_t;

struct _cellule_t {
  int donnee;
  cellule_t *suivant;
};

int nb_maximum(cellule_t *liste) {
    if(!liste) return 0;
    cellule_t* current = liste;
    int compteur = 0, max = current->donnee;
    while(current){
        if(current -> donnee > max) {
            max = current -> donnee;
            compteur = 0;
        }
        if(current -> donnee == max) compteur++;
        current = current -> suivant;
    }
    return compteur;
}

int main() {
   int n;
   scanf("%d", &n);
   /* creation d'une liste de n elements */
   cellule_t *ma_liste = creerListe(n);
   printf("%d\n", nb_maximum(ma_liste));
   return 0;
}