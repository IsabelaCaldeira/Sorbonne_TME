from typing import List
#Exercice 6.7 Question 1 
def list_mult(L: List[int], k: int) -> List[int]:
    """Renvoie la liste obtenue en multipliant par k tout les elements de L"""
    new_L : List[int] = []
    for i in range(len(L)):
        new_L.append(L[i] * k)
    return new_L

#Exercice 6.7 Question 2
def liste_div(L: List[int], k : int) -> List[int]:
    """Pre  k != 0
    Renvoie la liste obtenue en divisant par k tout les elements de L
    """
    new_L : List[int] = []
    for i in range(len(L)):
        if L[i] % k == 0:
            new_L.append(L[i] / k)        
    return new_L

assert liste_div([2, 7, 9, 24, 6], 2) == [1, 12, 3]
assert liste_div([2, 7, 9, 24, 6], 3) == [3, 8, 2]

#Exercice 6.8 Question 1 
def entrelacement(L1 : List[int], L2 : List[int]) -> List[int]:
    """Pre len(L1) == len(L2)
    Renvoie la liste obtenue en alternant les elements de L1 et L2
    """
    new_L : List[int] = []
    i : int
    for i in range(len(L1)):
        new_L.append(L1[i])
        new_L.append(L2[i])
    return new_L

assert entrelacement([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6]


#Exercice 6.8 Question 2
def  entrelacement_general(L1: List[int], L2: List[int]) -> List[int]:
    """Renovie la liste obtenue en alternant les elements de L1 et L2 et si il reste des elements dans L1 ou L2, les ajoute à la fin de la liste
    """
    min_length : int = min(len(L1), len(L2))
    new_L : List[int] = entrelacement(L1[:min_length], L2[:min_length])
    i : int
    j : int 
    if len(L1) > len(L2):
        for i in range(len(L2), len(L1)):
            new_L.append(L1[i])
    
    elif len(L2) > len(L1):
        for j in range(len(L1), len(L2)):
            new_L.append(L2[j])        
    
    return new_L
    
assert entrelacement_general([1, 2, 3], [4, 5, 6, 7, 8]) == [1, 4, 2, 5, 3, 6, 7, 8]
assert entrelacement_general([1, 2, 3, 4, 5], [6, 7, 8]) == [1, 6, 2, 7, 3, 8, 4, 5]

#Exercice 6.9 Question 1 
def jonction(l : List[str], c: str) -> str:
    """Pre len(c) = 1
    Retourn la chaine de caractere obtenue en joignant les elements de l par le caractere c
    """
    s : str = ""
    i : int 
    for i in range(len(l)):
        if i != len(l) - 1:
            s = s + l[i] + c
        else:
            s = s + l[i]
    return s

assert jonction(['un', 'deux', 'trois', 'quatre'], '.') == 'un.deux.trois.quatre'
assert jonction(['les', 'mots', 'de', 'cette', 'phrase'], ' ') == 'les mots de cette phrase'

#Exercice 6.9 Question 2 
def separation(s: str, c: str) -> List[str]:
    """Précondition : len(c) = 1
    retourne la liste de chaînes composées des sous-chaînes
    de s séparées par le caractère séparateur c.
    Le séparateur c n'est pas présent dans la chaîne résultat."""
    L : List[str] = []
    s2 : str = ""
    i : int
    for i in range(len(s)):
        if s[i] != c:
            s2 = s2 + s[i]
        else:
            L.append(s2)
            s2 = ""
    L.append(s2)
    return L

assert separation("un.deux.trois.quatre", ".") == ['un', 'deux', 'trois', 'quatre']
assert separation('les mots de cette phrase', ' ') == ['les', 'mots', 'de', 'cette', 'phrase']
