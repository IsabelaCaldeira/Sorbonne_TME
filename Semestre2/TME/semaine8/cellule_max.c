#include <stdio.h>

typedef struct _cellule_t cellule_t;

struct _cellule_t {
  int donnee;
  cellule_t *suivant;
};

cellule_t* maximum(cellule_t *liste){
    cellule_t *current = liste;
    cellule_t *max = liste;
    
    while (current != NULL) {
        if (current->donnee > max->donnee) {
            max = current;
        }
        current = current->suivant;
    }
    
    return max;

}

int main() {
   int n;
   scanf("%d", &n);
   /* creation d'une liste de n elements */
   cellule_t *ma_liste = creerListe(n);
   /* la fonction le_max calcule le resultat attendu */
   assert( maximum(ma_liste) == le_max(ma_liste) );
   return 0;
}