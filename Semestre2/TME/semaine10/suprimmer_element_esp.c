#include <stdio.h>
#include <stdlib.h>

typedef struct _element_t element_t;

struct _element_t
{
    int valeur;
    int frequence;
    element_t *suivant;
};

element_t *supprime_frequence_inf_seuil(element_t *ens, int seuil)
{
    element_t *courant = ens;
    element_t *precedent = NULL;

    while (courant != NULL)
    {
        if (courant->frequence < seuil)
        {
            if (precedent == NULL)
            {
                ens = courant->suivant;
            }
            else
            {
                precedent->suivant = courant->suivant;
            }
            element_t *temp = courant;
            courant = courant->suivant;
            free(temp);
        }
        else
        {
            precedent = courant;
            courant = courant->suivant;
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