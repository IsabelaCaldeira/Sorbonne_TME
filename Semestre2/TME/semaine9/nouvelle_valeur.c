#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#define SEPARATOR "#<ab@17943918#@>#"

typedef struct _element_t element_t;
struct _element_t
{
    int valeur;
    int frequence;
    element_t *suivant;
};
element_t *Recherche_val2(element_t *ensemble, int val)
{
    element_t *ptr = ensemble;

    while ((ptr != NULL) && (ptr->valeur != val))
    {
        ptr = ptr->suivant;
    }
    return ptr;
}

/* Ajoute l'element val en tete de l'ensemble s'il n'apparait pas dans l'ensemble, augmente sa frequence de freq sinon */
element_t *Ajout_tete_ensemble(element_t *ensemble, int val, int freq)
{
    element_t *ptr;

    ptr = Recherche_val2(ensemble, val);
    if (ptr != NULL)
    {
        ptr->frequence = ptr->frequence + freq;
        return ensemble;
    }
    else
    {
        ptr = malloc(sizeof(element_t));
        ptr->valeur = val;
        ptr->frequence = freq;
        ptr->suivant = ensemble;
        return ptr;
    }
}

/* Affche tous les elements d'un ensemble avec leur frequence */
void Affiche_ensemble(element_t *ensemble)
{
    element_t *ptr = ensemble;

    while (ptr != NULL)
    {
        printf("val : %d, frequence : %d\n", ptr->valeur, ptr->frequence);
        ptr = ptr->suivant;
    }
}

element_t *CreationMultiEnsemble(int n, int freq)
{
    element_t *liste = NULL;
    int i;

    for (i = n; i >= 1; i--)
    {
        liste = Ajout_tete_ensemble(liste, i, freq);
    }
    return liste;
}

element_t *Supprime_element_ensemble_trie(element_t *ensemble, int val)
{
    element_t *current = ensemble;
    element_t *previous = NULL;

    while (current != NULL)
    {
        if (current->valeur == val)
        {
            if (current->frequence > 1)
            {
                current->frequence--;
            }
            else
            {
                if (previous != NULL)
                {
                    previous->suivant = current->suivant;
                }
                else
                {
                    ensemble = current->suivant;
                }
                free(current);
            }
            break;
        }
        previous = current;
        current = current->suivant;
    }

    return ensemble;
}

int main()
{
    {
        element_t *ensemble = CreationMultiEnsemble(10, 1);
        ensemble = Supprime_element_ensemble_trie(ensemble, 5);
        Affiche_ensemble(ensemble);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *ensemble = CreationMultiEnsemble(10, 1);
        ensemble = Supprime_element_ensemble_trie(ensemble, 10);
        Affiche_ensemble(ensemble);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *ensemble = CreationMultiEnsemble(10, 1);
        ensemble = Supprime_element_ensemble_trie(ensemble, 1);
        Affiche_ensemble(ensemble);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *ensemble = CreationMultiEnsemble(10, 2);
        ensemble = Supprime_element_ensemble_trie(ensemble, 4);
        Affiche_ensemble(ensemble);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *ensemble = CreationMultiEnsemble(10, 2);
        ensemble = Supprime_element_ensemble_trie(ensemble, 50);
        Affiche_ensemble(ensemble);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *ensemble = CreationMultiEnsemble(1, 1);
        ensemble = Supprime_element_ensemble_trie(ensemble, 1);
        Affiche_ensemble(ensemble);
        ;
    }
    return 0;
}
