#Exercice 2.4 Question 1
def egal_eps(x1 : float, x2 : float, epsilon : float) -> bool:
    """Précondition : epsilon > 0
    Retourne True quand x1 et x2 = epsilon près.
    """
    return epsilon > abs (x1 - x2)

assert egal_eps(5,4,1.1) == True
assert egal_eps(-4,-5,1.1) == True
assert egal_eps(-3,-5,1.1) == False

#Question 2 
def fiabilite(v1 : float, v2 : float, v3 : float, epsilon : float) -> float:
    """Précondition: epsilon > 0
    Retourne le taux de fiabilité de v1, v2 et v3 à epsilon près
    """
    if egal_eps(v1, v2, epsilon):
        if egal_eps(v1, v3, epsilon):
            if egal_eps(v2, v3, epsilon):
                return 1
            else:
                return 2/3
        else:
            if egal_eps(v2, v3, epsilon):
                return 2/3
            else:
                return 0
    elif egal_eps(v2, v3, epsilon):
        if egal_eps(v1, v3, epsilon):
            return 2/3
        else:
            return 0
    else:
        return 0
    
assert fiabilite(3,3,3,1.1) == 1
assert fiabilite(3,2,1,1.1) == 2/3
assert fiabilite(1,2,3,1.1) == 2/3