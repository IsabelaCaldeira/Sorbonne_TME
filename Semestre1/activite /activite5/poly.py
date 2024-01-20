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
            if i!=deg:
                deg = i
    return deg

assert degre(ex1) == 2
assert degre(ex2) == 3
assert degre(ex3) == 0
assert degre([0,0,0,0,0]) == 0

#Question 2
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

#Question 3
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

#Question 4
def produit(P1:Polyn,P2:Polyn)->Polyn:
    """renvoie le produit de deux polynômes
    """
    temp : Polyn = []
    res : Polyn = []
    i : int
    j : int
    k : int
    for i in range(len(P1)):
        for j in range(len(P2)):
            if P1[i]!=0:
                temp.append(P1[i]*P2[j])
    for k in range(len(temp)):
        if degre([temp[k]])==degre([temp[k+1]]):
            temp[k]=temp[k]+temp[k+1]
        res.append(temp[k])
    return res

assert normalise(produit(ex1,ex1))==[9,0,12,0,4]

