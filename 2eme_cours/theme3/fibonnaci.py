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
        
#Exercice 3.5 Question 2
#Exercice3.5 Question 3
def fibo_diff(n: int) -> float:
    """Préconditions: n >= 2
    Renvoie le k-ième de le terme n"""

    i : float = 2
    while i >= n:
        return fibo_diff(n) / fibo_diff(n-1)        
print(fibo_diff(5))

    

    
    


