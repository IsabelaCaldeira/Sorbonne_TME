#include <stdio.h>
#include <stdlib.h>

typedef struct _element_t element_t;

struct _element_t{
  int valeur;
  int frequence;
  element_t *suivant;
};

element_t* ajout_tete_ensemble(element_t* ens, int valeur, int frequence) {
    element_t* new_element = (element_t*)malloc(sizeof(element_t));
    new_element->valeur = valeur;
    new_element->frequence = frequence;
    new_element->suivant = ens;
    return new_element;
}

element_t* creer_multiEnsemble(int n) {
    element_t* ens = NULL;
    for (int i = 0; i < n; i++) {
        int valeur;
        scanf("%d", &valeur);
        int frequence;
        scanf("%d", &frequence);
        ens = ajout_tete_ensemble(ens, valeur, frequence);
    }
    return ens;
}

element_t* ajout_suivant(element_t* element, int val, int freq) {
    element_t* nouveau = malloc(sizeof(element_t));
    nouveau->valeur = val;
    nouveau->frequence = freq;
    
    if (element == NULL) {
        nouveau->suivant = NULL;
        return nouveau;
    }
    
    nouveau->suivant = element->suivant;
    element->suivant = nouveau;
    
    return nouveau;
}

element_t* union_triee_rec(element_t* ens1, element_t* ens2) {
    if(!ens1) return ens2;
    if(!ens2) return ens1;

    element_t* res = NULL;

    if(ens1 -> valeur > ens2 -> valeur) res = ajout_tete_ensemble(union_triee_rec(ens1, ens2->suivant), ens2 -> valeur, ens2 -> frequence);
    else if(ens1 -> valeur < ens2 -> valeur) res = ajout_tete_ensemble(union_triee_rec(ens1 -> suivant, ens2), ens1 -> valeur, ens1 -> frequence);
    else res = ajout_tete_ensemble(union_triee_rec(ens1 -> suivant, ens2 -> suivant), ens1 -> valeur,ens1->frequence + ens2->frequence);
    
    return res;
}

int main() {
   int n1, n2;
   scanf("%d", &n1);
   /* creation d'un multi-ensemble trie contenant n1 valeurs differentes */
   element_t* multiE1 = creer_multiEnsemble(n1);
   scanf("%d", &n2);
   /* creation d'un multi-ensemble trie contenant n2 valeurs differentes */
   element_t* multiE2 = creer_multiEnsemble(n2);
   printf("Union : ");
   affiche_ensemble(union_triee_rec(multiE1, multiE2));
   /* on affiche les ensembles APRES pour verifier que l'union duplique les elements */
   printf("multiE1 : ");
   affiche_ensemble(multiE1);
   printf("multiE2 : ");
   affiche_ensemble(multiE2);
   return 0;
}