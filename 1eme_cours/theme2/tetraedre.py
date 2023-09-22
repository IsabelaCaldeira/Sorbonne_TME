from math import * 
#Exercice 2.5 Question 1 
def volume_tetraedre(a: float, b: float, c: float, d: float, e: float, f: float) -> float:
    """Précondition a > 0, b > 0, c > 0, d > 0, e > 0, f > 0
    Retourne: le volume d'un tétraèdre  
    """
    x = a**2 + b**2 - d**2
    y = b**2 + c**2 - e**2
    z = a**2 + c**2 - f**2
    p = 4 * (a**2) * (b**2) * (c ** 2)
    q = (a**2) * (y**2) + (b**2)*(z**2) + (c**2) * (x**2)
    r = x * y *z
    
    return 1/12 * sqrt(p - q + r)

assert volume_tetraedre(1, 1, 1, 1, 1, 1) == 0.11785113019775792
assert volume_tetraedre(2, 2, 2, 2, 2, 2) == 0.9428090415820634

#Exercice 2.5 Question 2 
def volume_tetraedre_regulier(longeur: float) -> float:
    """Précondition longeur > 0
    Retourne le volume d'un téatrèdre régulier
    """
    return volume_tetraedre(longeur, longeur, longeur, longeur, longeur, longeur)

assert volume_tetraedre_regulier(1) == 0.11785113019775792
assert volume_tetraedre_regulier(2) == 0.9428090415820634
