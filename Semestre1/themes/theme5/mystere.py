#Exercice 5.2 Question 1
def f(a: str)-> int:
    b: int = 0
    c: str
    for c in a:
        if c>= '0' and c <='9':
            b = b + 1 
            
    return b


