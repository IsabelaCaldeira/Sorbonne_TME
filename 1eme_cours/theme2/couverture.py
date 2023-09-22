#Exercice 2.3 Question 1
def f(n1 : float, n2 : float, n3 : float) -> str:
    """Précondition : n1 != n2 and n2 != n3 and n3 != n1
    retourne un cas parmi 6 selon les valeurs de n1, n2 et n3.
    """
    if n1 < n2 and n2 < n3:
        return 'cas 1'
    elif n1 < n3 and n3 < n2:
        return 'cas 2'
    elif n2 < n1 and n1 < n3:
        return 'cas 3'
    elif n2 < n3 and n3 < n1:
        return 'cas 4'
    elif n3 < n1 and n1 < n2:
        return 'cas 5'
    else:
        return 'cas 6'

assert f(2.3, 2.5, 2.7) == 'cas 1'
assert f(7, 2, 5) == 'cas 4'
assert f(6, 18, 4) == 'cas 5'
assert f(9, 17, 15) == 'cas 2'
assert f(1.3, 0.7, 3.7) == 'cas 3'
assert f(9, 9, 9) == 'cas 6'