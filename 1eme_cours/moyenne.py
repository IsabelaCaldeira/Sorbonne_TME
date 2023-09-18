def moyenne_trois_nb(nombre1: float, nombre2: float, nombre3: float) -> float :
    """ 
        Retourne la moyenne de trois nombres flotantes pour arriver à la moyenne 
    """
    return (nombre1 + nombre2 + nombre3)/3

assert moyenne_trois_nb(3, 6,-3) == 2
assert moyenne_trois_nb(-3, 0, 3) == 0
assert moyenne_trois_nb(1.5, 2.5, 1.0) == 5/3