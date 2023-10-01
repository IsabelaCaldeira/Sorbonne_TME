#Exercice 1.6 Question 1
def nombre_fermat(n : int) -> int:
    """
    Préconditions n => 0
    Retourne calculer le nombre de Fermat
    """
    return (2**2**n)+1

assert nombre_fermat(0) == 3
assert nombre_fermat(1) == 5
assert nombre_fermat(2) == 17
assert nombre_fermat(5) == 4294967297

#Question 2
def nombre_premier(n1 : int)-> str:
    """Pŕeconditions n1 => 0
    Vérifier si Fn est premier ou non-premier.
    """
    if(nombre_fermat(n1) % 641 == 0):
        return "Le nombre est non-premier"
    else:
        return "Le nombre est premier"
    
assert nombre_premier(0) == "Le nombre est premier"
assert nombre_premier(1) == "Le nombre est premier"
assert nombre_premier(2) == "Le nombre est premier"
assert nombre_premier(5) == "Le nombre est non-premier"
    
