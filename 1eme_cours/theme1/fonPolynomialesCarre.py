#Exercice 1.3 Question 2
def polynomiales_carre(a: float, b: float, c: float, x:float) -> float :
    """Préconditions: a > 0
    Retourne la  valeur de a*x⁴ + b*x² + c
    """
    return (a*x**4 + b*x**2 + c)

assert polynomiales_carre(1, 1, 1, 2) == 21
assert polynomiales_carre(1, 1, 1, 3) == 91

###Cela ce est la version la plus simplifique parce que il y a seulement deux multiplication 
###avec le x (exemple: x² comme x**2) et pas la multiplication de lui pour lui même (exemple: x² comme X*X) 