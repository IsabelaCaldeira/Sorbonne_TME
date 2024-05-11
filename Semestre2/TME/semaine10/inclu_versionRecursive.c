#include <stdio.h>
#include <stdlib.h>

typedef struct _element_t element_t;

struct _element_t
{
    int valeur;
    int frequence;
    element_t *suivant;
};

int inclus_rec(element_t *ens1, element_t *ens2)
{
    if (ens1 == NULL)
        return 1;

    if (ens2 == NULL)
        return 0;

    if (ens1->valeur < ens2->valeur)
        return 0;

    if (ens1->valeur == ens2->valeur)
    {
        if (ens1->frequence > ens2->frequence)
            return 0;

        return inclus_rec(ens1->suivant, ens2->suivant);
    }

    return inclus_rec(ens1, ens2->suivant);

}

int main()
{
    int n1, n2;
    scanf("%d", &n1);
    /* creation d'un multi-ensemble trie contenant n1 valeurs differentes */
    element_t *multiE1 = creer_multiEnsemble(n1);
    scanf("%d", &n2);
    printf("multiE1 : ");
    affiche_ensemble(multiE1);
    /* creation d'un multi-ensemble trie contenant n2 valeurs differentes */
    element_t *multiE2 = creer_multiEnsemble(n2);
    printf("multiE2 : ");
    affiche_ensemble(multiE2);
    printf("%d\n", inclus_rec(multiE1, multiE2));
    return 0;
}