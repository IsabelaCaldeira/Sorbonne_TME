#include <stdio.h>
#include <stdlib.h>

typedef struct _cellule_t cellule_t;

struct _cellule_t {
  int donnee;
  cellule_t *suivant;
};

int nb_occurences(int val, cellule_t *liste) {
    int count = 0;
    cellule_t *current = liste;

    while(current != NULL) {
        if(current->donnee == val) {
            count++;
        }
        current = current->suivant;
    }

    return count;
}

int main() {
   int el, n;
   scanf("%d", &n);
   /* creation d'une liste de n elements */
   cellule_t *ma_liste = creerListe(n);
   scanf("%d", &el);
   printf("%d\n", nb_occurences(el, ma_liste));
   return 0;
}