#Exercice 1.5 Question 1
def fahrenheit_vers_celsius(t: float) -> float:
    """
    Convertir des Degrés Fahrenheit à Celsius
    """
    return (t-32)*5/9

assert fahrenheit_vers_celsius(212) == 100.0
assert fahrenheit_vers_celsius(32) == 0.0
assert fahrenheit_vers_celsius(41) == 5.0
