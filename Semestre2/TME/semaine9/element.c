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

element_t *CreationMultiEnsemble(int n)
{
    element_t *liste = NULL;
    int i;

    for (i = 1; i <= n; i++)
    {
        liste = Ajout_tete_ensemble(liste, i, i * 2);
    }
    return liste;
}
element_t *Recherche_val(element_t *ensemble, int val)
{
    element_t *current = ensemble;

    while (current != NULL)
    {
        if (current->valeur == val)
        {
            return current;
        }
        current = current->suivant;
    }

    return NULL;
}

int main()
{
    {
        element_t *liste = CreationMultiEnsemble(10);
        int val = 1;
        element_t *res = Recherche_val(liste, val);
        if (res != NULL)
        {
            printf("frequence %d = %d\n", val, res->frequence);
        }
        else
        {
            printf("%d non present dans le multi-ensemble\n", val);
        };
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *liste = CreationMultiEnsemble(10);
        int val = 10;
        element_t *res = Recherche_val(liste, val);
        if (res != NULL)
        {
            printf("frequence %d = %d\n", val, res->frequence);
        }
        else
        {
            printf("%d non present dans le multi-ensemble\n", val);
        };
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *liste = CreationMultiEnsemble(10);
        int val = 5;
        element_t *res = Recherche_val(liste, val);
        if (res != NULL)
        {
            printf("frequence %d = %d\n", val, res->frequence);
        }
        else
        {
            printf("%d non present dans le multi-ensemble\n", val);
        };
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *liste = CreationMultiEnsemble(10);
        int val = 15;
        element_t *res = Recherche_val(liste, val);
        if (res != NULL)
        {
            printf("frequence %d = %d\n", val, res->frequence);
        }
        else
        {
            printf("%d non present dans le multi-ensemble\n", val);
        };
    }
    return 0;
}