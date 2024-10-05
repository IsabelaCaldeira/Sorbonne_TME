import math 
#Exercice 3.5 Question 1
def fibonacci(n:int)->int:
    """Précondition n>=0
    Renvoie le n-iéme terme de la suite Fibonacci"""
   
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

assert fibonacci(3) == 2
     
#Exercice 3.5 Question 2   
assert fibonacci(8) == 21

#Exercice3.5 Question 3
def fibo_diff(n: int) -> float:
    """Préconditions: n >= 2
    Renvoie le k-ième de le terme n"""

    return fibonacci(n) / fibonacci(n-1)

assert fibo_diff(3) == 2
assert fibo_diff(2) == 1

#Exercice 3.5 Question 4
def fibo_approx(n: int) -> float:
    """Précondition n >= 5
    Renvoie le approximation de fibonacci 
    """
    
    return (((1 + math.sqrt(5)) / 2)**n)/math.sqrt(5)

assert 4 < fibo_approx(5) < 5