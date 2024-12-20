#Exercice 3.4 Question 1 
def reste(a: int, b: int) -> int:
    """Précondition a > 0 et b > 0 
    Renvoie le reste de la division euclidienne de a par b
    """
    c: int = a
    
    while c > b:
        c = c - b
    
    return c 

assert reste(3, 2) == 1
assert reste(21, 7) == 0

#Exercice 3.4 Question 2 
def est_divisible_par(a: int, b: int) -> bool:
    """Précondition a >= 0, b >= 0
    Donne la divisibilité de le nombre 
    """
    return reste(a, b) == 0
    
assert est_divisible_par(2,4) == False
assert est_divisible_par(4,2) == True

#Exercice 3.4 Question 3 
def ppcm(a: int, b: int) -> int:
    """Précondition: a>0, b>0
    Renvoie le plus petit entier naturel non nul qui est un multiple commun à a et b."""
    c: int = 1
    while not(est_divisible_par(c, a) and est_divisible_par(c, b)):
        c = c + 1
    return c

assert ppcm(3, 2) == 6
    
    

