#Exercice 1.2 Question 1
def prix_ht(prix: float, tva: float) -> float :
    """
    Préconditions: tva >= 0, 
    
    Retourne le prix hors taxes (ht) sans des taxes (tva)  
    """
    
    return prix / (1 + tva/100.0)

assert prix_ht(21, 5) == 20
assert prix_ht(67.469, 0.70) == 67.0