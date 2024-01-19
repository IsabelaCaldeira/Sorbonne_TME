#Activite 01 - Cadavres Exquis Doha Rachid - Isabela Caldeira
import random
import math
#Exercice 1.1
def sujet(n : int) -> str:
    """
    Precondition: 1 <= n <= 6
    Retourne = le sujet d'une phrase
    """
    if(n == 1):
        return "Taylor"
    elif(n == 2) :
        return "Swift"
    elif(n == 3):
        return "Harry"
    elif(n == 4):
        return "Styles"
    elif(n == 5):
        return "Doha"
    else:
        return "Isabela :)"

assert sujet(6) == "Isabela :)"
assert sujet(1) == "Taylor"
assert sujet(5) == "Doha"

#Exercice 1.2
def verbe(n : int) -> str:
    """
    Precondition: 1 <= n <= 6
    Retourne: Un verbe transitif direct d'une phrase
    """
    if(n == 1):
        return "chante"
    elif(n == 2) :
        return "mange"
    elif(n == 3):
        return "écrit"
    elif(n == 4):
        return "ouvre"
    elif(n == 5):
        return "casse"
    else:
        return "boit"
    
assert verbe(4) == "ouvre"
assert verbe(5) == "casse"
assert verbe(1) == "chante"

def cod(n : int) -> str:
    """
    Precondition: 1 <= n <= 6
    Retourne: un complement d’objet direct d'une phrase
    """
    if(n == 1):
        return "une chanson"
    elif(n == 2) :
        return "un café"
    elif(n == 3):
        return "des boites"
    elif(n == 4):
        return "un téléphone"
    elif(n == 5):
        return "des bonbons"
    else:
        return "de l'alcool"

assert cod(5) == "des bonbons"
assert cod(2) == "un café"
assert cod(3) == "des boites"

def lieu(n : int) -> str:
    """
    Precondition: 1 <= n <= 6
    Retourne: Un complement circonstanciel de lieu d'une phrase
    """
    if(n == 1):
        return "a New York"
    elif(n == 2) :
        return "a la maison"
    elif(n == 3):
        return "a la plage"
    elif(n == 4):
        return "dans la classe"
    elif(n == 5):
        return "dans le club"
    else:
        return "a Rio de Janeiro"

assert lieu(6) == "a Rio de Janeiro"
assert lieu(1) == "a New York"
assert lieu(3) == "a la plage"

#Exercice 1.3
def phrase(a: int, b: int, c: int, d: int) -> str:
    """Precondition:: 1 <= a <= 6, : 1 <= b <= 6, : 1 <= c <= 6, : 1 <= d <= 6
    Retourne: une phrase
    """
    return sujet(a)+ " " +verbe(b)+ " " +cod(c)+ " " +lieu(d)

assert phrase(1, 1, 1, 4) == "Taylor chante une chanson dans la classe"
assert phrase(3, 6, 6, 5) == "Harry boit de l'alcool dans le club"

#Exercice 1.4
def de6()-> int:
    """ Retourne un nombre entre 1 et 6 """
    return math.floor(random.random()*6+1)

assert 1 <= de6() <= 6

#Exercice 1.5
def phrase_aleatoire() -> str:
    """
    Retourne une phrase aleatoire
    """
    return phrase(de6(),de6(),de6(),de6())

#Exercice 3 Suggestion 
def verbe_intra(n:int) -> str:
    """Précondition: 1<= n <= 6
    Retourne: un verbe intrasitif d'une phrase
    """

    if(n == 1):
        return "dors"
    elif(n == 2):
        return "meurt"
    elif(n == 3):
        return "marche"
    elif(n == 4):
        return "crie"
    elif(n == 5):
        return "parle"
    else:
        return "ment"
    
assert verbe_intra(4) == "crie"
assert verbe_intra(5) == "parle"
assert verbe_intra(1) == "dors"

def phrase_aleatoire2() -> str:
    """
    """
    x : int = math.floor(random.random()*2+1)
    if x == 1:
        return phrase_aleatoire()
    else:
        return sujet(de6()) + " " + verbe_intra(de6())+" " +lieu(de6())

print(phrase_aleatoire2())