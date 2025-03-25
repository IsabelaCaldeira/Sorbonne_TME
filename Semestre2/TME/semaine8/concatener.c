#include <stdio.h>

typedef struct _cellule_t cellule_t;

struct _cellule_t {
  int donnee;
  cellule_t *suivant;
};

cellule_t* concatener(cellule_t *liste1, cellule_t *liste2) {
    if(!liste1) return liste2;
    if(!liste2) return liste1;

    cellule_t* current = liste1;
    while(current -> suivant != NULL) current = current -> suivant;
    current -> suivant = liste2;

    return liste1;

}

int main() {
   int n1, n2;
   scanf("%d", &n1);
   cellule_t *liste1 = creerListe(n1);
   scanf("%d", &n2);
   cellule_t *liste2 = creerListe(n2);
   afficher_liste_int(concatener(liste1, liste2));
   return 0;
}