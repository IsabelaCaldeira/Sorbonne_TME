from typing import Set, List, T, Dict

#Exercice 10.3 : Revisiter le theme 9
def diff_sym(ens1 : Set[T], ens2 : Set[T]) -> Set[T]:
    """Utilise une comprehension d'ensemble pour retourner la difference symetrique entre deux ensembles ens1 et ens2"""
    return {e1 for e1 in ens1 if e1 not in ens2}|{e2 for e2 in ens2 if e2 not in ens1}

assert diff_sym({2, 5, 9}, {3, 5, 8}) == {2, 3, 8, 9}
assert diff_sym({2, 5, 9}, {2, 5, 8, 9}) == {8}
#Question 2
#Exercice 10.3  Question 3 
Recette = Dict[str,Set[str]]
Dessert : Recette = {'gateau chocolat' : {'chocolat', 'oeuf', 'farine', 'sucre', 'beurre'},'gateau yaourt' : {'yaourt', 'oeuf', 'farine', 'sucre'},'crepes' : {'oeuf', 'farine', 'lait'},'quatre-quarts' : {'oeuf', 'farine', 'beurre', 'sucre'},'kouign amann' : {'farine', 'beurre', 'sucre'}}

#(9.3 Question 2 )
def recette_avec(des : Recette, i : str) -> Set[T]:
    """Renvoie l'ensemble des recettes qui utilisent lingredient i en utilisant une comprehension des ensembles"""
    set_recettes : Set[T] = {r for r in des if i in des[r]}
    return set_recettes

assert recette_avec(Dessert, 'beurre') == {'gateau chocolat', 'kouign amann', 'quatre-quarts'}
#(9.3 Question 3)
def tous_ingredients(des : Recette) -> Set[T]:
    """Renvoie l'ensemble de tous les ingredients apparaissant au moins une fois dans une recette des"""
    return {j for i in des for j in des[i]}

assert tous_ingredients(Dessert) == {'beurre', 'chocolat', 'farine', 'lait', 'oeuf', 'sucre', 'yaourt'}
#T9.3 -> Question 4
#Q4 - Exo 4 T9 Répondre à la question 4 en utilisant une compréhension.
#Q5 - Exo 6 T9 Répondre aux questions 1, 2 et 3 en utilisant des compréhensions.

#Exercice 10.4
#Question 1
def melements_list(l : List[T])-> Set[T]:
    """Retourne lensemble des elements qui apparaissent au moins une fois dans la liste"""
    return {i for i in l}

assert melements_list(['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']) == {'a', 'b', 'c'}
assert melements_list(['a', 'b', 'c', 'c', 'a', 'b', 'c', 'b', 'b' ]) == {'a', 'b', 'c'}

def melements_dict(l : Dict[T, int])-> Set[T]:
    """Retourne lensemble des elements qui apparaissent au moins une fois dans la liste"""
    return {i for i in l}

assert melements_dict({'a':2, 'b':4, 'c':3}) == {'a', 'b', 'c'}

#Question 2
def mdict_de_mlist(l : List[str]) -> Dict[str, int]:
    """Renvoie le dictionnaire representant du muli-ensemble represente par une liste"""
    res : Dict[str,int] = dict()
    i : str
    for i in l:
        if i in res:
            res[i] = res[i] + 1
        else:
            res[i] = 1
    return res

assert mdict_de_mlist(['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']) == {'b': 4, 'c': 3, 'a': 2}
assert mdict_de_mlist(['a', 'b', 'c', 'c', 'a', 'b', 'c', 'b', 'b' ]) == {'b': 4, 'c': 3, 'a': 2}
assert mdict_de_mlist([]) == {}

#Question 3 sans compréhension
def mlist_de_mdict(dico : Dict[str, int]) -> List[str]:
    """Renvoie la liste representante du muli-ensemble represente par un dictionnaire""" 
    res : List[str] = []
    i : str
    for i in dico:
        j : int = 0
        while j < dico[i]:
            res.append(i)
            j = j + 1
    return res 

assert mlist_de_mdict({'b': 4, 'c': 3, 'a': 2}) == ['b', 'b', 'b', 'b', 'c', 'c', 'c', 'a', 'a']   
assert mlist_de_mdict({}) == []


#Question 3 avec compréhension
def mlist_de_mdict_c(dico : Dict[str, int]) -> List[str]:
    """Renvoie la liste representante du muli-ensemble represente par un dictionnaire""" 
    return [i for i in dico for j in range(0, dico[i])]

assert mlist_de_mdict_c({'b': 4, 'c': 3, 'a': 2}) == ['b', 'b', 'b', 'b', 'c', 'c', 'c', 'a', 'a']
assert mlist_de_mdict_c({}) == []

#Question 4
def minter_dict(m1:Dict[str,int], m2:Dict[str,int]) ->Dict[str,int]:
    """Retourne la représentation en dictionnaire de leur intersection."""
    res: Dict[str,int] = dict()
    i :str
    for i in m1:
        if i in m2:
            res[i] = min(m1[i], m2[i])
    return res
        
assert minter_dict({'a':2, 'b':4, 'c':3},{'f':1, 'a':1, 'b':3}) == {'b': 3, 'a': 1}
assert minter_dict(dict(), {'f':1, 'a':1, 'b':3}) == {}
assert minter_dict({'a':2, 'b':4, 'c':3}, dict()) == {}

#Question 5 
def minter_list(l1:List[str], l2:List[str])->List[str]:
    """retourne l’intersection de deux multi-ensembles l1 et l2 représentés par des listes"""
    return mlist_de_mdict(minter_dict(mdict_de_mlist(l1),mdict_de_mlist(l2)))
    
assert minter_list(['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c'],['f', 'a', 'b', 'b', 'b']) == ['a', 'b', 'b', 'b']

#Question 6
def munion_list(l1:List[str],l2:List[str])->List[str]:
    """Renvoie l'union de l1 et l2"""
    return l1 + l2

assert munion_list(['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c'],['f', 'a', 'b', 'b', 'b']) == ['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'f', 'a', 'b', 'b', 'b']
assert munion_list([], ['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c'])==['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']
assert munion_list(['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c'], []) == ['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']

def munion_dict(d1:Dict[str,int],d2:Dict[str,int])->Dict[str,int]:
    """Renvoie l'union de s1 et s2
    """
    return mdict_de_mlist(mlist_de_mdict(d1) + mlist_de_mdict(d2))

assert munion_dict({'a':2, 'b':4, 'c':3},{'f':1, 'a':1, 'b':3})=={'a': 3, 'b': 7, 'c': 3, 'f': 1}

#Exercice 10.5
Grandes_Lignes : Dict[str, Set[str]]
Grandes_Lignes = {'Paris': {'Strasbourg', 'Dijon', 'Toulouse','Lille', 'Lyon', 'Bordeaux'},'Strasbourg':{'Paris', 'Dijon', 'München'},'München': {'Strasbourg'},'Dijon': {'Paris', 'Strasbourg', 'Lyon', 'Toulouse'},'Lyon':{'Paris', 'Dijon', 'Toulouse'},'Toulouse': {'Paris', 'Lyon', 'Dijon', 'Bordeaux'},'Bordeaux': {'Nantes', 'Paris'},'Nantes': {'Paris', 'Bordeaux','Quimper'},'Quimper':{'Nantes'}, 'Ajaccio': {'Bastia'},'Bastia': {'Ajaccio'}, 'Lille': {'Paris'}}

#Exercice 10.5 Question 1
def trajet_direct(carte: Dict[str, Set[str]], st1: str, st2: str) -> bool:
    """
    Vérifie s'il existe un trajet direct de la station st1 à la station st2 dans la carte.
    """
    if st2 in carte[st1]:
        return True
    else:
        return False

assert trajet_direct(Grandes_Lignes, 'Paris', 'Bordeaux')==True
assert trajet_direct(Grandes_Lignes, 'Paris', 'Ajaccio')==False

#Exercice 10.5 Question 2
def ajout_station(station: str, correspondances: Set[str], carte: Dict[str, Set[str]]) -> Dict[str, Set[str]]:
    """
    Ajoute la station et ses connexions directes à toutes les stations de correspondances dans la carte.
    """
    nouvelle_carte :Dict[str,Set[str]]={}

    k: str
    for k in carte:
        nouvelle_carte[k] = { e for e in carte[k] }

    s:str

    for s in carte:
        nouvelle_carte[s].add(station)

    nouvelle_carte[station] = correspondances

    return nouvelle_carte


Nouvelles_Lignes : Dict[str, Set[str]]
Nouvelles_Lignes = ajout_station('Limoges', {'Paris', 'Toulouse', 'Bordeaux'},Grandes_Lignes)
assert ajout_station('Limoges', {'Paris', 'Toulouse', 'Bordeaux'},Grandes_Lignes)==Nouvelles_Lignes


assert trajet_direct(Nouvelles_Lignes, 'Limoges', 'Paris')==True
assert trajet_direct(Nouvelles_Lignes, 'Bordeaux', 'Limoges')==True
assert trajet_direct(Nouvelles_Lignes, 'Limoges', 'Dijon')==False

#Exercice 10.5 Question 3
def stations_atteignables(carte:Dict[str,Set[str]],depart:str,k:int)->Set[str]:
    """Précondition : k>=0
    Récupère l'ensemble des stations atteignables depuis la station de départ en exactement k correspondances
    """
    stations_a_visiter : Set[str] = {depart}
    stations_visitees : Set[str] = set()

    for _ in range(k):
        stations_visitees = stations_a_visiter
        stations_a_visiter = set()
        station : str
        for station in stations_visitees:
            stations_a_visiter = stations_a_visiter | carte[station]
    return stations_a_visiter

assert stations_atteignables(Grandes_Lignes, 'Paris', 0)=={'Paris'}
assert stations_atteignables(Grandes_Lignes, 'Paris', 1)=={'Bordeaux', 'Dijon', 'Lille', 'Lyon', 'Strasbourg', 'Toulouse'}

#Exercice 10.5 Question 4
def compteur_changements(carte:Dict[str,Set[str]],depart: str,arrivee:str)->int:
    """Retourne le nombre de correspondances à effectuer pour rejoindre une station arrivee depuis une station depart pour une carte donnée
    """
    res : int = 0
    while arrivee not in stations_atteignables(carte,depart,res):
        res = res + 1
    return res

assert compteur_changements(Grandes_Lignes, 'Paris', 'Paris')==0
assert compteur_changements(Grandes_Lignes, 'Paris', 'Dijon')==1
assert compteur_changements(Grandes_Lignes, 'Paris', 'Quimper')==3
assert compteur_changements(Grandes_Lignes, 'München', 'Quimper')==5


def existence_trajet(carte:Dict[str,Set[str]],depart:str,arrivee:str)->bool:
    """Préconditions : depart et arrivee dans carte
    vérifie dans une carte donnée s'il existe un trajet entre la station depart et le station arrivee
    """
    att:Set[str]={depart}
    prev_att:Set[str]=set()
    deja_visitees:Set[str]=set()
    while len(att)>0:
        prev_att=att
        att=set()
        prec:str
        for prec in prev_att:
            suivante :str
            for suivante in carte[prec]:
                if suivante ==arrivee:
                    return True
                elif suivante not in deja_visitees:
                    att.add(suivante)
            deja_visitees.add(prec)
    return False


assert existence_trajet(Grandes_Lignes, 'Paris', 'München') == True
assert existence_trajet(Grandes_Lignes, 'Ajaccio', 'Bordeaux') == False
