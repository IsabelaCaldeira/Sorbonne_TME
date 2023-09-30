import math 
#Exercice 1 Question 1 
def terme_leibniz(n : int) -> float:
    """Préconditions: n>=0 
    Renvoie le terme d'indice n de la somme
    """
    somme : float = 0
    i : int
    for i in range (n):
        somme = somme + ((-1)**i/2*n +1) - math.pi/4
         
        
    return somme 

print (terme_leibniz(0))
assert terme_leibniz(0) == 1