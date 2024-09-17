def mention(x: float) -> str:
    """Précondition: 0 <= x <= 20
    Retourne le calcul de la mention 
    """
    if(x < 10):
        return "Eliminé"
    elif(x < 12):
        return "Passable"
    elif(x < 14):
        return "AB"
    elif(x < 16):
        return "B"
    else:
        return "TB"

assert mention(0) == "Eliminé"
assert mention(8) == "Eliminé"
assert mention(10) == "Passable"
assert mention(12.5) == "AB"
assert mention(15) == "B"
assert mention(20) == "TB"

#Exercice 2.2 Question 2
def mention2(note : float) -> str:
    """Précondition: 0 <= note <= 20
    Retourne le calcul de la mention 
    """    
    if(note < 12):
        if(note < 10):
            return "Eliminé"
        else:
            return "Passable"
    elif(note < 14):
        return "AB"
    elif(note < 16):
        return "B"
    else:
        return "TB"
    
assert mention2(0) == "Eliminé"
assert mention2(8) == "Eliminé"
assert mention2(10) == "Passable"
assert mention2(12.5) == "AB"
assert mention2(15) == "B"
