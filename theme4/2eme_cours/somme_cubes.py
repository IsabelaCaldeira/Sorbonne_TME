def somme_cubes(n : int) -> int:
    """
        Précondition
        retourne ???
    """
    # ?? à quoi sert s ?
    somme : int = 0
    k : int = 1
    while k <= n:
        somme = somme + (n ** 3)
        k = k + 1
    return somme

print(somme_cubes(1))