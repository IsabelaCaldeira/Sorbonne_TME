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
trier_bulles(l0)

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

l0 : List[int] = [6, 1, 3, 2, 4, 5]
trier_bulles_optim(l0)

#Exercice 12.5 Question 1
def partitionner(L:List[int],n:int)->None:
    """Tri L en fonction du pivot
    """
    temp : int
    i : int
    for i in range(len(L)):
        if i < n:
            temp =
            L