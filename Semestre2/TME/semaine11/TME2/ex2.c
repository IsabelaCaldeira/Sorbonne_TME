#include <stdio.h>
#include <stdlib.h>
#include "ex2.h"

/* Ajoute un nouveau caractère en tête de la liste listeCaracteres, le caractère et sa frequence sont passés en parametres.
   Renvoie la nouvelle tête de liste */
caractere* ajouterCaractereTete(char c, int freq, caractere* listeCaracteres){
  caractere* new = malloc(sizeof(caractere));
  new-> caract = c;
  new-> frequence = freq;
  new -> suivant = listeCaracteres;
  return new;
}

/* affiche les caractéristiques d'un caractère */
/* NE PAS MODIFIER LA FONCTION */
void afficherCaractere(caractere *c){
  printf("caractere : %c, frequence : %d\n",c->caract,c->frequence);
}

/* Affiche les caractéristiques de tous les éléments de la liste listeCaracteres */
void afficherListe(caractere* listeCaracteres) {
  caractere *courrant = listeCaracteres;
  while(courrant){
    afficherCaractere(courrant);
    courrant = courrant -> suivant;
  }
}

/* Renvoie le caractère qui a la fréquence la plus élevée.
   Si plusieurs caractères sont concernés, renvoie le dernier de la liste.
   Renvoie le caractère '0' si la liste est vide */
char maxFrequence(caractere *listeCaracteres) {
  if(!listeCaracteres) return '0';
  int freq = -1;
  char res = ' ';
  caractere *courrant = listeCaracteres;
  while(courrant){
    if(freq <= courrant->frequence){
      freq = courrant->frequence;
      res = courrant-> caract;
    }
    courrant = courrant -> suivant;
  }
  return res;
}

/* Renvoie le pointeur sur la première apparition du caractère passé en paramètre dans la liste listeCaracteres.
   Renvoie NULL si le caractère n'est pas dans la liste */
caractere* chercherCaractere(char c, caractere* listeCaracteres) {
  caractere *courrant = listeCaracteres;
  while(courrant){
    if(courrant->caract == c) return courrant;
    courrant = courrant-> suivant;
  }
  return NULL;
}

/* Crée et renvoie la liste associée à la chaîne de caractères passée en paramètre.
   Chaque élément de la liste doit correspondre à un caractère de la chaîne et à sa fréquence d'apparition dans la chaîne.
   Chaque caractère de la chaîne ne doit apparaître qu'une fois dans la liste */
caractere* frequenceCaracteres(char * chaine) {
  caractere* res = malloc(sizeof(caractere));
  res = NULL;
  
  for(int i = 0; chaine[i] != '\0'; i++){
    caractere * courrant = chercherCaractere(chaine[i], res);
    if(courrant) courrant->frequence++;
    else res = ajouterCaractereTete(chaine[i], 1, res);
  }
  return res;
}

/* Supprime de la liste listeCaracteres tous les caractères dont la fréquence est égale à zéro.
   Renvoie la tête de liste.
   La fonction doit libérer la mémoire.
   Si la chaîne passée en paramètre est vide, la fonction doit renvoyer NULL */
caractere *supprimeZero(caractere *listeCaracteres){
  /*Je n'ai pas compris l'erreur de segmentation
  mais ici vous pouvez trouver la logique que j'ai pensée meme si cela ne marche pas :(*/
  if(!listeCaracteres) return NULL;

  caractere *courrant = listeCaracteres, *temp = NULL, *pred = NULL;
  while(courrant){
    if(courrant->frequence == 0){
      if(!pred) listeCaracteres = listeCaracteres -> suivant;
      else pred -> suivant = courrant -> suivant;

      temp = courrant;
      courrant = courrant->suivant;
      free(temp);
    }else{
      pred -> suivant = courrant;
      courrant = courrant -> suivant;
    }
  }
  return listeCaracteres;
}
