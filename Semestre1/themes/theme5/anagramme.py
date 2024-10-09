#Exercice 5.9 Question 1
def moins_lettre(c:str, a:str) -> str:
    """len(a) && len(c) >= 0
    Renvoie la chaîne obtenue à partir de la chaîne c en supprimant la première occurence de la lettre a dans c si c contient au moins une fois a sinon None"""
    i: int    
    for i in range(len(c)-1):
        if c[i] == a:
            return c[0:i] + c[i+1:len(c)]
    
    return None

assert moins_lettre("test", "e") == "tst"

#Exercice 5.9 Question 2
def anagramme(m1:str,m2:str) -> bool:
    """len(m1) && len(m2) >= 0
    Renovie True si m1 et m2 sont anagrammes"""

    lettre: str
    for lettre in m1:
        m3 : str = moins_lettre(m2, lettre)
        if m3 == " ":
            return False
    return True

assert anagramme("alberteinstein", "alberteinstein") == True
