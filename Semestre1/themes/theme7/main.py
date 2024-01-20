

import math as math
#Exercice 7.4 Question 1
def pgcd(x:int,y:int)->int:
    """Précondition : x>=y et x>0
    Retourne le plus grand commun diviseur de x et y
    """
    q : int = x
    p : int = y
    temp : int = 0
    while p!=0:
        temp = q%p
        q = p
        p = temp
    return q
        
assert pgcd(9,3)==3
assert pgcd(15,15)==15

def fraction(a:int,b:int)->Tuple[int,int]:
    """Précondition : b!=0
    retourne la fraction canonique de a/b
    """
    return a//pgcd(a,b),b//pgcd(a,b)

assert fraction(9,12)==(3,4)
assert fraction(180,240)==(3,4)

#Exercice 7.4 Question 2
def frac_mult(f1:Tuple[int,int],f2:Tuple[int,int])->Tuple[int,int]:
    """Précondition : les dénominateurs sont différents de 0
    retourne la multiplication de deux fractions f1 et f2 sous la forme d'une fraction canonique
    """
    a,b = f1
    c,d = f2
    return fraction(a*c,b*d)

assert frac_mult((3,4),(8,4))==(3,2)
assert frac_mult((3,4),(0,2))==(0,1)

#Exercice 7.4 Question 3
def frac_div(f1:Tuple[int,int],f2:Tuple[int,int])->Tuple[int,int]:
    """Précondition : les dénominateurs sont différents de 0
    renvoie la division entre deux fractions rationnelles
    """
    a,b = f1
    c,d = f2
    e : int = d
    f : int = c
    return frac_mult(f1,(e,f))

assert frac_div((3,4),(4,8))==(3,2)
assert frac_div((3,4),(1,1))==(3,4)

#Exercice 7.4 Question 4
def lcm(x:int,y:int)->int:
    """Précondition : a!=0 et b!=0
    renvoie le plus petit commun multiple de x et y
    """
    p : int = 0
    if x>=y:
        return (x*y)//pgcd(x,y)
    else:
        return (x*y)//pgcd(y,x)

assert lcm(4,3)==12
assert lcm(11,17)==187

def frac_add(f1:Tuple[int,int],f2:Tuple[int,int])->Tuple[int,int]:
    """Précondition : les dénominateurs sont différents de 0
    retourne la fraction canonique correspondant à la somme de 2 fractions
    """
    a,b = f1
    c,d = f2
    p : int = lcm(b,d)
    return fraction((a*(p//b)+c*(p//d)),p)

assert frac_add((8,4),(1,4))==(9,4)
assert frac_add((9,4),(5,4))==(7,2)

#Exercice 7.5 Question 1
Point = Tuple[int,int]

def vecteur(p1:Point,p2:Point)->Point:
    """renvoie le couple de coordonnées du vecteur formé par les points p1 et p2
    """
    x1,y1 = p1
    x2,y2 = p2
    return x2-x1,y2-y1

assert vecteur((0,0),(1,1))==(1,1)
assert vecteur((1,1),(5,5))==(4,4)

#Exercice 7.5 Question 2
def vectoriel(p1:Point,p2:Point)->int:
    """renvoie le produit vectoriel entre deux points
    """
    x1,y1 = p1
    x2,y2 = p2
    return x1*y2-y1*x2

assert vectoriel((0,0),(1,1))==0
assert vectoriel((2,4),(2,1))==-6

def alignes(p1:Point,p2:Point,p3:Point)->bool:
    """vérifie si les trois points sont alignés
    """
    p12 : Point = vecteur(p1,p2)
    p23 : Point = vecteur(p2,p3)
    return vectoriel(p12,p23)==0

assert alignes((0,0),(1,1),(5,5))
assert not(alignes((0,0), (1,1), (1,2)))

#Exercice 7.5 Question 3
def alignement(L:List[Point])->bool:
    """Précondition : len(L)>=3
    vérifie si tous les points de la liste sont alignés
    """
    i : int = 0
    rep_courante : bool = True
    while ((rep_courante) and (i+2<len(L))):
        rep_courante = alignes(L[i],L[i+1],L[i+2])
        i = i+1
    return rep_courante

assert alignement([(0,0),(1,1),(5,5)])
assert not(alignement([(0,0),(1,1),(5,5),(1,0)]))
        
