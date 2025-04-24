/* Nous nous interessons a des listes de scores de matchs, chaque match est caracterise par l'identifiant entier des deux equipes (l'equipe1 est celle qui joue a domicile), et le score de chaque equipe */

typedef struct _match match;

typedef struct _match {
  int equipe1;
  int equipe2;
  int scoreEquipe1;
  int scoreEquipe2;
  match* suivant;
} match;

/* Ajoute un nouveau match (dont les caracteristiques sont passees en parametre) en tete de liste.
Retourne la nouvelle tete de liste */
match *ajouterMatchTete(int eq1, int eq2, int score1, int score2, match *listeMatchs);

/* Affiche les caracteristiques d'un match */
void afficherMatch(match *m);

/* Affiche les caracteristiques de tous les matchs de la liste listeMatchs */
void afficherListe(match *listeMatchs);

/* Retourne un pointeur sur le match avec la plus grosse difference de score. Si la plus grosse difference de score est la mmeme pour plusieurs matchs, la fonction retourne un pointeur sur le dernier rencontre.
Retourne NULL si tous les matchs ont un score nul */
match *maximumDifference(match *listeMatchs);

/* Retourne un pointeur sur le premier match de la liste remporte a domicile par l'equipe passee en parametre (l'equipe1 est l'equipe qui joue a dimicile). 
Retourne NULL si l'equipe n'a remporte aucun match a domicile ou n'a participe a aucun match)*/
match *matchGagne(int equipe, match *listeMatchs);
  
/* Supprime de la liste tous les matchs concernant l'equipe passee en parametre, retourne la tete de liste apres suppression. La fonction doit liberer la memoire */
match *disqualifierEquipe(int equipe, match *listeMatchs);

/* Cree et retourne la tete de la liste comprenant une copie de tous les matchs remportes a l'exterieur.
Retourne NULL si aucun match n'a ete remporte a l'exterieur */
match *victoireExterieur(match *listeMatchs);