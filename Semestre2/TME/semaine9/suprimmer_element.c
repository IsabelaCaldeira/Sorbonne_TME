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

element_t *Supprime_total_element(element_t * ensemble, int val) {
    element_t *current = ensemble;
    element_t *prev = NULL;
    
    while(current){
        if(current -> valeur == val){
            if(!prev) ensemble = current -> suivant;
            else prev-> suivant = current-> suivant;
            free(current);
            break;
        }
        prev = current;
        current = current -> suivant;
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
        ensemble = Supprime_total_element(ensemble, 5);
        Affiche_ensemble(ensemble);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *ensemble;
        int val;
        ensemble = NULL;
        for (val = 1; val <= 10; val++)
        {
            ensemble = Ajout_tete_ensemble(ensemble, val, val);
        }
        ensemble = Supprime_total_element(ensemble, 1);
        Affiche_ensemble(ensemble);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *ensemble;
        int val;
        ensemble = NULL;
        for (val = 1; val <= 10; val++)
        {
            ensemble = Ajout_tete_ensemble(ensemble, val, val);
        }
        ensemble = Supprime_total_element(ensemble, 10);
        Affiche_ensemble(ensemble);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *ensemble;
        int val;
        ensemble = NULL;
        for (val = 1; val <= 10; val++)
        {
            ensemble = Ajout_tete_ensemble(ensemble, val, val);
        }
        ensemble = Supprime_total_element(ensemble, -4);
        Affiche_ensemble(ensemble);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *ensemble = NULL;
        ensemble = Ajout_tete_ensemble(ensemble, 3, 7);
        ensemble = Supprime_total_element(ensemble, 3);
        Affiche_ensemble(ensemble);
        ;
    }
    return 0;
}