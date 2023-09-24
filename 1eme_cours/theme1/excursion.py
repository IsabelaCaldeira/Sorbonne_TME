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

#Exercice 1.7 Question 2
def excursion2(nb_adu: int, nb_enf: int) -> int:
    """Précondition: nb_adu >= 0 et nb_enf >= 0
    Retourne le coût minimum pour l'association d'une excursion de nb_adu et nb_enf
    """
    autocar: int = (nb_adu + nb_enf) // 60
    guide: int = nb_adu // 18 
    anim: int = nb_enf // 8
    prix_autocar = 0
    prix_guide = 0
    prix_anim = 0
    
    if(nb_adu + nb_enf) % 60 == 0:
        prix_autocar = autocar * 1200
    elif(nb_adu + nb_enf) % 60 != 0:
        prix_autocar = (autocar + 1) * 1200
        
    if nb_adu % 18 == 0:
        prix_guide = guide * 300
    elif nb_adu % 18 != 0:
        prix_guide = (guide + 1) * 300
        
    if nb_enf % 8 == 0:
        prix_anim = anim * 250
    elif nb_enf % 8 != 0:
        prix_anim = (anim + 1) * 250
        
    return (prix_anim + prix_autocar + prix_guide)

assert excursion2(18, 8) == 1750
assert excursion2(150, 120) == 12450
    
      
