#include <stdio.h>
#include "ex2.h"

/* programme de test */ 
int main() {
  char * chaine = "teste";
  caractere* listeCaracteres = NULL;
  listeCaracteres = ajouterCaractereTete('f', 3, listeCaracteres);
  afficherCaractere(listeCaracteres);
  listeCaracteres = ajouterCaractereTete('g', 9, listeCaracteres);
  afficherListe(listeCaracteres);
  printf("caractere : %c \n", maxFrequence(listeCaracteres));
  afficherCaractere(chercherCaractere('g', listeCaracteres));
  afficherListe(frequenceCaracteres(chaine));
  listeCaracteres = ajouterCaractereTete('h', 0, listeCaracteres);
  afficherListe(listeCaracteres);
  supprimeZero(listeCaracteres);
  return 0;
}