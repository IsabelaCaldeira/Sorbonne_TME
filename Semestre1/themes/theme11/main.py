import math
from typing import Callable, List, Tuple, T, U
#Exercice 11.4 Question 1
def f_fun(x: float) -> float:
    """Précondition:
    Approximation de la valeur de racine carrée de 2
    """
    return x**2 - 2

assert f_fun(3)==7

def f_deriv(x : float ) -> float:
    """Précondition:
    calcul la dérivée de f_fun(x)
    """
    return 2*x

assert f_deriv(3)==6

#Exercice 11.4 Question 2
def approx_newton(f : Callable[[float], float], df : Callable[[float], float], x0 : float, n : int) -> float:
    """calcule le n-ième terme de la suite
    """
    x_n : float = 0
    if n==0:
        return x0
    else:
        x_n=approx_newton(f,df,x0,n-1)
    return x_n-(f(x_n)/df(x_n))

assert approx_newton(f_fun, f_deriv, 1.0, 2)==1.4166666666666667
assert approx_newton(f_fun, f_deriv, 1.0, 5)==1.4142135623730951

#Exercice 11.4 Question 3
def approx_newton_it(f : Callable[[float], float], df : Callable[[float], float], x0 : float, n : int) -> float:
    """ cf. approx_newton """
    y : float = x0
    i : int
    for i in range(n):
        y = y - f(y)/df(y)
    return y

assert approx_newton_it(f_fun, f_deriv, 1.0, 2)==approx_newton(f_fun, f_deriv, 1.0, 2)

#Exercice 11.4 Question 4
def g(x:float)->float:
    """renvoie la fonction g(x)"""
    return math.cos(x)-x**3

assert g(3)==-27.989992496600447

def dg(x:float)->float:
    """renvoie la dérivée de g(x)"""
    return -math.sin(x)-3*x**2

assert dg(3)==-27.14112000805987

def resolution(n:int)->float:
    """donne le n-ième terme de l'approximation de Newton
    """
    return approx_newton(g,dg,0.5,n)

assert resolution(5)==0.8654740331109566

#Exercice 11.5 Question 1 
def f_fun(x: float) -> float:
    """Calculates f(x) = x^2 - 2"""
    return x**2 - 2

def f_deriv(x: float) -> float:
    """Calculates f'(x) = 2x"""
    return 2 * x

#Exercice 11.5 Question 2
def approx_newton(f: Callable[[float], float], df: Callable[[float], float], x0: float, n: int) -> float:
    """Calculates the n-th term of the sequence using Newton's method."""
    if n == 0:
        return x0
    else:
        x1 = x0 - f(x0) / df(x0)
        return approx_newton(f, df, x1, n - 1)

# Example usage
print(approx_newton(f_fun, f_deriv, 1.0, 2))  # Output: 1.4166666666666667
print(approx_newton(f_fun, f_deriv, 1.0, 5))  # Output: 1.4142135623730951

#Exercice 11.5 Question 3 
def approx_newton_it(f : Callable[[float], float], df : Callable[[float], float]
, x0 : float, n : int) -> float:
    """ cf. approx_newton """
    y : float = x0
    i : int
    for i in range(n):
        y = y - f(y)/df(y)
    return y

#Exercice 11.5 Question 4


#Exercice 11.6 Question 1
def fmap(f : Callable[[T], U], lst : List[T]) -> List[U]:
    """Retourne la liste des applications de f aux éléments de lst
    (schéma de transformation)
    """
    res : List[T] = []
    i : int
    for i in range(len(lst)):
        res.append(f(lst[i]))
    return res

def oppose(n : int) -> int:
    """Retourne l'opposé de n"""
    return -n
assert oppose(1)==-1
assert oppose(2)==-2

assert fmap(oppose, [1, 2, 3, 4, 5])==[-1, -2, -3, -4, -5]
assert fmap(len, ["un", "deux", "trois", "quatre", "cinq"])==[2, 4, 5, 6, 4]

#Exercice 11.6 Question 2
def fmap2(f : Callable[[T], U], lst : List[T]) -> List[U]:
    """Retourne la liste des applications de f aux éléments de lst
    (schéma de transformation)
    """
    return [f(lst[i]) for i in range(len(lst))]

assert fmap2(oppose, [1, 2, 3, 4, 5])==fmap(oppose, [1, 2, 3, 4, 5])
assert fmap2(len, ["un", "deux", "trois", "quatre", "cinq"])==fmap(len, ["un", "deux", "trois", "quatre", "cinq"])

#Exercice 11.6 Question 3
def ffilter(pred : Callable[[int],bool], lst : List[int])->List[int]:
    """construit la liste des seuls éléments de lst qui vérifient pred
    """
    res : List[int] = []
    i : int
    for i in range(len(lst)):
        if pred(lst[i]):
            res.append(lst[i])
    return res

def even(n : int) -> bool:
    """Retourne True ssi n est pair"""
    return n % 2 == 0
assert even(2)
assert not(even(1))

assert ffilter(even, [1, 2, 3, 4, 5, 6, 7])==[2, 4, 6]

def odd(n : int) -> bool:
    """Retourne True ssi n est impair"""
    return not(even(n))
assert odd(1)
assert not(odd(2))

#Exercice 11.6 Question 4
def ffilter2(pred : Callable[[int],bool], lst : List[int])->List[int]:
    """construit la liste des seuls éléments de lst qui vérifient pred
    """
    return [lst[i] for i in range(len(lst)) if pred(lst[i])]

assert ffilter2(even, [1, 2, 3, 4, 5, 6, 7])==ffilter(even, [1, 2, 3, 4, 5, 6, 7])

#Exercice 11.7 Question 1
def fzip(lst1 : List[T], lst2 : List[U]) -> List[Tuple[T, U]]:
    """Retourne la liste des couples formés par les éléments de lst1
    (premier élément du couple) et les éléments de lst2 (second élément).
    """
    lst3 : List[Tuple[T, U]] = []
    res : Tuple[T, U]
    i : int = 0
    while i < min(len(lst1),len(lst2)):
        res = lst1[i], lst2[i]
        lst3.append(res)
        i = i + 1
    return lst3

assert fzip([1, 3, 5], [2, 4, 6]) == [(1, 2), (3, 4), (5, 6)]
assert fzip(["un", "deux", "trois"], [1, 2, 3, 4]) == [('un', 1), ('deux', 2), ('trois', 3)]

#Exercice 11.7 Question 2
def funzip(lst : List[Tuple[T, U]]) -> Tuple[List[T], List[U]]:
    """Retourne un couple formé de la
    - la liste des premiers éléments de la liste lst,
    - la liste des seconds éléments de cette même liste
    """
    lst2 : List[T] = []
    lst3 : List[U] = []
    res : Tuple[List[T], List[U]]
    i : Tuple[T, U]
    for i in lst:
        a,b = i
        lst2.append(a)
        lst3.append(b)
        res = lst2, lst3
    return res

assert funzip([(1, 2), (3, 4), (5, 6)]) == ([1, 3, 5], [2, 4, 6])
assert funzip([("un", 1), ("deux", 2), ("trois", 3)]) == (['un', 'deux', 'trois'], [1, 2, 3])

#Exercice 11.7 Question 3
def inf(a : int, b : int) -> bool:
    """Indique si a < b"""
    return a < b

def plus(a : int, b : int) -> int:
    """Retourne a + b"""
    return a + b

def fzip_with(f:Callable[[T, T],U],lst1:List[V],lst2:List[V])->List[U]:
    """
    """
    lst : List[U] = []
    i : int
    for i in range(min(len(lst1),len(lst2))):
        lst.append(f(lst1[i],lst2[i]))
    
    return lst

assert fzip_with(plus, [1, 2, 3], [9, 8, 7]) == [10,10,10]
assert fzip_with(inf, [1, 2, 3], [3, 2, 1, 4]) == [True, False, False]
        
