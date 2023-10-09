#Exercice 5.7 Question 1
def ord2(n:str)->int:
    """Précondition : n est une chaîne de caractère d'un entier positif de longueur 1
    """
    

def chiffre(n:str)->int:
    """Précondition : n est une chaîne de caractère d'un entier positif de longueur 1
    renvoie l'entier qui correspond
    """
    p:int=48
    compteur :int = 0
    while p-ord(n)!=0:
        p=p+1
        compteur=compteur+1
    return compteur

assert chiffre('5')==5
assert chiffre('8')==8

#Exercice 5.7 Question 2
def entier(s:str)->int:
    """Précondition : s est une chaîne de caractère d'un entier positif
    retourne l'entier représenté par la chaîne s
    """
    i:int
    r:int=0
    for i in range(len(s)):
        r=r*10
        r=r+chiffre(s[i])
    return r

assert entier('42')==42
assert entier('0012')==12

#Exercice 5.7 Question 3
def chr(n:int)->str:
    """Précondition : 48<=n<=57
    construit un caractère à partir de son numéro Unicode n"""

def caractere(n:int)->str:
    """Précondition : 0<=n<=9
    retourne le caractère qui représente le chiffre n
    """
    return str(n)

assert caractere(8)=='8'
assert caractere(4)=='4'

#Exercice 5.7 Question 4
def chaine(n:int)->str:
    """Précondition n>=0
    retourne la chaîne représentant l'entier naturel n
    """
    return str(n)

assert chaine(42)=='42'
assert chaine(entier('122'))=='122'