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

element_t *Recherche_val(element_t *ensemble, int val)
{
    element_t *ptr = ensemble;

    while ((ptr != NULL) && (ptr->valeur != val))
    {
        ptr = ptr->suivant;
    }
    return ptr;
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

element_t *Ajout_tete_ensemble(element_t *ensemble, int val, int freq)
{
    element_t *element = Recherche_val(ensemble, val);
    if (element != NULL)
    {
        element->frequence += freq;
    }
    else
    {
        element_t *nouvelElement = malloc(sizeof(element_t));
        nouvelElement->valeur = val;
        nouvelElement->frequence = freq;
        nouvelElement->suivant = ensemble;
        ensemble = nouvelElement;
    }
    return ensemble;
}

int main()
{
    {
        element_t *ensemble;
        int val;
        ensemble = NULL;
        for (val = 1; val <= 10; val++)
        {
            ensemble = Ajout_tete_ensemble(ensemble, val, val);
        }
        Affiche_ensemble(ensemble);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *ensemble;
        int val;
        ensemble = NULL;
        for (val = 1; val <= 10; val = val + 3)
        {
            ensemble = Ajout_tete_ensemble(ensemble, val, val);
        }
        ensemble = Ajout_tete_ensemble(ensemble, 4, 2);
        Affiche_ensemble(ensemble);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *ensemble;
        int val;
        ensemble = NULL;
        for (val = 1; val <= 10; val = val + 2)
        {
            ensemble = Ajout_tete_ensemble(ensemble, val, val);
        }
        ensemble = Ajout_tete_ensemble(ensemble, 9, 3);
        Affiche_ensemble(ensemble);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *ensemble;
        int val;
        ensemble = NULL;
        for (val = 1; val <= 10; val = val + 2)
        {
            ensemble = Ajout_tete_ensemble(ensemble, val, val);
        }
        ensemble = Ajout_tete_ensemble(ensemble, 1, 5);
        Affiche_ensemble(ensemble);
        ;
    }
    return 0;
}