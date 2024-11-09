import typing
#Exercice 4.5 Question 1 
def nb_couples_intervalle(n: int, p : int) -> int:
    """ n <= p
    Renvoie le nombre de couples (i,j) d'etneries appartenant à l'intervalle [n,p]"""
    if n == p:
        return 0    
    else:
        i : int = 0; j : int = 0
        count = 0
        for i in range(n, p + 1):
            for j in range(i+ 1, p + 1):
                if i < j:
                    count = count + 1 
    return count
assert nb_couples_intervalle(0,0) == 0
assert nb_couples_intervalle(2,4) == 3
assert nb_couples_intervalle(-1,3) == 10

#Exercice 4.5 Question 2 
def nb_couples_divise(n: int, p : int) -> int:
    """Pre n<=p
    Renvoie la somme des nombre de couples d'entiers disctincts appartenant à [n,p] tels que i divise j"""
    if n == p:
        return 0    
    else:
        count = 0 
        i : int = 0; j : int = 0
        for i in range(n, p + 1):
            for j in range(n, p + 1):
                if i != 0 and i != j and j % i == 0 and i > 0:
                    count = count + 1 
        return count
    
assert nb_couples_divise(4, 6) == 0
assert nb_couples_divise(2, 6) == 3
assert nb_couples_divise(-1, 1) == 2
assert nb_couples_divise(1, 10) == 17
    
#Exercice 4.5 Question 3
def nb_couples_divise_trace(n: int, p: int) -> int:
    """Renvoie la somme des nombre de couples d'entiers distincts appartenant à [n,p] tels que i divise j et trace l'exécution"""
    count = 0
    for i in range(n, p + 1):
        for j in range(i + 1, p + 1):
            print(f"couple ( {i} , {j} )")
            if j % i == 0:
                print("------------")
                print(f"{i} divise {j} !")
                print("------------")
                count = count + 1
    print(count)
    return count

assert nb_couples_divise_trace(2,6) == 3

#Exercice 4.5 Question 4 et 5 
def existe_couples_divise_rapide(n: int, p: int) -> bool:
    """Précondition : n <= p
    Renvoie True s'il existe un couple (i,j) d'entiers appartenant
    à l'intervalle [n,p] tels que i != j et i divise j,
    ou False sinon.
    """
    for i in range(n, p + 1):
        for j in range(i + 1, p + 1):
            if j % i == 0:
                return True
    return False

assert existe_couples_divise_rapide(0, 0) == False
assert existe_couples_divise_rapide(2, 6) == True
assert existe_couples_divise_rapide(-1, 1) == True
assert existe_couples_divise_rapide(1, 10) == True
assert existe_couples_divise_rapide(21, 34) == False


