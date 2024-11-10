def perimetre(longeur: float, largeur: float) -> float : 
    """
    Précondition: (largeur >= 0) and (longeuer >= 0) and (largeur >= longueur)

   Retourne le périmètre du rectangle défini par sa largeur et sa longueur
    """
    return 2 * (largeur + longeur)

assert perimetre(1,1) == 4
assert perimetre(2,3) == 10