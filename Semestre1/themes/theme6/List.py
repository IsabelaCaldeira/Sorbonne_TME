#Exercice 6.6
#Question 1 
def somme(L):
    i: int 
    for i in range(): 
#Exercice 6.9
#Question 2 
def separation(s: str, c: str):
    L = []
    s2 : str = ""
    
    i : int
    for i in range(len(s)):
        if s[i] != c:
            s2 += s[i]
            print(s[i])
        else:
            L.append(s2)
            s2 = ""
    L.append(s2)
    
    print(L)
    return L

assert separation("un.deux.trois.quatre", ".") == ['un', 'deux', 'trois', 'quatre']