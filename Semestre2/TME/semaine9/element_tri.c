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

element_t * Recherche_val2(element_t *ensemble, int val) {
  element_t *ptr = ensemble;
  
  while ((ptr != NULL) && (ptr->valeur != val)){
    ptr=ptr->suivant;
  }
  return ptr;
} 

/* Ajoute l'element val en tete de l'ensemble s'il n'apparait pas dans l'ensemble, augmente sa frequence de freq sinon */
element_t * Ajout_tete_ensemble(element_t *ensemble, int val, int freq) {
  element_t *ptr;
 
  ptr = Recherche_val2(ensemble,val);
  if (ptr != NULL) {
    ptr->frequence = ptr->frequence+freq;
    return ensemble;
  } else {
    ptr=malloc(sizeof(element_t));
    ptr->valeur=val;
    ptr->frequence=freq;
    ptr->suivant=ensemble;
    return ptr;
  }
}

/* Affche tous les elements d'un ensemble avec leur frequence */
void Affiche_ensemble(element_t *ensemble) {
  element_t *ptr = ensemble;
  
  while (ptr != NULL) {
    printf("val : %d, frequence : %d\n",ptr->valeur,ptr->frequence);
    ptr=ptr->suivant;
  }
}

element_t *CreationMultiEnsemble(int n){
  element_t *liste=NULL;
  int i;
  
  for (i=n; i >=1; i--) {
    liste=Ajout_tete_ensemble(liste,2*i,2*i);
  }
  return liste;
}

element_t *Ajout_ensemble_trie(element_t *ensemble, int val, int freq)
{
    element_t *new = malloc(sizeof(element_t));
    new->valeur = val;
    new->frequence = freq;
    new->suivant = NULL;

    if (ensemble == NULL)
    {
        return new;
    }

    element_t *current = ensemble;
    element_t *previous = NULL;

    while (current != NULL)
    {
        if (current->valeur == val)
        {
            current->frequence += freq;
            free(new);
            return ensemble;
        }
        else if (current->valeur > val)
        {
            if (previous == NULL)
            {
                new->suivant = ensemble;
                return new;
            }
            else
            {
                previous->suivant = new;
                new->suivant = current;
                return ensemble;
            }
        }
        previous = current;
        current = current->suivant;
    }

    previous->suivant = new;
    return ensemble;
}

int main()
{
    {
        element_t *ensemble = NULL;
        ensemble = Ajout_ensemble_trie(ensemble, 4, 2);
        Affiche_ensemble(ensemble);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *ensemble = CreationMultiEnsemble(4);
        ensemble = Ajout_ensemble_trie(ensemble, 6, 2);
        Affiche_ensemble(ensemble);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *ensemble = CreationMultiEnsemble(4);
        ensemble = Ajout_ensemble_trie(ensemble, 9, 2);
        Affiche_ensemble(ensemble);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *ensemble = ensemble = CreationMultiEnsemble(4);
        ensemble = Ajout_ensemble_trie(ensemble, 0, 1);
        Affiche_ensemble(ensemble);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *ensemble = ensemble = CreationMultiEnsemble(4);
        ensemble = Ajout_ensemble_trie(ensemble, 5, 2);
        Affiche_ensemble(ensemble);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *ensemble = NULL;
        int val;
        for (val = 1; val <= 10; val++)
        {
            ensemble = Ajout_ensemble_trie(ensemble, val, val);
        }
        Affiche_ensemble(ensemble);
        ;
    }
    printf("%s\n", SEPARATOR);
    {
        element_t *ensemble = NULL;
        int val;
        for (val = 10; val >= 1; val--)
        {
            ensemble = Ajout_ensemble_trie(ensemble, val, val);
        }
        Affiche_ensemble(ensemble);
        ;
    }
    return 0;
}
