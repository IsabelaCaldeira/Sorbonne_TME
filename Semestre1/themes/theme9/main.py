# Exercice 9.5  Magasin en ligne
from typing import List, Dict, Set

#Exercice 9.5 Question 1
from typing import Dict, Set
Magasin : Dict[str, float] = {
    "Sabre Laser": 229.0,
    "Mitendo DX" :127.30,
    "Coussin Linux": 74.50,
    "Slip Goldorak": 29.90,
    "Station Nextpresso": 184.60}

#Exercice 9.5 Question 2
def prix_moyen(produits: Dict[str, float])->float:
    """Précondition : len(produits)>0
    retourne le prix moyen des produits disponibles
    """
    m : float = 0
    i : str
    for i in produits:
        m = m + produits[i]
    return m/len(produits)

assert prix_moyen(Magasin) == 129.06

#Exercice 9.5 Question 3
def fourchette_prix(mini:float, maxi:float, prix: Dict[str, float])-> Set[str]:
    """Préconditions : mini <= maxi
    retourne l'ensemble des noms de produits disponibles dans cette fourchette de prix
    """
    res : Set[str] = set()
    i : str
    for i in prix:
        if ((mini <= prix[i]) and (maxi >= prix[i])):
            res.add(i)
    return res

assert fourchette_prix(50.0,200.0,Magasin)=={'Coussin Linux', 'Mitendo DX', 'Station Nextpresso'}

#Exercice 9.5 Question 4
panier : Dict[str, float] = {"Sabre Laser": 3, "Coussin Linux": 2,"Slip Goldorak": 1}

#Exercice 9.5 Question 5
def tous_disponibles(Panier: Dict[str, float], Prix: Dict[str,float])-> bool:
    """retourne True si tous les produits demandés sont disponibles ou False sinon
    """
    comp : int = 0
    i : str
    for i in Panier:
        j : str
        for j in Prix:
            if i == j:
                comp = comp + 1
    return comp == len(Panier)
    
assert tous_disponibles(panier,Magasin) 

#Exercice 9.5 Question 6
def prix_achat(Panier: Dict[str, float], Prix: Dict[str, float])-> float:
    """retourne le prix total correspondant
    """
    res : float = 0
    i : str
    for i in Panier:
        j : str
        for j in Prix:
            if i == j:
                res = res + Prix[j]*Panier[i]
    return res

assert prix_achat(panier,Magasin) == 865.9

#Exercice 9.6 Traduction
Dict_Ang_Fra : Dict[str, str]
Dict_Ang_Fra = {'the': 'le', 'cat': 'chat',
                'fish': 'poisson', 'catches': 'attrape'}
Dict_Fra_Ita : Dict[str, str]
Dict_Fra_Ita = {'le': 'il', 'chat': 'gatto',
                'poisson': 'pesce', 'attrape': 'cattura'}

def traduction_mot_a_mot(l : List[str], dico : Dict[str,str]) -> List[str]:
    """retourne la liste des mots de l traduits à partir du dictionnaire
dico"""
    res : List[str] = []
    i : str 
    for i in l:
        res.append(dico[i])
    return res 

assert traduction_mot_a_mot(['the', 'cat', 'catches', 'the', 'fish'],Dict_Ang_Fra) ==['le', 'chat', 'attrape', 'le', 'poisson']
assert traduction_mot_a_mot(['le', 'chat', 'attrape', 'le', 'poisson'],Dict_Fra_Ita)==['il', 'gatto', 'cattura', 'il', 'pesce']

#Question 2
def dictionnaire_inverse(dico: Dict[str, str]) -> Dict[str,str]:
    """renvoie le dictionnaire inverse."""
    res : Dict[str,str] =dict()
    i : str
    for i in dico: 
        res[dico[i]] = i
    return res 

assert dictionnaire_inverse({"cat": "chat"}) == {'chat': 'cat'}
assert dictionnaire_inverse(Dict_Fra_Ita) == {'pesce': 'poisson', 'il': 'le', 'gatto': 'chat', 'cattura': 'attrape'}

#Question 3
def composition_dictionnaires(dico1: Dict[str,str], dico2:Dict[str,str]) -> Dict[str,str]:
    """Précondition: len(dico1)> 0 and len(dico2) > 0
    Renvoie le dictionnaire correspondant à la composition des traductions"""
    res: Dict[str,str] = {}
    i : str
    for i in dico1:
        j : str
        for j in dico2:
            if j==dico1[i]:
                res[i] = dico2[j]
    return res

assert composition_dictionnaires({"chat":"cat"}, {"cat":"gatto"}) == {'chat': 'gatto'}


#Exercice 9.7 Décomposition en facteurs premiers
#Exercice 9.7 Question 1
def valeur_decomposition(decomp:Dict[int,int])->int:
    """calcule le nombre correspondant à decomp
    """
    res : int = 1
    i : int
    for i in decomp:
        res = res * (i ** decomp[i])
    return res

assert valeur_decomposition({2:1, 3:1, 5:1}) == 30
assert valeur_decomposition({2:3, 7:1}) == 56

#Exercice 9.7 Question 2
def decomposition(lst:List[int])-> Dict[int,int]:
    """Précondition : len(lst)>0
    retourne le dictionnaire correspondant à la décomposition lst
    """
    res : Dict[int,int] = dict()
    i : int
    for i in lst:
        if i in res:
            res[i] = res[i] + 1
        else:
            res[i] = 1
    return res

assert decomposition([2, 3, 5]) == {2: 1, 3: 1, 5: 1}
assert decomposition([2, 2, 2, 7]) == {2: 3, 7: 1}

#Exercice 9.7 Question 3
def liste_nombres_premiers(n:int)->List[int]:
    """Précondition : n>=2
    renvoie la liste des nombres premiers inférieurs ou égaux à n
    """
    temp : List[int] = [i for i in range(2,n+1)]
    res : List[int] = []
    p : int = 0
    while len(temp)>0:
        p = temp[0]
        res.append(p)
        temp = [j for j in temp if j%p != 0]
    return res

assert liste_nombres_premiers(10) == [2, 3, 5, 7]
assert liste_nombres_premiers(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def liste_facteurs_premiers(n:int)-> List[int]:
    """Précondition : n>=2
    calcule la liste des facteurs premiers (avec répétition) de n
    """
    new_n : int = n
    L : List[int] = []
    prems : List[int] = liste_nombres_premiers(n)
    p : int
    for p in prems:
        while new_n % p == 0:
            L.append(p)
            new_n = new_n//p
    return L

assert liste_facteurs_premiers(30)==[2, 3, 5]
assert liste_facteurs_premiers(56)==[2, 2, 2, 7]
assert liste_facteurs_premiers(13)==[13]

#Exercice 9.7 Question 4
def decomposition_facteurs_premiers(n:int)->Dict[int,int]:
    """Précondition : n>=2
    renvoie le dictionnaire correspondant à la décomposition en facteurs premiers de n
    """
    res : List[int] = liste_facteurs_premiers(n)
    return decomposition(res)

assert decomposition_facteurs_premiers(1024) == {2: 10}
assert decomposition_facteurs_premiers(30) == {2: 1, 3: 1, 5: 1}
assert decomposition_facteurs_premiers(56) == {2: 3, 7: 1}
