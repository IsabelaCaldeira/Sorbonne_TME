#include <stdio.h>

typedef struct _cellule_t cellule_t;

struct _cellule_t {
  int donnee;
  cellule_t *suivant;
};

int tous_plus_grands(int val, cellule_t* liste) {
    cellule_t* current = liste;
    
    while (current != NULL) {
        if (current->donnee < val) return 0;
        current = current->suivant;
    }
    
    return 1;
}


int main() {
   int el, n;
   scanf("%d", &n);
   /* creation d'une liste de n elements */
   cellule_t *ma_liste = creerListe(n);
   scanf("%d", &el);
   printf("%d\n", tous_plus_grands(el, ma_liste));
   return 0;
}