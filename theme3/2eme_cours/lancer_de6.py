import math 
import random

#Exercice 3.8 Question 1 
def lancer_de6() -> int:
    """ Retourne un nombre entre 1 et 6 """
    return math.floor(random.random()*6+1)
    
assert 1 <= lancer_de6() <= 6

#Exercice 3.8 Question 2 
def lancer_de6_2() -> int:
    """Retourne un nombre entre 1 et 6
    """
    random.seed(42)
    return math.floor(random.random()*6+1)

assert lancer_de6_2() == 4

#Exercice 3.8 Question 3
def moyenne_plusieurs_lancers(n: int) -> float :
    """Précondition: n >= 1
    Renvoie la moyenne 
    """
    somme_moyenne: float = 0 
    k : int = 1
    while k <= n:
        k = k + lancer_de6_2()
        somme_moyenne = k
        k = k + 1
        
    return somme_moyenne/n

assert moyenne_plusieurs_lancers(5) == 1
assert moyenne_plusieurs_lancers(3) == 1.6666666666666667

#Exercice 3.8 Question 4 
def frequence_valeur(r: int, n: int) -> float:
    """Précondition 0<r>=6, n > 0
    retourne la fréquence d’apparition de la valeur r lors de n lancers
    """
    frequence : float = 0
    k : int 
    for k in range(1, n-1):
        if lancer_de6() == r:
            frequence = frequence + 1
        
    return frequence/n 
    
assert frequence_valeur(1, 1) == 0
assert frequence_valeur(1, 10) == 0.2

#Exercice 3.8 Question 5 
def lancer_de_n(n: int) -> int:
    """Précondition n> 0 
    Renvoie à chaque appel une valeur entière comprise entre 1 et n.
    """
    return math.floor(random.random()*n+1)

assert 1 <= lancer_de_n(20) <= 20
assert 1 <= lancer_de_n(30) <= 30

