from typing import List

#1 Partie Guidée : Polynômes
Polyn  = List[int]

ex1 : Polyn = [3, 0, 2]
ex2 : Polyn = [1, -1, 1, -1, 0]
ex3 : Polyn = [27]
ex4 : Polyn = []

#Question 1
def degre(P:Polyn)->int:
    """renvoie le degré d'un polynôme
    """
    deg : int = 0
    i : int
    for i in range(len(P)):
        if P[i]!=0:
            deg = deg + 1
            if i!= deg:
                deg = i
    return deg

assert degre(ex1) == 2
assert degre(ex2) == 3
assert degre(ex3) == 0
assert degre([0,0,0,0,0]) == 0

#Partie Guidee Polynome Question 2
def somme(P:Polyn,Q:Polyn)->Polyn:
    """renvoie la somme de deux polynômes passés en argarment
    """
    maxi : int = max(len(P),len(Q))
    s : Polyn = [0]*maxi
    i : int
    for i in range(maxi):
        if i<len(P):
            s[i] = s[i] + P[i]
        if i<len(Q):
            s[i] = s[i] + Q[i]
    return s

assert somme(ex1,ex1) == [6, 0, 4]
assert somme(ex1, ex4) == ex1
assert somme(ex1, ex2) == [4, -1, 3, -1, 0]

#Partie Guidee Polynome Question 3
def normalise(P:Polyn)->Polyn:
    """renvoie la forme normale d'un polynôme
    """
    res : Polyn = []
    i : int
    if degre(P)==0:
        return res
    else:
        for i in range(len(P)):
            if i<=degre(P):
                res.append(P[i])
    return res

assert normalise(ex1)==ex1
assert normalise(ex2)==[1,-1,1,-1]
assert normalise([0,0,0,0,0])==[]

#Partie Guidee Polynome Question 4
def produit(P1:Polyn,P2:Polyn)->Polyn:
    """renvoie le produit de deux polynômes
    """
    res : Polyn = [0] * (len(P1) + len(P2) - 1)
    for i in range(len(P1)):
        for j in range(len(P2)):
            res[i+j] = res[i+j] + P1[i] * P2[j]
    return res

assert normalise(produit(ex1,ex1)) == [9,0,12,0,4]
assert normalise(produit(ex1 , ex4 )) == []
assert normalise(produit(ex1 , ex1 )) == [9, 0, 12, 0, 4]
assert normalise(produit(ex1 , ex2 )) == [3, - 3, 5, - 5, 2, - 2]
assert normalise(produit(ex1 , ex3 )) == [27 * 3, 0, 27 * 2]
assert normalise(produit([1 , 1], [1, 0, 1])) == [1, 1, 1, 1]

#Suggestion 2 Autres opérations 
def multiplication(P:Polyn, n : int)-> Polyn:
    """renvoie le produit d'un polynôme par un scalaire
    """
    res : Polyn = [0] * len(P)
    i : int
    for i in range(len(P)):
        res[i] = n * P[i]        
    return res

assert multiplication(ex1, 3) == [9, 0, 6]
assert multiplication(ex1, 0) == [0, 0, 0]

def derivee(P:Polyn)-> Polyn:
    """Renvoie la derivee du polynome P  
    """
    res : Polyn = []
    i : int 
    for i in range(1, len(P)):
        res.append(i * P[i])
    return res

assert normalise(derivee(ex1)) == [0, 4]
assert normalise(derivee(ex4)) == []
assert normalise(derivee(ex2)) == [-1, 2,-3]

#Suggestion 3 Fonction Associee
def valeur(P: Polyn, x: float) -> int:
    """Renvoie la valeur de la fonction associée au polynôme calculée en x. """
    res : int = 0 
    i : int 
    for i in range(len(P)):
        res = res + P[i] * x ** i
        
    