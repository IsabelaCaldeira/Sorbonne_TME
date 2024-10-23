from typing import List
from typing import Tuple

#1 Partie Guidée : Polynômes
Polyn  = List[int]

ex1 : Polyn = [3, 0, 2]
ex2 : Polyn = [1, -1, 1, -1, 0]
ex3 : Polyn = [27]
ex4 : Polyn = []

CPolyn = List[ Tuple[int , int ]]
cex1 : CPolyn = [(3 , 0), (2, 2)]
cex3 : CPolyn = [(27 , 0)]
cex4 : CPolyn = []

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
def valeur(P: Polyn, x: float) -> float:
    """Renvoie la valeur de la fonction associée au polynôme calculée en x. """
    res : float = 0 
    i : int 
    for i in range(len(P)):
        res = res + P[i] * x ** i
    return res 

#Suggestion 4 Presentation 
def cdp(P: Polyn) -> str:
    """Renvoie une chaîne de caractères représentant le polynôme P."""
    if len(P) == 0:
        return "0"
    
    result: str = ""
    i: int
    for i in range(len(P)-1, -1, -1):
        if P[i] != 0:
            coeff_str: str
            if abs(P[i]) == 1 and i != 0:
                coeff_str = ""
            else:
                coeff_str = str(P[i])
            
            if result == "":
                if P[i] > 0:
                    result = coeff_str
                else:
                    result = "-" + coeff_str
            else:
                if P[i] > 0:
                    result = result + " + " + coeff_str
                else:
                    if len(coeff_str) > 0 and coeff_str[0] == '-':
                        result = result + " - " + coeff_str[1:]
                    else:
                        result = result + " - " + coeff_str
                
            if i > 1:
                result = result + "X^" + str(i)
            elif i == 1:
                result = result + "X"
    
    return result

assert cdp(ex1) == "2X^2 + 3"
assert cdp(ex4) == "0"
assert cdp(ex2) == "-X^3 + X^2 - X + 1"
assert cdp(ex3) == "27"

def pdc(p_str: str) -> List[int]:
    """Renvoie le polynôme correspondant à la chaîne de caractères p_str."""
    if len(p_str) == 0:
        return []
    
    terms: List[Tuple[int, str]] = []
    i: int = 0 
    while i < len(p_str):
        if p_str[i] == " ":
            i = i + 1
        else:
            sign: int = 1
            if i < len(p_str):
                if p_str[i] == "+":
                    i = i + 1
                elif p_str[i] == "-":
                    sign = -1
                    i = i + 1
            
            term: str = ""
            while i < len(p_str) and p_str[i] != '+' and p_str[i] != '-':
                term = term + p_str[i]
                i = i + 1
            
            terms.append((sign, term))
    
    max_exponent: int = 0
    for sign, term in terms:
        exponent: int = 0
        j: int = 0
        found: bool = False
        while j < len(term):
            if term[j] == 'X':
                if j + 1 < len(term) and term[j + 1] == '^':
                    exponent = int(term[j + 2:])
                else:
                    exponent = 1
                found = True
            j = j + 1
        if not found:
            exponent = 0
        max_exponent = max(max_exponent, exponent)
    
    coefficients: List[int] = [0] * (max_exponent + 1)
    
    for sign, term in terms:
        exponent: int = 0
        coeff: str = ""
        j: int = 0
        found: bool = False
        while j < len(term):
            if term[j] == 'X':
                coeff = term[:j]
                if j + 1 < len(term) and term[j + 1] == '^':
                    exponent = int(term[j + 2:])
                else:
                    exponent = 1
                found = True
            j = j + 1
        if not found:
            coeff = term
            exponent = 0
        
        # Remove leading and trailing spaces manually
        start: int = 0
        end: int = len(coeff)
        
        while start < end and coeff[start] == ' ':
            start = start + 1
        while end > start and coeff[end - 1] == ' ':
            end = end - 1
        
        coeff = coeff[start:end]
        coeff_int : int
        if coeff == '' or coeff == '+':
            coeff_int = 1
        elif coeff == '-':
            coeff_int = -1
        else:
            coeff_int = int(coeff)
        
        coefficients[exponent] = coefficients[exponent] + (sign * coeff_int)
    
    return coefficients

assert pdc(cdp(normalise(ex1))) == normalise(ex1)
assert pdc(cdp(normalise(ex2))) == normalise(ex2)

          
#Suggestion 6
def cdegre(pol:CPolyn)->int:
    """
    Renvoie le degre du polynome entré"""
    deg_max:int=0
    for (coeff,deg) in pol:
        if deg>deg_max and coeff!=0:
            deg_max=deg
    return deg_max

assert cdegre (cex1) == 2

def cnormalise(pol: CPolyn) -> CPolyn:
    """Renvoie la forme normale du polynome entre"""
    d:int=cdegre(pol)
    res:CPolyn=[(0,0)]*len(pol)
    for (coeff,deg) in pol:
        if coeff!=0:
            if d>=deg and deg>d-2:
                res[d]=(coeff,deg)
        d=d-1
    return res