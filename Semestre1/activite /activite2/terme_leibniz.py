import random
import math 
#Exercice 1 Question 1 
def terme_leibniz(n : int) -> float:
    """Préconditions: n>=0 
    Renvoie le terme d'indice n de la somme
    """
        
    return ((-1)**n)/(2*n +1)

assert terme_leibniz(0) == 1
assert terme_leibniz(1) == -1/3

#Exercice 1 Question 2
def somme_leibniz(n: int) -> float:
    """Précondition: n>=0
    Renvoie la somme des n premiers termes
    """
    i : int = 0
    somme : float = 0

    while i <= n:
        somme = somme + terme_leibniz(i)
        i = i + 1

    return somme

assert somme_leibniz(1) == 1-1/3
assert somme_leibniz(0) == 1

#Exercice 1 Question 3 
def approx_leibniz(n:int) -> float:
    """Précondition: n>= 0
    Calcule une approximation de pi  avec la somme des n premiers termes"""
    return somme_leibniz(n) * 4


assert approx_leibniz(10) == 3.232315809405594
assert approx_leibniz(100) == 3.1514934010709914

#Exercice 1 Question 4

assert abs(approx_leibniz(10)-3.232315) < 10**6 
assert abs(approx_leibniz(100)-3.1514934) < 10**7

#Exercice 4 Suggestion Aléatoire
def approx_aleatoire(N: int) -> float:
    """Précondition:
    Calcule une approximation de pi
    """
    a : int = 0
    i : int
    for i in range(N+1):
        x : float = random.random()
        y : float = random.random()
        if math.sqrt(((1/2) - x) ** 2 + ((1/2)-y)**2)<= (1/2):
            a = a + 1

    return (a/N)*4
    
assert 2.5 < approx_aleatoire(50) < 3.5
assert 2.5 < approx_aleatoire(1000) < 3.5