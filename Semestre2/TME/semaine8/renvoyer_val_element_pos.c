#include <stdio.h>

typedef struct _cellule_t cellule_t;

struct _cellule_t {
  int donnee;
  cellule_t *suivant;
};

int renvoyer_val_element_pos(int pos, cellule_t* liste){
    cellule_t* current = liste;
    int compteur = 0;
    
    while(current != NULL){
        if(compteur == pos) return current -> donnee;
        current = current -> suivant;
        compteur++;
    }
    return -1;
}

int main() {
   int i, n;
   scanf("%d", &n);
   cellule_t *ma_liste = creerListe(n);
   scanf("%d", &i);
   assert (i >= 0 && i < n);
   printf("%d\n", renvoyer_val_element_pos(i, ma_liste));
   return 0;
}