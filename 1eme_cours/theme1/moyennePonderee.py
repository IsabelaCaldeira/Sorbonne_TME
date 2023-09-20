#Exercice 1.1 Question 2
def moyenne_ponderee(a: float, b: float, c: float, pa: float, pb: float, pc:float) -> float :
    """ 
        Retourne la moyenne pondérée de nombres
        flotantes pour arriver à la moyenne 
    """
    return (a*pa + b*pb + c*pc)/( pa + pb + pc )

assert moyenne_ponderee(2,2,2,2,2,2) == 2
assert moyenne_ponderee(1,2,3,3,2,2) == 13/7
assert moyenne_ponderee(5, 10, 40, 1, 2, 1) == 68
