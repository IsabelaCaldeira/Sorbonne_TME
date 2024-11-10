#Exercice 1.4 Question 1
from math import *
def aire_disque(r : float) -> float :
    """Précondition: r > 0
    Retourne l'aire d'un risque de rayon r
    """
    return 3.14*(r)**(2)

assert aire_disque(8.0) == 200.96

#Exercice 1.4 Question 2
def aire_couronne(r1: float, r2: float) -> float:
    """Précondition: r2 >= r1 >= 0
    Retourne l'aire de la couronne de rayon intérieur r1 et rayon extérieur r2
    """
    
    return aire_disque(r2) - aire_disque(r1)

assert aire_couronne(4,9) == 204.1
assert aire_couronne(3,17) == 879.2