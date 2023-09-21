def factorielle(n : int) -> int:
    """Précondition: n >= 0
    retourne n!
    """
    #déclaration et initialisation variables
    res : int = 1
    i :  int = 1 
    
    while i <= n:
        res = res * i
        i = i +1
        
        return res
    
assert factorielle(0) == 1
assert factorielle(1) == 1
assert factorielle(5) == 120
    