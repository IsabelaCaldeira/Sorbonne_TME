#Exercice 1.5 Question 2
def celsius_vers_fahrenheit(t: float) -> float:
    """
    Convertir des Degrés Celsius à Fahrenheit
    """
    return t*9/5 + 32

assert celsius_vers_fahrenheit(100.0) == 212.0
assert celsius_vers_fahrenheit(0.0) == 32.0
assert celsius_vers_fahrenheit(5.0) == 41.0
    
