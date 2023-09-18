def prixTTC(ht: float, tva: float) -> float :
    """
    Préconditions: ht > 0, tva >= 0
    
    Retourne le prix hors taxes (ht) avec des taxes (tva)  
    """
    
    return ht * (1 + tva/100)

assert prixTTC(20, 5) == 21.0
assert prixTTC(67.0 , 0.70) == 67.469

