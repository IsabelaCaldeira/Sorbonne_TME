#Exercice 3.1 
def somme_impairs_inf(n : int) -> int :
    """ Précondition n >= 0
    Renvoie la somme des entiers impairs <= n
    """
    somme : int = 0
    i : int = 0
    
    while i <= n :
        somme = somme + i
        i = i + 2

    return somme        