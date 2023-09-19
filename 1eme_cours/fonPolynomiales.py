#Exercice 1.3 Question 1
def polynomiales(a: float, b: float, c: float, d:float, x:float) -> float :
    """Préconditions: a > 0
    Retourne la  valeur de a*x³ + b*x² + c*x + d 
    """
    return (a*x**3 + b*x**2 + c*x + d)

assert polynomiales(1, 1, 1, 1, 2) == 15
assert polynomiales(1, 1, 1, 1, 3) == 40

###Cela ce est la version la plus simplifique parce que il y a seulement trois multiplication 
###avec le x (exemple: x² comme x**2) et pas la multiplication de lui pour lui même (exemple: x² comme X*X) 