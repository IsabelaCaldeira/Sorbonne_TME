#Exercice 4.4 Question 1
def somme_cubes(n : int) -> int:
    """
        Précondition n >=0 
        Renvoie la somme de cubes
    """
    # La somme c'est la variable que va prends le valeur de la somme de cubes 
    
    somme : int = 0
    k : int = 1
    
    while k <= n :
        somme = somme + (k ** 3)
        k = k + 1
        
    return somme

assert somme_cubes(0) == 0
assert somme_cubes(1) == 1
assert somme_cubes(2) == 9 
assert somme_cubes(3) == 36
assert somme_cubes(4) == 100

#Exercice 4.4 Question 2 
assert somme_cubes(4) == 0+1**3+2**3+3**3+4**3 




