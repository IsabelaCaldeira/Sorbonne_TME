#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#define SEPARATOR "#<ab@17943918#@>#"

typedef struct _element_t element_t;
struct _element_t{
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

element_t *CreationMultiEnsemble(int deb, int n, int freq){
  element_t *liste=NULL;
  int i;
  
  for (i=deb+n-1; i >=deb; i--) {
    liste=Ajout_tete_ensemble(liste,i,freq);
  }
  return liste;
}

int Intersection_vide(element_t *ens1, element_t *ens2){
    element_t *e1 = ens1;
    element_t *e2 = ens2;

    while(e1 && e2){
        if(e1 -> valeur == e2 -> valeur) return 0;
        else {
            if(e1 -> valeur > e2 -> valeur) e2 = e2 -> suivant;
            else e1 = e1 -> suivant;
        }
    }
    return 1;
}

int main() {
   {
    element_t *ensemble1= CreationMultiEnsemble(1,10,1);
element_t *ensemble2= CreationMultiEnsemble(1,10,2);
printf("%d\n",Intersection_vide(ensemble1, ensemble2));;
   }
    printf("%s\n", SEPARATOR);   {
    element_t *ensemble1= CreationMultiEnsemble(1,10,1);
element_t *ensemble2= CreationMultiEnsemble(1,10,2);
printf("%d\n", Intersection_vide(ensemble2, ensemble1));;
   }
    printf("%s\n", SEPARATOR);   {
    element_t *ensemble1= CreationMultiEnsemble(11,20,1);
element_t *ensemble2= CreationMultiEnsemble(1,10,2);
printf("%d\n", Intersection_vide(ensemble1, ensemble2));;
   }
    printf("%s\n", SEPARATOR);   {
    element_t *ensemble1= CreationMultiEnsemble(11,20,1);
element_t *ensemble2= CreationMultiEnsemble(1,10,2);
printf("%d\n", Intersection_vide(ensemble2, ensemble1));
;
   }
    printf("%s\n", SEPARATOR);   {
    element_t *ensemble2= CreationMultiEnsemble(5,20,2);
printf("%d\n", Intersection_vide(NULL, ensemble2));;
   }
    printf("%s\n", SEPARATOR);   {
    element_t *ensemble2= CreationMultiEnsemble(5,20,2);
printf("%d\n", Intersection_vide(ensemble2,NULL));;
   }
    printf("%s\n", SEPARATOR);   {
    element_t *ensemble1= CreationMultiEnsemble(3,10,1);
printf("%d\n", Intersection_vide(ensemble1, ensemble1));;
   }
    printf("%s\n", SEPARATOR);   {
    element_t *ensemble1= CreationMultiEnsemble(1,20,1);
element_t *ensemble2= CreationMultiEnsemble(5,10,2);
printf("%d\n",Intersection_vide(ensemble1, ensemble2));;
   }
    printf("%s\n", SEPARATOR);   {
    element_t *ensemble1= CreationMultiEnsemble(1,20,1);
element_t *ensemble2= CreationMultiEnsemble(5,10,2);
printf("%d\n",Intersection_vide(ensemble2, ensemble1));;
   }
        return 0;
}