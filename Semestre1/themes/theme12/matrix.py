from typing import List, Set, T 
#Exercice 12.1 Question 1 
def censurer(l: List[str], mots : Set[str]) -> None:
    """Renvoie ***CENSURE*** a chaque mots trouvee
    """
    i : int 
    for i in  range(len(l)):
        if l[i] in mots:
            l[i] = "***CENSURE***"
            
t0 : List[str] = ["le", "loup", "est", "un",
                "loup", "pour", "l'", "homme"]
assert censurer(t0, {"loup"}) == None
assert t0 == ['le', '***CENSURE***', 'est', 'un',
'***CENSURE***', 'pour', "l'", 'homme']

#Exercice 12.1 Question 2
def decaler(l : List[T], k : int) -> None:
    """ Decale l k fois vers la droite
    """
    
    i : int 
    for i in range(k%len(l)):
        temp : T = l[-1]
        j : int
        for j in range(len(l)-1,0,-1):
            l[j] = l[j-1]
        l[0] = temp
        
l1 : List[int] = [1, 2, 3, 4, 5, 6]
assert decaler(l1, 2) == None
assert l1 == [5, 6, 1, 2, 3, 4]

#Exercice 12.4 Question 1
def trier_bulles(L:List[T])->None:
    """Précondition : L!=[]
    Trie une liste selon la méthode du tri à bulle
    """
    temp : T
    i : int
    for i in range(len(L)-1):
        j : int
        for j in range(len(L)-(i+1)):
            if L[j]>L[j+1]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
            

l0 : List[int] = [6, 1, 3, 2, 4, 5]
assert trier_bulles(l0) == None
assert l0 == [1, 2, 3, 4, 5, 6]

#Exercice 12.4 Question 2 
def trier_bulles_optim(L:List[T])->None:
    """Précondition : L!=[]
    Trie une liste selon la méthode du tri à bulle
    """
    temp : T
    i : int
    for i in range(len(L)-1):
        j : int
        e : bool = True
        for j in range(len(L)-(i+1)):
            if L[j]>L[j+1]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
                e = False
        if e == True:
            return None

l3 : List[int] = [6, 1, 3, 2, 4, 5]
assert trier_bulles_optim(l3) == None
assert l3 == [1, 2, 3, 4, 5, 6]

#Exercice 12.5 Question 1 
def partitionner(l : List[T]) -> int:
    """Renvoie l'indice du pivot une fois le partitionnement effectue"""
    
    
    
new_l = [2, 1, 4, 0, 3]
print(partitionner(new_l))
print(new_l)
    
