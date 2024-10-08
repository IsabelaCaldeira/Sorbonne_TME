#Exercice 5.6 Question 1
def base_comp(base : str)-> str:
    """ len(c)>= 0
    Renvoie le base complementaire"""

    if base == 'A':
        return 'T'
    elif base == 'T':
        return 'A'
    elif base == 'C':
        return 'G'
    else:
        return 'C'

assert base_comp('A') == 'T'
assert base_comp('G') == 'C'
assert base_comp('C') == 'G'
assert base_comp('T') == 'A'

#Exercice 5.6 Question 2
def brin_comp(brin : str)-> str:
    """Pre len(brin) >= 0
    Renvoie le brin d'ADN complémentaire"""

    res : str = "" 
    i : int = 0 
    while len(brin) > i:
        res = base_comp(brin[i]) + res     
        i = i + 1
    return res

assert brin_comp('ATCG') == 'CGAT'
assert brin_comp('ATTGCCGTATGTATTGCGCT') == 'AGCGCAATACATACGGCAAT'

#Exercice 5.5 Question 3
def test_comp(a: str, b: str) -> bool:
    """Pre a && b >= 0
    Renovie si a et b sont complementaires"""

    if len(a) != len(b):
        return False

    if brin_comp(a) != b:
        return False
        
    return True    

assert test_comp('', 'ATCG') == False
assert test_comp('ATCG', 'CGAT') == True
assert test_comp('ATTGCCGTATGTATTGCGCT', 'AGCGCAATACATACGGCAAT') == True

#Exercice 5.6 Question 4 
def test_sous_sequence(a: str, b: str) -> bool:
    """len(a), len(b) >= 0
    Renvoie si le premier est une sous-sequence du second"""

    i : int
    for i in range(len(b) - len(a) + 1):
        if b[i:i+len(a)] == a:
            return True
    return False

assert test_sous_sequence('','') == True
assert test_sous_sequence('','ATCG') == True
assert test_sous_sequence('ATCG','') == False

#Exercice 5.6 Question 5
def recherche_sous_sequence(b1: str, b2: str) -> Optional[int]:
    """len(b1)&& len(b2) >= 0
    Renvoie lindice de b2 correpondant au debut de b1 si b1 est une sous-sequence de b2 et ne renvoie rien sinon"""
    i : int
    for i in range(len(b2) - len(b1) + 1):
        if b2[i:i+len(b1)] == b1:
            return i
    return None

assert recherche_sous_sequence('','') == 0
assert recherche_sous_sequence('','ATCG') == 0
assert recherche_sous_sequence('ATCG','') == None