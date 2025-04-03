#include <stdio.h>
#include <stdlib.h>

typedef struct _element_t element_t;

struct _element_t
{
    int valeur;
    int frequence;
    element_t *suivant;
};

element_t* supprime_frequence_inf_seuil(element_t* ens, int seuil) {
    element_t *courrant = ens;
    element_t * prec = NULL;
    while(courrant){
        if(courrant -> frequence < seuil){
            if(!prec) ens = courrant -> suivant;
            else prec -> suivant = courrant -> suivant;
            element_t *supprime = courrant;
            courrant = courrant -> suivant;
            free(supprime);
        }else{
            prec = courrant;
            courrant = courrant -> suivant;
        }
    }
    return ens;
}

int main()
{
    int n, s;
    scanf("%d", &n);
    /* creation d'un multi-ensemble contenant n valeurs differentes */
    element_t *multiE = creer_multiEnsemble(n);
    scanf("%d", &s);
    affiche_ensemble(multiE);
    printf("seuil : %d. ", s);
    multiE = supprime_frequence_inf_seuil(multiE, s);
    affiche_ensemble(multiE);
    return 0;
}