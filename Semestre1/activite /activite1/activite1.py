#Activité 01 Caldeira Ribeiro Cruz Isabela 21307818

import random

#Partie 1 Question 1
def sujet(x : int) -> str:
    """Pŕeconditions  0 < x < 7
    Renvoie une chaine de caractères pour chaque valeur different de x"""

    if(x == 1):
        return "Taylor "
    elif(x == 2):
        return "Aurora "
    elif(x == 3):
        return "Noah "
    elif(x == 4):
        return "Conan "
    elif(x == 5):
        return "Gracie "
    else:
        return "Renee "

assert sujet(3) == "Noah "
assert sujet(1) == "Taylor "
assert sujet(6) == "Renee "

#Partie 1 Question 2
def verbe(x : int) -> str:
    """Pŕeconditions  0 < x < 7
    Renvoie un verbe pour chaque valeur different de x"""

    if(x == 1):
        return "detruit "
    elif(x == 2):
        return "mange "
    elif(x == 3):
        return "frappe "
    elif(x == 4):
        return "aime "
    elif(x == 5):
        return "ouvre "
    else:
        return "boit "

assert verbe(3) == "frappe "
assert verbe(1) == "detruit "
assert verbe(6) == "boit "

def cod(x : int) -> str:
    """Pŕeconditions  0 < x < 7
    Renvoie un complément d'objet direct pour chaque valeur different de x"""

    if(x == 1):
        return "du chocolat "
    elif(x == 2):
        return "du cafe "
    elif(x == 3):
        return "de l'alcool "
    elif(x == 4):
        return "des boites "
    elif(x == 5):
        return "des t-shirts "
    else:
        return "des pantalons "

assert cod(3) == "de l'alcool "
assert cod(1) == "du chocolat "
assert cod(6) == "des pantalons "

def lieu(x : int) -> str:
    """Pŕeconditions  0 < x < 7
    Renvoie un lieu pour chaque valeur different de x"""

    if(x == 1):
        return "a Paris"
    elif(x == 2):
        return "dans la foret"
    elif(x == 3):
        return "a Salvador"
    elif(x == 4):
        return "dans la classe"
    elif(x == 5):
        return "dans le ciel"
    else:
        return "en Mars"

assert lieu(5) == "dans le ciel"
assert lieu(1) == "a Paris"
assert lieu(6) == "en Mars"

#Partie 1 Question 3
def phrase(a: int, b: int, c: int, d: int) -> str:
    """Précondition 0 < a,b,c,d > 7
    Renvoie une phrase 
    """
    return sujet(a) + verbe(b) + cod(c) + lieu(d)

assert phrase(2,1,1,6) == "Aurora detruit du chocolat en Mars"
assert phrase(3,4,2,5) == "Noah aime du cafe dans le ciel"

#Partie 1 Question 4
def de6() -> int:
    """Renvoie un entier aléatoire compris entre 1 et 6"""
    return int(random.random()*6+1)

assert  1 <= de6() <= 6

#Partie 1 Question 5
def phrase_aleatoire() -> str:
    """Renvoie une phrase aléatoire"""
    return phrase(de6(),de6(),de6(),de6())

#Suggestion 2
def adjectif(x: int) -> str:
    """Pŕeconditions  0 < x < 7
    Renvoie un adjectif pour chaque valeur different de x"""

    if(x == 1):
        return "gorgeous "
    elif(x == 2):
        return "the brave one "
    elif(x == 3):
        return "the beauty "
    elif(x == 4):
        return "the monster "
    elif(x == 5):
        return "the stupit "
    else:
        return "the genius "

assert adjectif(5) == "the stupit "
assert adjectif(1) == "gorgeous "
assert adjectif(6) == "the genius "

def adverbe(x: int) -> str:
    """Pŕeconditions  0 < x < 7
    Renvoie un adverbe pour chaque valeur different de x"""

    if(x == 1):
        return "heureusement "
    elif(x == 2):
        return "malureusement "
    elif(x == 3):
        return "gentiment "
    elif(x == 4):
        return "brutalement "
    elif(x == 5):
        return "sans doute "
    else:
        return "produmment "

assert adverbe(5) == "sans doute "
assert adverbe(1) == "heureusement "
assert adverbe(6) == "produmment "

def phrase2(a: int, b: int, c: int, d: int, e: int, f : int) -> str:
    """Précondition 0 < a,b,c,d > 7
    Renvoie une phrase 
    """
    return sujet(a) + adjectif(b) + verbe(c) + adverbe(f) + cod(d) + lieu(e)

assert phrase2(2,1,1,6,1,1) == "Aurora gorgeous detruit heureusement des pantalons a Paris"
assert phrase2(3,4,2,5,3,6) == "Noah the monster mange produmment des t-shirts a Salvador"

def phrase_aleatoireRiche() -> str:
    """Renvoie une phrase aléatoire"""
    return phrase2(de6(),de6(),de6(),de6(),de6(),de6())

#Suggestion 3
def verbe_intra(x: int) -> str:
    """Pŕeconditions  0 < x < 7
    Renvoie un verbe pour chaque valeur different de x"""

    if(x == 1):
        return "vit "
    elif(x == 2):
        return "cours "
    elif(x == 3):
        return "mours "
    elif(x == 4):
        return "ecrit "
    elif(x == 5):
        return "dort "
    else:
        return "ris "

assert verbe_intra(5) == "dort "
assert verbe_intra(1) == "vit "
assert verbe_intra(6) == "ris "
        
def phrase_aleatoire2() -> str:
    """Renvoie une phrase aleatoire avec un verbe intrasitif ou transitfs et le COD
    """ 
    x : int = de6()
    if(x > 3):
        return phrase_aleatoireRiche()
    else:
        return sujet(de6()) + adjectif(de6()) + verbe_intra(de6())+ adverbe(de6()) + lieu(de6())

#Suggestion 4
def ldvelh(a : int) -> str:
    """Precondition 14 > a > 0
    Renvoie une aventure à la recherche d'Aengus """
    
    if (a == 1):
        return "Vous êtes un jeune aventurier à la recherche d'Aengus, le dieu de l'amour et de la jeunesse. Les anciens racontent qu'il vit dans un magnifique palais au-delà des montagnes. Partir vers les montagnes (allez au chapitre 2) ou demander des conseils à la sage du village (allez au chapitre 3)"
        
    elif(a == 2):
        return "Vous gravissez les montagnes, mais la route est périlleuse. Soudain, vous êtes confronté à un vent puissant. Lutter contre le vent et continuer (allez au chapitre 4) ou chercher un abri dans une grotte (allez au chapitre 5)"
        
    elif(a == 3):
        return "La sage vous parle de la légende d'Aengus. Elle vous recommande de chercher une fleur rare qui est la clé pour atteindre son palais. Partir à la recherche de la fleur (allez au chapitre 6) ou ignorer son conseil et partir vers les montagnes (allez au chapitre 2)"
        
    elif(a == 4):
        return "Vous luttez vaillamment contre le vent et parvenez à atteindre le sommet. Là, vous découvrez une vue magnifique et une clairière. Explorer la clairière (allez au chapitre 7) ou continuer vers le palais d'Aengus (allez au chapitre 8)"
        
    elif(a == 5):
        return "Dans la grotte, vous trouvez un trésor ancien, mais vous êtes piégé par un esprit malveillant. Fin du jeu."
        
    elif(a == 6):
        return "Vous partez à la recherche de la fleur rare. Après de nombreuses aventures, vous la trouvez, mais elle est gardée par une créature magique.Affronter la créature (allez au chapitre 9) ou tenter de négocier avec elle (allez au chapitre 10)"
        
    elif(a == 7):
        return "Dans la clairière, vous trouvez un passage secret qui mène au palais d'Aengus. Vous êtes enfin près de votre but ! Entrer dans le palais (allez au chapitre 11) ou prendre le temps d'explorer la clairière (allez au chapitre 12)"
        
    elif(a == 8):
        return"Vous atteignez le palais d'Aengus, mais il est protégé par des énigmes. Vous devez résoudre ces énigmes pour entrer. Essayer de résoudre l'énigme (allez au chapitre 13) ou retourner sur vos pas (allez au chapitre 4)"
        
    elif(a == 9):
        return"Vous vous battez courageusement contre la créature, mais elle est trop puissante. Vous perdez la bataille.Fin du jeu."
        
    elif (a == 10):
        return"La créature est impressionnée par votre sagesse et vous laisse passer. Vous obtenez la fleur rare et pouvez maintenant entrer dans le palais d'Aengus. Maintenant vous pouvez entrer dans le palais (allez au chapitre 11)"
        
    elif(a == 11):
        return "Vous entrez dans le palais d'Aengus et êtes accueilli par sa beauté. Aengus apparaît et vous offre un sourit.Là vous trouverez les réponses que vous cherchez <3 Fin du jeu."
        
    elif(a == 12):
        return"Vous explorez la clairière et découvrez d'autres secrets du monde, mais vous n'atteignez jamais le palais d'Aengus. Fin du jeu."
        
    else:
        return"Vous résolvez l'énigme avec brio et Aengus vous permet d'entrer. Vous êtes maintenant dans son royaume magique. Là vous trouverez les réponses que vous cherchez <3 Fin du jeu."

assert ldvelh(1) == "Vous êtes un jeune aventurier à la recherche d'Aengus, le dieu de l'amour et de la jeunesse. Les anciens racontent qu'il vit dans un magnifique palais au-delà des montagnes. Partir vers les montagnes (allez au chapitre 2) ou demander des conseils à la sage du village (allez au chapitre 3)"

assert ldvelh(11) == "Vous entrez dans le palais d'Aengus et êtes accueilli par sa beauté. Aengus apparaît et vous offre un sourit.Là vous trouverez les réponses que vous cherchez <3 Fin du jeu." 
