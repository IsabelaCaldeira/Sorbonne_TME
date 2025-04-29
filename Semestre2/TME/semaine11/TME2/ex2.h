/* Dans cet exercice, nous considérons une liste permettant de stocker des caractères et leur fréquence */

typedef struct _caractere caractere;

typedef struct _caractere{
  char caract;
  int frequence;
  caractere * suivant;
} caractere;

/* Ajoute un nouveau caractère en tête de la liste listeCaracteres, le caractère et sa fréquence sont passés en paramètres.
Renvoie la nouvelle tête de liste */
caractere *ajouterCaractereTete(char c, int freq, caractere *listeCaracteres);

/* affiche les caractéristiques d'un caractère */
/* NE PAS MODIFIER LA FONCTION */
void afficherCaractere(caractere *c);

/* Affiche les caractéristiques de tous les éléments de la liste listeCaracteres */
void afficherListe(caractere *listeCaracteres);

/* Renvoie le caractère qui a la fréquence la plus élevée, si plusieurs caractères sont concernés, renvoie le dernier de la liste.
   Renvoie le caractère '0' si la liste est vide */
char maxFrequence(caractere *listeCaracteres);

/* Renvoie le pointeur sur la première apparition du caractère passé en paramètre dans la liste listeCaracteres.
   Renvoie NULL si le caractère n'est pas dans la liste */
caractere *chercherCaractere(char c, caractere *listeCaracteres);

/* Crée et renvoie la liste associée à la chaîne de caractères passée en paramètre.
   Chaque élément de la liste doit correspondre à un caractère de la chaîne et à sa frequence d'apparition dans la chaîne.
   Chaque caractère de la chaîne ne doit apparaître qu'une fois dans la liste */
caractere *frequenceCaracteres(char * chaine);

/* Supprime de la liste listeCaracteres tous les caractères dont la fréquence est égale à zéro.
   Renvoie la tête de liste.
   La fonction doit libérer la mémoire.
   Si la chaîne passée en paramètre est vide, la fonction doit renvoyer NULL */
caractere *supprimeZero(caractere *listeCaracteres);
