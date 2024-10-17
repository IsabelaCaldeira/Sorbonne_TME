from typing import List

#Partie 1 
def identite (s : str) -> str :
    """ Renvoie la chaine s telle quelle """
    return s

def identite_texte(nom: str) -> None :
    """ Precondition : < nom > . txt est un fichier existant
    recopie le contenu du fichier < nom > . txt dans < nom > − copie .txt """
    with open(nom + ".txt", "r") as source :
        with open(nom + " − copie .txt", "w") as destination :
            ligne : str
            for ligne in source . readlines () :
                destination . write ( identite ( ligne ))

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
    if est_minuscule(c):
        a = ord(c) + n
        if a < ord('a'):
            return chr(ord('z') - (ord('a') - a - 1))
        elif a > ord('z'):
            return chr(ord('a') + (a - ord('z') - 1))
        else:
            return chr(a)
    elif est_majuscule(c):
        a = ord(c) + n
        if a < ord('A'):
            return chr(ord('Z') - (ord('A') - a - 1))
        elif a > ord('Z'):
            return chr(ord('A') + (a - ord('Z') - 1))
        else:
            return chr(a)
    else:
        return c
    
assert caractere_decale("a",0)=="a"
assert caractere_decale("a",3)=="d"
assert caractere_decale("z",3)=="c"

#Partie Guidee 2 Question 3 
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


#Partie Guidée Question 4 
def chiffre_fichier_cesar(nom: str, n: int) -> None:
    """Precondition: <nom>.txt is an existing file
    Copies the content of the file <nom>.txt into <nom>-cesar.txt, applying the Caesar cipher with key n to each line.
    """
    with open(nom + ".txt", "r") as source:
        with open(nom + "-cesar.txt", "w") as destination:
            ligne : str
            for ligne in source.readlines():
                destination.write(ligne_chiffre_cesar(ligne, n))

def dechiffre_fichier_cesar(nom: str, n: int) -> None:
    """Precondition: <nom>-cesar.txt is an existing file
    Copies the content of the file <nom>-cesar.txt into <nom>-decesar.txt, applying the Caesar cipher with key -n to each line.
    """
    with open(nom + "-cesar.txt", "r") as source:
        with open(nom + "-decesar.txt", "w") as destination:
            ligne : str
            for ligne in source.readlines():
                destination.write(ligne_dechiffre_cesar(ligne, n))  

#3 Suggestion Attaque 
def attaque_cesar(nom: str) -> None:
    """Precondition: <nom>.txt est un fichier existant
    Lit quelques lignes du fichier <nom>.txt, les déchiffre avec chaque clé de 0 à 25, et écrit les résultats dans <nom>-attaque.txt.
    """
    with open(nom + ".txt", "r") as source:
        with open(nom + "-attaque.txt", "w") as destination:

            n : int        
            for n in range(0,26):
                for ligne in source.readlines()[:5]:
                    destination.write(ligne_dechiffre_cesar(ligne,n)+"\n===================\nDécalage de : "+str(n))
             
#Suggestion 4 Chiffre Affine
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

def chiffre_fichier_affine(nom: str, a: int, b: int) -> None:
    """Pre len(nom) >= 0, a>=0, b>=0
    Renvoie le chiffre affine de la ligne du fichier nom.txt avec les clefs a et b
    """
    x : int = a 
    while pgcd(x, 26) != 1:
        x = x + 1
    with open(nom + ".txt", "r") as source:
        with open(nom + "-chiffre.txt", "w") as destination:
            ligne : str
            for ligne in source.readlines():
                char : str
                for char in ligne:
                    base : int 
                    if est_majuscule(char):
                        base = ord('A') 
                    else:
                        base = ord('a')
                    
                    p : int = ord(char) - base
                    p_chiffre : int = (x * p + b) % 26
                    char_chiffre : str = chr(p_chiffre + base)
                    destination.write(char_chiffre)  

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
    """Fonction qui chiffre la ligne selon le chiffrement de vigenere avec la clé clef."""
    ligne_chiffre: str = ""
    count:int=0
    ind:List[int]=[]
    
    s : str
    for s in clefs:
        if est_majuscule(s):
            ind.append(ord(s)-65)
        elif est_minuscule(s):
            ind.append(ord(s)-97)
    
    c : int
    for c in range(0, len(l)):
        ligne_chiffre = ligne_chiffre + caractere_decale(l[c], ind[count % len(ind)])
        count = count + 1
    return ligne_chiffre

assert ligne_chiffre_vigenere("Bonjour", "cle") == "Dzrlzyt"
assert ligne_chiffre_vigenere("bateau" , "arc") == "brverw"

def ligne_dechiffre_vigenere(l:str, clefs:str)->str:
    """Fonction qui déchiffre la ligne selon le chiffrement de vigenere avec la clé clef."""
    ligne_dechiffre: str = ""
    count:int=0
    ind:List[int]=[]
    
    s : str
    for s in clefs:
        if est_majuscule(s):
            ind.append(ord(s)-65)
        elif est_minuscule(s):
            ind.append(ord(s)-97)
    
    c : int
    for c in range(0, len(l)):
        ligne_dechiffre = ligne_dechiffre + caractere_decale(l[c], -ind[count % len(ind)])
        count = count + 1

    return ligne_dechiffre

assert ligne_dechiffre_vigenere("Dzrlzyt", "cle") == "Bonjour"
assert ligne_dechiffre_vigenere("brverw" , "arc") == "bateau"

#Suggestion 6:
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
