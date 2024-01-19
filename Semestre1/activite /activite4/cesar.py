#2 Partie Guidée : Chiffre de César
#Question 1
def est_minuscule(lettre:str)->bool:
    """Décide si un caractère est une des 26 lettres romaines minuscules
    """
    if ((ord(lettre)>=97) and (ord(lettre)<=122)):
        return True

assert not(est_minuscule("C"))
assert est_minuscule("c")
assert not(est_minuscule(" "))

def est_majuscule(lettre:str)->bool:
    """Décide si un caractère est une des 26 lettres romaines majuscules
    """
    if ((ord(lettre)>=65) and (ord(lettre)<=90)):
        return True

assert est_majuscule("C")
assert not(est_majuscule("c"))
assert not(est_majuscule(" "))

#Question 2 
def caractere_decale(c:str,n:int)->str:
    """Précondition : n>=0 et len(c)=1
    renvoie le caractère obtenu par un décalage de n
places dans l'alphabet de c si c est une lettre romaine (majuscule ou minuscule), et c sinon.
    """
    a : int = ord(c)+n
    s : int = a-122
    t : int = a-90
    u : int = 97 - a
    v : int = 65 - a
    
    if est_minuscule(c):
        if n>=0:
            if a>122:
                return chr(96+s)
            else:
                return chr(a)
        else:
            if a<95:
                return chr(a)
            else:
                return chr(96-s)
    elif est_majuscule(c):
        if n>=0:
            if a>90:
                return chr(64+t)
            else:
                return chr(a)
        else:
            if a<90:
                return chr(a)
            else:
                return chr(64-t)
    else:
        return c

assert caractere_decale("a",0)=="a"
assert caractere_decale("a",3)=="d"
assert caractere_decale("z",3)=="c"

#Question 3.1
def ligne_chiffre_cesar(s: str, n: int) -> str:
    """Précondition n>=0 et len(s)>=1
    Renvoie la chaine obtenue en appliquant le chiffrement de César de clef n à s.
    """
    a : str = "" 
    i : int
    for i in range (len(s)):
        a = a + caractere_decale(s[i], n)
    return a

assert ligne_chiffre_cesar (" Bonjour LU1IN011 ", 3) == " Erqmrxu OX1LQ011 "
assert ligne_chiffre_cesar (" Bonjour LU1IN011 ", 0) == " Bonjour LU1IN011 "

#Question 3.2
def ligne_dechiffre_cesar(s: str, n: int) -> str:
    """Précondition n>=0 et len(s)>=1
    Renvoie la chaine obtenue en appliquant le dechiffrement de César de clef n à s.
    """
    return ligne_chiffre_cesar(s, -n)

assert ligne_dechiffre_cesar (" Erqmrxu OX1LQ011 ", 3) == " Bonjour LU1IN011 "
assert ligne_dechiffre_cesar (" Bonjour LU1IN011 ", 0) == " Bonjour LU1IN011 "

#4 Suggestion : Chiffre affine
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


def affine_majuscule(x:int,y:int,p:str)->int:
    """Précondition : len(p)=1
    Retourne un nombre entre 0, qui correspond à "A", et 25, qui correspond à "Z"
    """
    return (x*(ord(p)-ord("A"))+y)%26

assert affine_majuscule(3,2,"A")==2
assert affine_majuscule(3,2,"M")==12

def affine_minuscule(x:int,y:int,p:str)->int:
    """Précondition : len(p)=1
    Retourne un nombre entre 0, qui correspond à "a", et 25, qui correspond à "z"
    """
    return (x*(ord(p)-ord("a"))+y)%26

assert affine_minuscule(3,2,"a")==2
assert affine_majuscule(3,2,"m")==4

def ligne_chiffre_affine(nom:str,a:int,b:int)->str:
    """Précondition : 0<=a<=25 et 0<=b<=25 ; a et 26 doivent être premiers entre eux
    complexifie le chiffre de César en un chiffre affine qui utilise deux clefs a et b
    """
    c : str = ''
    a2 : int = a
    
    while pgcd(a2,26)!=1:
        a2 = a2 + 1
    
    i : str
    for i in nom:
        if est_majuscule(i):
            c = c + chr(ord('A') + affine_majuscule(a2,b,i))
        elif est_minuscule(i):
            c = c + chr(ord('a') + affine_minuscule(a2,b,i))
        else:
            c = c + i
    return c

assert ligne_chiffre_affine("Bonjour LU1IN011!",3,7)=="Kxuixpg OP1FU011!"
assert ligne_chiffre_affine("Bonjour LU1IN011!",14,47)=="Kxiaxjq EJ1LI011!"
#5 Suggestion: chiffre de vigenère
def ligne_chiffre_vigenere(l:str, clefs:str)->str:
    """Fonction qui prend en entrer une chaine de caractères ligne et une chaine de caractère clef et chiffre la ligne selon le chiffrement de vigenere avec la clé clef et renvoie cette ligne chiffré."""
    ligne_chiffre:str=""
    sss:str
    count:int=0
    ind:List[int]=[]
    for sss in clefs:
        if est_majuscule(sss):
            ind.append(ord(sss)-65)
        elif est_minuscule(sss):
            ind.append(ord(sss)-97)
    lenClef:int=len(clefs)
    ssss:str
    for ssss in l:
        ligne_chiffre=ligne_chiffre+caractere_decale(ssss, ind[count])
        count=(count+1)%lenClef
    return ligne_chiffre
assert ligne_chiffre_vigenere("Bonjour", "cle") == "Dzrlzyt"
assert ligne_chiffre_vigenere("bateau" , "arc") == "brverw" 


#suggestion6:
def ligne_chiffre_scytale (s:str, n:int)->str:
    """précondition:
renvoie le chiffre avec scytale"""
    phrase:str=""
    saut:int=0
    colonne: int = len (s) // n 
    for i in range (colonne):
        saut =i
        for j in range (n+1):
            if saut < len(s):
                phrase = phrase + s[saut]
                saut = saut + (colonne)
    return phrase
           
def ligne_dechiffre_scytale (s:str, n:int)->str:
    """précondition:
renvoie la ligne dechiffre avec scytale"""
    phrase:str=""
    saut:int=0
    colonne: int = len (s) // n 
    for i in range (n):
        saut =i
        for j in range (colonne):
            if saut < len(s):
                print ("s", saut)
                phrase = phrase + s[saut]
                saut = saut + n
    return phrase
