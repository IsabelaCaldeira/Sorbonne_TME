/* Nous souhaitons calculer la somme des valeurs paires d'un tableau d'entiers strictement positifs.

- Complétez la fonction sommePaires pour qu'elle retourne la somme de valeurs paires du tableau.
  La fonction doit prendre en paramètres le tableau et sa taille.

- Complétez la fonction main pour afficher le résultat.
  Le message affiché doit dépendre du résultat de l'appel à la fonction sommePaires.
  N'oubliez pas de remplacer les ... en paramètre des appels à printf.

Les éléments du tableau et sa taille sont définis par des primitives #define, ces valeurs seront modifiées pour tester votre programme.
Vous pouvez les modifier pour effectuer des tests.
*/

#include <stdio.h>

#define VALTAB {7,9,12,8,15}
#define TAILLE 5

int sommePaires(int tab[], int taille) {
/* hypothèse : le tableau contient des valeurs strictement positives */
  int somme = 0;
  for(int i = 0; i<taille; i++) if(tab[i]%2==0) somme += tab[i];
  return somme;
}

int main() {
  /* NE MODIFIEZ PAS L'INSTRUCTION SUIVANTE
  ELLE PERMET D'INITIALISER LE TABLEAU */
  int tab[] = VALTAB;

  /* Affichage */
  printf("La somme des valeurs paires est :  %d\n", sommePaires(tab, 5));

  printf("Le tableau ne contient pas de valeur paire\n");

  return 0;
}
