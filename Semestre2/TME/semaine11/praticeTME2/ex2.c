#include <stdio.h>
#include <stdlib.h>
#include "ex2.h"

/* Ajoute un nouveau match (dont les caracteristiques sont passees en parametre) en tete de liste.
Retourne la nouvelle tete de liste */
match *ajouterMatchTete(int eq1, int eq2, int score1, int score2, match *listeMatchs) {
    match *new_match = malloc(sizeof(match));
    new_match -> equipe1 = eq1;
    new_match -> equipe2 = eq2;
    new_match -> scoreEquipe1 = score1;
    new_match -> scoreEquipe2 = score2;
    new_match -> suivant = listeMatchs;
    return new_match;
}

/* Affiche les caracteristiques d'un match */
/* NE PAS MODIFIER CETTE FONCTION */
void afficherMatch(match *m) {
  printf("Equipe1 : %d, Equipe2 : %d, Score1 : %d, Score2 : %d\n",m->equipe1, m->equipe2,m->scoreEquipe1, m->scoreEquipe2);  
}

/* Affiche les caracteristiques de tous les matchs de la liste listeMatchs */
void afficherListe(match *listeMatchs){
    match *current = listeMatchs;
    while(current){
        afficherMatch(current);
        current = current -> suivant;
    }
}

/* Retourne un pointeur sur le match avec la plus grosse difference de score. Si la plus grosse difference de score est la mmeme pour plusieurs matchs, la fonction retourne un pointeur sur le premier rencontre.
Retourne NULL si tous les matchs ont un score nul */
match *maximumDifference(match *listeMatchs) {
    match *current = listeMatchs;
    match *res = NULL;
    int differenceScore = -1;

    while(current){
        int scoreCurrent = abs(current -> scoreEquipe1 - current -> scoreEquipe2);
        if(scoreCurrent > differenceScore){
            differenceScore = scoreCurrent;
            res = current;
        }
        current = current -> suivant;
    }
    if(differenceScore == 0) return NULL;
    return res;
}

/* Retourne un pointeur sur le premier match de la liste remporte a domicile par l'equipe passee en parametre (l'equipe1 est l'equipe qui joue a dimicile). 
Retourne NULL si l'equipe n'a remporte aucun match a domicile ou n'a participe a aucun match)*/
match *matchGagne(int equipe, match *listeMatchs) {
    match *current = listeMatchs;
    while(current){
        if(equipe == current -> equipe1){
            if(current -> scoreEquipe1 > current -> scoreEquipe2) return current;
        }
        current = current -> suivant;
    }
    return NULL;
}

/* Supprime de la liste tous les matchs concernant l'equipe passee en parametre, retourne la tete de liste apres suppression. La fonction doit liberer la memoire */
match *disqualifierEquipe(int equipe, match *listeMatchs) {
    match *current = listeMatchs, *temp = NULL, *pred = NULL;
    while(current){
        if(current -> equipe1 == equipe || current -> equipe2 == equipe){
            if(!pred) listeMatchs = listeMatchs -> suivant;
            else pred -> suivant = current -> suivant;

            temp = current;
            current = current -> suivant;
            free(temp);
        }
        else{
            pred = current;
            current = current -> suivant;
        }
    }
    return listeMatchs;
}

/* Cree et retourne la tete de la liste comprenant une copie de tous les matchs remportes a l'exterieur.
Retourne NULL si aucun match n'a ete remporte a l'exterieur */
match *victoireExterieur(match *listeMatchs){
    match *new_match = NULL;
    match *current = listeMatchs;
    while(current){
        if(current -> scoreEquipe2 > current -> scoreEquipe1){
            new_match = ajouterMatchTete(current -> equipe1, current -> equipe2, current -> scoreEquipe1, current -> scoreEquipe2, new_match);
        }
        current = current -> suivant;
    }
    return new_match;
}

int main(){
    int eq1 = 1, eq2 = 2, score1 = 7, score2 = 3;
    match * listeMatch = NULL;
    listeMatch = ajouterMatchTete(eq1, eq2, score1, score2, listeMatch);
    listeMatch = ajouterMatchTete(2, 3, score1, 37, listeMatch);

    afficherListe(listeMatch);
    afficherMatch(maximumDifference(listeMatch));
    afficherMatch(disqualifierEquipe(3, listeMatch));
    afficherMatch(victoireExterieur(listeMatch));
    return 0;
}