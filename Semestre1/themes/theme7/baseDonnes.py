# TME6 Caldeira Ribeiro Cruz Isabela 21307818
from typing import List
from typing import Tuple 

#Exercice 7.6 Question 1
Etudiant = Tuple[str, str, int, List[int]]
BaseUPMC = List[Etudiant]
BaseUPMC = [('GARGA', 'Amel', 20231343, [12, 8, 11, 17, 9]),
        ('POLO', 'Marcello', 20342241, [9, 11, 19, 3]),
        ('AMANGEAI', 'Hildegard', 20244229, [15, 11, 7, 14, 12]),
        ('DENT', 'Arthur', 42424242, [8, 4, 9, 4, 12, 5]),
        ('ALEZE', 'Blaise', 30012024, [17, 15, 20, 14, 18, 16, 20]),
        ('D2', 'R2', 10100101, [10, 10, 10, 10, 10, 10])]

def note_moyenne(note : List[int]) -> float:
    """Pre les valeurs de i ou [] ou entre 0 a 20
    Renvoie la moyenne de la liste"""
    if len(note) == 0:
        return 0.0
    
    i: int
    compteur : float 
    for i in range(len(note)):
        compteur = compteur + note[i]
    return compteur/len(note)

assert note_moyenne([12, 8, 14, 6, 5, 15]) == 10.0
assert note_moyenne([]) == 0.0

def moyenne_generale(base : List[Etudiant]) -> float:
    """Renvoie la moyenne de la moyenne des notes des etudiants"""
    if len(base) == 0:
        return 0.0

    compteur : float = 0.0
    for (Nom, prenom, num, notes) in base:
        compteur = compteur + note_moyenne(notes)

    return compteur/len(base)

assert moyenne_generale(BaseUPMC) == 11.307142857142857
assert moyenne_generale([]) == 0.0

#Exercice 7.6 Question 3
def top_etudiant(bd : List[Etudiant]) -> Tuple[str, str]:
    """Précondition : len(bd) > 0
    retourne un étudiant de la base bd avec la meilleure
    moyenne. Si des étudiants sont ex-aequo alors on
    retourne le premier dans l'ordre séquentiel de la liste."""
    res : Tuple[str, str] = ("", "")
    compteur : float = 0.0
    for (Nom, prenom,num, notes) in bd:
        if note_moyenne(notes) > compteur:
            compteur = note_moyenne(notes)
            res = (Nom, prenom)

    return res

assert top_etudiant(BaseUPMC) == ('ALEZE', 'Blaise')

#Exercice 7.6 Question 4
def recherche_moyenne(rnum : int, bd : List[Etudiant]) -> Optional[float]:
    """Pre rnum > 0, len(bd) > 0
    Renvoie la moyenne de l'etudiant correspond ou None si ce numero d'etudiant est inconnu"""
    for (Nom, prenom, num, notes) in bd:
        if rnum == num:
            return note_moyenne(notes)
        
    return None

assert recherche_moyenne(20244229, BaseUPMC) == 11.8
assert recherche_moyenne(20342241, BaseUPMC) == 10.5

#Exercice 7.7 Question 
def intersection_2_listes(l1 : List[int], l2 : List[int]) -> List[int]:
    """Pre l1 et l2 triees en ordre croissant
    Renvoie la liste des elements appartenant a l1 et a l2"""
    new_l : List[int]= []
    i : int = 0
    j : int = 0 
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            i = i +  1
        elif l1[i] > l2[j]:
            j = j +  1
        else:
            new_l.append(l1[i])
            i = i + 1
            j = j + 1

#Exercice 7.8
CarreMagique : List[List[int]]
CarreMagique = [ [2, 7, 6],
                [9, 5, 1],
                [4, 3, 8] ]

#Exercice 7.8 Question 1
def presence(n : int, l: List[int]) -> bool:
    """renvoie True si n est present sinon False"""
    i : int
    if len(l) == 0:
        return False
    for i in range(len(l)):
        if l[i] == n:
            return True
    return False

assert presence(5, [9,5,1]) == True
assert presence(4, [9,5,1]) == False

#Exercice 7.8 Question 2
def mat_presence(n: int, l1: List[List[int]]) -> bool:
    """Retourne True si l’entier n est présent dans la liste ll ou False sinon"""
    i : List[int]
    for i in l1:
        if presence(n, i):
            return True
    return False

assert mat_presence(5, [[1, 2, 3], [4, 5, 6]]) == True    
assert mat_presence(7, [ [1,2, 3], [4, 5, 6] ]) == False
assert mat_presence(7, CarreMagique) == True

#Exercice 7.8 Question 3
def verif_elems(n : int, l1 : List[List[int]]) -> bool:
    """Pre n > 0
    retourne True si tous les entiers dans l’intervalle [1; n × n] sont
présents dans la liste ll, ou False sinon."""

    new_l : List[int] = [1]
    i : int = 2
    while i <= n * n:
        new_l.append(i)
        i = i + 1
    j : int
    for j in new_l:
        if not (mat_presence(j,l1)):
            return False
    return True 

assert verif_elems(3, CarreMagique) == True
assert verif_elems(3, [ [2, 7, 6], [8, 5, 1], [4, 3, 8] ]) == False

def verif_elems_comp(n : int, l1 : List[List[int]]) -> bool:
    new_l : List[int] = [i for i in range(1, n*n + 1)]
    j : int 
    for j in new_l:
        if not (mat_presence(j,l1)):
            return False
    return True

def optim_verif_elem(n: int, l1: List[List[int]]) -> bool:
    zMat = [i for i in range(0, n*n)]
    for ligne in l1:
        for col in ligne:
            zMat[col-1] = 11
    for z in zMat:
        if z == 0:
            return False
    return True 
    

#Exercice 7.8 Question 4
def somme_liste(l :List[int]) -> int:
    """pre len(l) > 0
    Renvoie la somme des elements de l"""
    i : int
    res : int = 0
    for i in range(len(l)):
        res = res + l[i]
    return res

assert somme_liste([2, 7, 6]) == 15
assert somme_liste([9, 5, 1]) == 15

#Exercice 7.8 Question 5
def verif_ligne(l1: List[List[int]], s: int) -> bool:
    """Renvoie true si toutes les sous listes de l1 possedent la meme somme s ou false sinon"""
    i : List[int]
    for i in l1:
        if not (somme_liste(i) == s):
            return False
    return True

assert verif_ligne(CarreMagique, 15) == True
assert verif_ligne(CarreMagique, 16) == False

#Exercice 7.8 Question 6
def colonne(j : int, mat : List[List[int]]) -> List[int]:
    """Pre   0 < j  < n
    Renvoie la j'ieme collonne de mat"""
    i : List[int]
    new_l : List[int] = []
    for i in mat:
        new_l.append(i[j])
    return new_l

assert colonne(0, [ [2, 7, 6],
                [9, 5, 1],
                [4, 3, 8] ]) == [2, 9, 4]

def colonne_comp(j : int, mat: List[List[int]]) -> List[int]:
    return [liste[j] for liste in mat]

#Bonus 
def ligne(i : int, mat: List[List[int]]) -> List[int]:
    return mat[i]

#Pour comprendre les listes compréhensives
def ligne_comp(i : int, mat: List[List[int]]) -> List[int]:
    return [mat[j] for j in range(len(mat)) if j == i]

#Exercice 7.8 Question 8
def diagonale_1(mat : List[List[int]]) -> List[int]:
    """Renvoie la diagonale de une matrice de n dimensions"""
    new_l : List[int] = []
    i : int
    for i in range(len(mat)):
        new_l.append(mat[i][i])

    return new_l

assert diagonale_1([ [2, 7, 6],
                    [9, 5, 1],
                    [4, 3, 8] ]) ==[2, 5, 8]

def diagonale_2(mat : List[List[int]]) -> List[int]:
    """Renvoie la diagonale de une matrice de n dimensions"""
    new_l : List[int] = []
    i : int 
    for i in range(len(mat)):
        new_l.append(mat[i][len(mat) - 1 - i])
    return new_l

    
assert diagonale_2([ [2, 7, 6],
                    [9, 5, 1],
                    [4, 3, 8] ]) == [6, 5, 4]




    
