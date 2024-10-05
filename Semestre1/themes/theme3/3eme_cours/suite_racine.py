#Exercice 3.7 Question 1
def suite_racine(x: int, n: int) -> float:
    """Précondition n >= 0
    Renvoie une suite de la approximation de la racine de x 
    """
    i: int = 0
    u : float = 1.0
    
    while i < n:
        u = ((u+x/u)/2)
        i = i + 1

    return u             

assert suite_racine(4, 0) == 1.0
assert suite_racine(4, 1) == 2.5

def suite_racine2(x : int, n: int) -> float:
    if(n == 0):
        return 1
    return (suite_racine2(x,n-1)+ (x/suite_racine2(x,n-1)))/2

assert suite_racine2(4, 0) == 1.0
assert suite_racine2(4, 1) == 2.5

#Exercice 3.7 Question 2 
def approx_racine_stable(n: int) -> float:
    """Précondition: n >= 0
    Renvoie la racine stable avec la fonction suite_racine
    """
    x : int = 1
    n_fois1 : float = suite_racine(n, x)
    n_fois2 : float = suite_racine(n, x -1)


    while n_fois1 != n_fois2:
        x = x + 1
        n_fois1 = suite_racine(n, x)
        n_fois2 = suite_racine(n, x -1)
        
    return n_fois1
    
assert approx_racine_stable(4) == 2.0
assert approx_racine_stable(25) == 5.0

#Exercice 3.7 Question 3
def approx_racine_eps(x : int, e: float) -> float:
    """Précondition: x>= 0 
    Retourne la valeur approchée de sqrt(x) obtenu

    """
    n : int = 1
    n_fois1 : float = suite_racine(x, n)
    n_fois2  : float= suite_racine(x, n -1)

    while abs(n_fois1 - n_fois2) > e:
        n = n + 1
        n_fois1 = suite_racine(x, n)
        n_fois2 = suite_racine(x, n -1)

    return n_fois1

assert approx_racine_eps(4, 0.1) == 2.000609756097561
assert approx_racine_eps(4, 0.0001) == 2.000000000000002

