import studentlib.gfx as gfx
from typing import Image

#Exercice 2.7 Question 1 
#x et y : coordonnées du coin inférieur gauche de la base de la tour.
#largeur_base : la largeur de la base de la tour.
#largeur_etage : la largeur de l'étage supérieur.
#hauteur_etage : la hauteur de chaque étage (identique pour les deux étages).

#Exercice 2.7 Question 2
def rectangle(x: float, y : float, l: float, h: float) -> Image:
    """Renvoie une image representant un rectangle plein de longueur l et de hauteur h dont le coin en haut a gauche est en x, y
    """
    triangle1 = gfx.fill_triangle(x, y, x + l, y, x, y + h)
    triangle2 = gfx.fill_triangle(x + l, y, x, y + h, x + l, y + h)
    return gfx.overlay(triangle1, triangle2)

#Les parametres necessaires, sont x, y, l et h qui sont les coordonnees du coin en haut a gauche du rectangle, la longueur et la hauteur du rectangle

