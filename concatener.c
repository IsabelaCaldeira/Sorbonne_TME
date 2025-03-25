#include <stdlib.h>
#include "cellule.h" // Assurez-vous que ce fichier contient la définition de cellule_t

cellule_t* concatener(cellule_t* liste1, cellule_t* liste2) {
    if (!liste1) {
        // Si liste1 est vide, renvoyer liste2
        return liste2;
    }
    if (!liste2) {
        // Si liste2 est vide, renvoyer liste1
        return liste1;
    }

    // Parcourir liste1 jusqu'au dernier élément
    cellule_t* courant = liste1;
    while (courant->suivant != NULL) {
        courant = courant->suivant;
    }

    // Chaîner le premier élément de liste2 au dernier élément de liste1
    courant->suivant = liste2;

    // Retourner la tête de liste1
    return liste1;
}
