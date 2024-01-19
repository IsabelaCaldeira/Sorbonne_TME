#Exercice 5.5
def est_voyelle(c : str) -> bool:
    """Précondition : len(c) == 1
    Retourne True si et seulement si c est une voyelle
    miniscule ou majuscule.
    """
    return (c == 'a') or (c == 'A') \
        or (c == 'e') or (c == 'E') \
        or (c == 'i') or (c == 'I') \
        or (c == 'o') or (c == 'O') \
        or (c == 'u') or (c == 'U') \
        or (c == 'y') or (c == 'Y')

# Jeu de tests
assert est_voyelle('a') == True
assert est_voyelle('E') == True
assert est_voyelle('b') == False
assert est_voyelle('y') == True
assert est_voyelle('z') == False

#Exercice 5.5 Question 1 
def nb_voyelles(s : str) -> int:
    """Précondition len(s) > 0
    Renvoie le nombre de voyelles dans une phrase
    """
    voyelles: int = 0
    i : int = 0
    while i <= len(s) - 1:
        if est_voyelle(s[i]) == True:
            voyelles = voyelles + 1 
        i = i + 1

    return voyelles

assert nb_voyelles('la maman du petit enfant le console') == 12
assert nb_voyelles('mr brrxcx') == 0

#Exercice 5.5 Question 2
def nb_voyelles_accents(s:str) -> int:
    """Précondition len(s) > 0
    Renvoie le nombre de voyelles dans une phrase avec des accents
    """
    voyelles_accents : int = 0
    voyelles : int = 0
    i : int = 0

    while i <= len(s) -1:
        if est_voyelle(s[i]) == True \
        or (s[i] == 'é') or (s[i] == 'É')\
        or (s[i] == 'è') or (s[i] == 'È')\
        or (s[i] == 'ê') or (s[i] == 'Ê')\
        or (s[i] == 'à') or (s[i] == 'À'):
            voyelles = voyelles + 1 
        i = i + 1

    return voyelles
            
assert nb_voyelles_accents('la maman du bébé le réconforte') == 11

#Exercice 5.5 Question 3
def sans_voyelle(s : str) -> str:
    """Précondition len(s) > 0
    Élimine les voyelles d’une phrase 
    """

    voyelles_accents : int = 0
    sans : str = ""
    i : int = 0

    while i <= len(s) -1:
        if est_voyelle(s[i]) == True \
        or (s[i] == 'é') or (s[i] == 'É')\
        or (s[i] == 'è') or (s[i] == 'È')\
        or (s[i] == 'ê') or (s[i] == 'Ê')\
        or (s[i] == 'à') or (s[i] == 'À'):
            sans = sans +""
        else:
            sans = sans + s[i]
        i = i + 1

    return sans

assert sans_voyelle('aeiouy') == ''
assert sans_voyelle('la balle au bond rebondit') == 'l bll  bnd rbndt'

#Exercice 5.5 Question 4
def mot_mystere(s: str) -> str:
    """Précondition: len(s) > 0
    Remplace dans une chaîne de caractères les voyelles par _
    """

    voyelles_accents : int = 0
    mot : str = ""
    i : int = 0

    while i <= len(s) -1:
        if est_voyelle(s[i]) == True \
        or (s[i] == 'é') or (s[i] == 'É')\
        or (s[i] == 'è') or (s[i] == 'È')\
        or (s[i] == 'ê') or (s[i] == 'Ê')\
        or (s[i] == 'à') or (s[i] == 'À'):
            mot = mot +"_"
        else:
            mot = mot + s[i]
        i = i + 1
    return mot

assert mot_mystere('aeiouy') == '______'
assert mot_mystere('mr brrxcx') == 'mr brrxcx'