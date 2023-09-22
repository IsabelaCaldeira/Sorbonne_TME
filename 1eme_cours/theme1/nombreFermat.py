#Exercice 1.6 Question 1
def nombre_fermat(n : float) -> float:
    """
    Préconditions n => 0
    Retourne calculer le nombre de Fermat
    """
    return (2**2**n)+1

assert nombre_fermat(0) == 3
assert nombre_fermat(1) == 5
assert nombre_fermat(2) == 17

#Question 2
def nombre_premier(n1 :float)-> float:
    """Pŕeconditions n1 => 0
    Vérifier si Fn est premier ou non-premier.
    """
    