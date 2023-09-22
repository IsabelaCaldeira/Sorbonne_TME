#Exercice 2.2 Question 1
def mention(note: float) -> str:
    """Précondition: 0 <= note <= 20
    Retourne le calcul de la mention 
    """
    if(0 <= note <= 9) :
        return "Eliminé"
    elif(10 <= note <= 11):
        return "Passable"
    elif(12 <= note <= 13):
        return "AB"
    elif(14 <= note <= 15):
        return "B"
    else:
        return "TB"
    
assert mention(19) == "TB"
assert mention(7) == "Eliminé"
assert mention(12) == "AB"