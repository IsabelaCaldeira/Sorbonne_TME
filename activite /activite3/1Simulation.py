#Exercice 1 
def divise (k : int , n : int) -> bool :
    """ Pre : k > 0 and n > = 0
    Decide si k divise n """
    return n % k == 0

def est_parfait(n : int) -> bool :
    """ Pre : n > = 1
    Decide si n est un nombre parfait ."""
    s : int = 0
    i : int = 1
    while i != n :
        if divise (i, n):
            s = s + i
        i = i + 1
    return n == s

#Exercice 1 Question 1 
assert divise(7,21) == True
assert divise(27,7) == False
assert est_parfait(6) == True
assert est_parfait(7) == False


#Exercice Question 2 
def est_parfait_simulee(n : int) -> bool:
    """ Pre : n > = 1
    Decide si n est un nombre parfait ."""
    s : int = 0
    i : int = 1
    while i != n:
        if((s == 0) and (i == 1)):
            print("debut de boucle, s =", s)
            print("debut de boucle, i =", i)
            print("==============================")

        if divise(i, n):
            s = s + i
        i = i + 1
        print("fin du tour ", (i -1),", s =", s)
        print("fin du tour ", (i -1),", i =", i)
        print("==============================")

        if(i == n):
            print("sortie de boucle, s = ", s, "et n =", n)
            
    return n == s

assert est_parfait_simulee(6) == True
assert est_parfait_simulee(7) == False
    