#include <stdio.h>
#include <stdlib.h>

typedef struct _element_t element_t;

struct _element_t
{
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

void affiche_ensemble(element_t* ens) {
    while (ens != NULL) {
        printf("(%d, %d) ", ens->valeur, ens->frequence);
        ens = ens->suivant;
    }
    printf("\n");
}

element_t* unionME(element_t* ens1, element_t* ens2) {
    element_t* current = NULL; 

    while(ens1 || ens2){
        if(!ens1){
            current = ajout_tete_ensemble(current, ens2 -> valeur, ens2 -> frequence);
            ens2 = ens2 -> suivant;
        } else if(!ens2){
            current = ajout_tete_ensemble(current, ens1 -> valeur, ens1 -> frequence);
            ens1 = ens1 -> suivant;
        } else if(ens1 -> valeur > ens2 -> valeur){
            current = ajout_tete_ensemble(current, ens1 -> valeur, ens1 -> frequence);
            ens1 = ens1 -> suivant;
        } else if(ens1 -> valeur < ens2 -> valeur){
            current = ajout_tete_ensemble(current, ens2 -> valeur, ens2 -> frequence);
            ens2 = ens2 -> suivant;
        } else{
            current = ajout_tete_ensemble(current, ens1 -> valeur,ens1->frequence + ens2->frequence);
            ens1 = ens1 -> suivant;
            ens2 = ens2 -> suivant;
        }
    }
    element_t* res = NULL;
    while(current) {
        element_t* temp = current;
        current = current->suivant;

        element_t* existeDeja = res;
        while (existeDeja && existeDeja->valeur != temp->valeur) {
            existeDeja = existeDeja->suivant;
        }

        if (existeDeja) {
            existeDeja->frequence += temp->frequence;
            free(temp);
        } else {
            if (!res || temp->valeur > res->valeur) {
                temp->suivant = res;
                res = temp;
            } else {
                element_t* current_sorted = res;
                while (current_sorted->suivant != NULL && current_sorted->suivant->valeur > temp->valeur) {
                    current_sorted = current_sorted->suivant;
                }
                temp->suivant = current_sorted->suivant;
                current_sorted->suivant = temp;
            }
        }
    }

    return res;
}


int main()
{
    int n1, n2;
    scanf("%d", &n1);
    /* creation d'un multi-ensemble trie contenant n1 valeurs differentes */
    element_t *multiE1 = creer_multiEnsemble(n1);
    scanf("%d", &n2);
    /* creation d'un multi-ensemble trie contenant n2 valeurs differentes */
    element_t *multiE2 = creer_multiEnsemble(n2);
    printf("Union : ");
    affiche_ensemble(unionME(multiE1, multiE2));
    /* on affiche les ensembles APRES (l'union ne doit pas modifier les listes) */
    printf("multiE1 : ");
    affiche_ensemble(multiE1);
    printf("multiE2 : ");
    affiche_ensemble(multiE2);
    return 0;
}