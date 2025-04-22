#include <stdio.h>
#include <stdlib.h>

typedef struct _element_t element_t;

struct _element_t{
    int valeur;
    int frequence;
    element_t *suivant;
};

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

element_t* union_triee(element_t* ens1, element_t* ens2) {
    element_t* tete = NULL;
    element_t* current = NULL;

    while(ens1 || ens2){
        int valeur, frequence;
        if(!ens1){
            valeur = ens2 -> valeur;
            frequence = ens2 -> frequence;
            ens2 = ens2 -> suivant;
        } else if(!ens2){
            valeur = ens1 -> valeur;
            frequence = ens1 -> frequence;
            ens1 = ens1 -> suivant;
        } else if(ens1 -> valeur < ens2 -> valeur){
            valeur = ens1 -> valeur;
            frequence = ens1 -> frequence;
            ens1 = ens1 -> suivant;
        } else if(ens1 -> valeur > ens2 -> valeur){
            valeur = ens2 -> valeur;
            frequence = ens2 -> frequence;
            ens2 = ens2 -> suivant;
        } else{
            valeur = ens2 -> valeur;
            frequence = ens2 -> frequence + ens1 -> frequence;
            ens1 = ens1 -> suivant;
            ens2 = ens2 -> suivant;
        }
        if(!tete){
            tete = ajout_suivant(tete, valeur, frequence);
            current = tete;
        } else current = ajout_suivant(current, valeur, frequence);
    }
    return tete;
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
   affiche_ensemble(union_triee(multiE1, multiE2));
   /* on affiche les ensembles APRES pour verifier que l'union duplique les elements */
   printf("multiE1 : ");
   affiche_ensemble(multiE1);
   printf("multiE2 : ");
   affiche_ensemble(multiE2);
   return 0;
}