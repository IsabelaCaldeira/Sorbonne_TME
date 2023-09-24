#Exercice 1.7 Question 1 
def excursion(nb_pers: int) -> int:
    """Préconditions: nb >= 0
    Retourne le coût mininum pour l'association d'une excursion de nb_pers personnes
    """
    autocar : int = nb_pers // 60
    guide: int = nb_pers // 18
    if nb_pers % 60 == 0 and nb_pers % 18 == 0:
        return autocar * 1200 + guide * 300
    elif nb_pers % 60 != 0 and nb_pers % 18 == 0:
        return (autocar + 1) * 1200 + guide * 300
    elif nb_pers % 60 == 0 and nb_pers % 18 != 0:
        return autocar * 1200 + (guide + 1) * 300
    else:
        return (autocar + 1) * 1200 + (guide + 1) * 300
    
assert excursion(18) == 1500
assert excursion(61) == 3600
