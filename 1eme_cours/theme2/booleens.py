#Exercice 2.6 Question 1 
def ou(p : bool, q: bool) -> bool :
    """Retourne la disjonction de p et q."""
    if(p == True):
        return True
    elif(q == True):
        return True
    else:
        return False
    
def et(p: bool, q: bool) -> bool:
    """Retourne la conjonction de p et q."""
    if(p == True):
        if(q == True):
            return True
    else: 
        return False
        
def non(p: bool) -> bool :
    """"Retourne la négation de p."""
    if(p == True):
        return False
    else:
        return True
    
assert ou(True, False) == True
assert ou(et(True, False), False) == False
assert et(ou(False, True), non(False)) == True
assert non(non(3 == 1 + 2)) == True

#Exercice 2.6 Question 2 
# ( ou(3 == 3, 5 // 0 == 2))
# Avec la fonction ou la division ne marche pas. 
# (3 == 3) or (5 // 0 == 2)
#Mais avec le "or" nous avons le resultat "True" et pas d'erreur
#La même situation se répète avec la fonction "et" et "and"

#Exercice 2.6 Question 3 
def implique(p: bool, q: bool) -> bool:
    if(ou(non(p), q == True)):
        return True
    else:
        return False
    
assert implique(False, False) == True
assert implique(True, False) == False
assert implique(True, 3 == 3) == True

def ou_exclusif(p: bool, q: bool) -> bool:
    if(et(p, q == True)):
        return False
    elif(ou(p,q == True)):
        return True
    else: 
        return False
    
assert ou_exclusif(True, False) == True
assert ou_exclusif(3 == 2, 3 == 3) == True
assert ou_exclusif(2 == 2, 3 == 3) == False
