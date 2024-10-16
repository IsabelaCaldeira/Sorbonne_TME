import math 
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
            print("debut de boucle, s = ", s)
            print("debut de boucle, i = ", i)
            print("==============================")

        if divise(i, n):
            s = s + i
        i = i + 1
        print("fin du tour " (i -1),", s =", s)
        print("fin du tour ", (i -1),", i =", i)
        print("==============================")

        if(i == n):
            print("sortie de boucle, s = ", s, "et n =", n)
            
    return n == s

#assert est_parfait_simulee(6) == True
#assert est_parfait_simulee(7) == False
    
#2 Suggestion : Test
def test_parfait(n : int) -> bool:
    """Pre 0 < n < 137 438 691 329
    Renvoie si est_parfait est bonne"""

    if n == 6:
        return ((n == 6) == est_parfait(n))
    elif n == 28:
        return ((n == 28) == est_parfait(28))
    elif n == 496:
        return ((n == 496) == est_parfait(496))
    elif n == 8128:
        return (n == 33550336) == est_parfait(33550336)
    elif n == 8589869056:
        return (n == 8589869056) == est_parfait(8589869056)

    elif n == 137438691328:
        return (n ==137438691328) == est_parfait(137438691328)
    else:
        return  False == est_parfait(n)
    
assert test_parfait(6) == True
assert test_parfait(7) == True

#Suggestion 3 Invariant Question 1 et Question 2 
def est_parfait_invariant(n : int) -> bool :
    """ Pre : n > = 1
    Decide si n est un nombre parfait ."""
    i : int = 1
    s : int = 0

    while i != n :
        print("Valeur de l'invariant",s,"dans le début du boucle")
        print("========================================")
        if divise(i, n):
            s = s + i
        i = i + 1

    print("Valeur de l'invariant", s,"aprés le boucle")
    print("========================================")

    return n == s



#3 Suggestion Invariant Question 1
#On utilise l'invariant s avec sa condition: s est égal à la somme de tous les diviseurs de n inférieurs ou égaux à i-1
#Pour est_divisible(6)
#Boucle 1, s = 1 == (1)
#Boucle 2, s = 3 == (2 + 1)
#Boucle 3, s = 6 == (3 + 2 + 1)
#Boucle 4, s = 6 == (3 + 2 + 1)
#Boucle 5, s = 6 == (3 + 2 + 1)
#Boucle 6, s = 6 == (3 + 2 + 1)

#3 Suggestion Invariant Question 2 
def invariant(i: int, n:int, s:int) -> bool:
    """i > 0, n >= 0, s>= 0
    renvoie si l’invariant est vrai.
    """
    new_s : int = 0
    j : int = 1
    while j != i:
        if divise(j, n):
            new_s = new_s + j
        j = j + 1

    return s == new_s

assert invariant(6,6,6) == True

#Suggestion 3 Question 3 
def est_parfait_invariant(n : int) -> bool :
    """ Pre : n > = 1
    Decide si n est un nombre parfait ."""
    i : int = 1
    s : int = 0

    while i != n :
        if(invariant(i, n, s)):
            print("Invariant vrai")
        if divise(i, n):
            s = s + i
        if(invariant(i, n, s)):
            print("Invariant vrai")
        i = i + 1

    return n == s

#Suggestion 4 Tableau de Simulation 
def est_parfait_fichier(n:int) -> bool:
    """ Pre : n > = 1
     Renvoie le même resultat que est_parfait et affiche dans un fichier"""
    s : int = 0
    i : int = 1
    
    with open("parfaitFichier.txt", "w") as fichier:
        while i != n:
            if((s == 0) and (i ==1)):
                  fichier.write("Debut de boucle, s=" + str(s) +"\nDebut de boucle, i=" + str(i)+"\n=============================\n")

            if divise(i, n):
                s = s + i
            i = i + 1
    
            fichier.write("\nFin du tour" + str(i - 1) + " s=" + str(s) + " Fin du tour " + str(i -1) + " i=" +str(i))
            
            if(i == n):
                fichier.write("\n=============================\n"+"\nSortie de boucle s = " + str(s) + " et n= " + str(n))
        fichier.close()
    return n == s

assert est_parfait_fichier(6) == True
assert est_parfait_fichier(7) == False

#Question 2 
def est_parfait_tableau(n : int)-> bool:
    """ Pre : n > = 1
     Renvoie le même resultat que est_parfait_fichier, mais sur un tableau"""
    s : int = 0
    i : int = 1
    
    with open("parfaitTableau.txt", "w") as fichier:
        if n < 10:
            fichier.write("==================================================\n|            Simulation est_parfait("+str(n)+")           |\n==================================================\n|      tour       |       i       |      s       |\n==================================================")
        elif n < 100 and n > 10:
            fichier.write("==================================================\n|            Simulation est_parfait("+str(n)+")          |\n==================================================\n|      tour       |       i       |      s       |\n==================================================")
        else:
            fichier.write("==================================================\n|            Simulation est_parfait("+str(n)+")         |\n==================================================\n|      tour       |       i       |      s       |\n==================================================")

        while i != n:
            if((s == 0) and (i ==1)):
                  fichier.write("\n| entree          |             1 |            0 |\n==================================================\n")
            if divise(i, n):
                s = s + i
            i = i + 1
            if (i-1<10) and (i<10) and (s<10) and not (i == n):
                fichier.write("| tour "+str(i-1)+ "          |             "+str(i)+" |            "+str(s)+" |\n==================================================\n")
            elif(i-1<10) and (i<10) and (s>=10) and not (i == n):
                fichier.write("| tour "+str(i-1)+ "          |             "+str(i)+" |           "+str(s)+" |\n==================================================\n")
            elif (i-1<10) and (i>=10) and (s<10) and not (i == n):
                fichier.write("| tour "+str(i-1)+ "         |           "+str(i)+" |           "+str(s)+" |\n==================================================\n")
            elif (i-1<10) and (i>=10) and (s>=10) and not (i == n):
                fichier.write("| tour "+str(i-1)+ "          |            "+str(i)+" |           "+str(s)+" |\n==================================================\n")
            elif (i-1<100) and (i-1>=10) and (s>=100) and not (i == n):
                fichier.write("| tour "+str(i-1)+ "         |            "+str(i)+" |          "+str(s)+" |\n==================================================\n")
            elif(i == n):
                if(n<10):
                    fichier.write("| tour "+str(i -1)+ "  (sortie)|             "+str(i)+" |            "+str(s)+" |\n==================================================")
                elif(n>=10) and (n<100) and (i>=10) and (s < 10) :
                    fichier.write("| tour "+str(i -1)+ "  (sortie)|            "+str(i)+" |            "+str(s)+" |\n==================================================")
                elif(n>10) and (n-1<100) and (i<100) and (s>=100):
                    fichier.write("| tour "+str(i -1)+ " (sortie)|           "+str(i)+" |           "+str(s)+" |\n==================================================")
                elif(n>10) and (n-1<100) and (i<100) and (s>=100):
                    fichier.write("| tour "+str(i -1)+ " (sortie)|           "+str(i)+" |           "+str(s)+" |\n==================================================")
                elif(n>10) and (n-1<100) and (i>= 100) and (s>=100):
                    fichier.write("| tour "+str(i -1)+ " (sortie)|           "+str(i)+" |          "+str(s)+" |\n==================================================")
        fichier.close()
    return n == s

est_parfait_tableau(100)
assert est_parfait_fichier(6) == True
assert est_parfait_fichier(7) == False

#5 Suggestion : Comparaison de complexité
#Question 1
def est_parfait_appels(n : int) -> bool :
    """ Pre : n >= 1
    Decide si n est un nombre parfait et affiche le nombre d'appels à divise."""
    i : int = 1
    s : int = 0
    count : int = 0

    while i != n :
        count += 1
        if divise(i, n):
            s = s + i
        i = i + 1

    print(f"{count} appels à la fonction divise.")
    return n == s


assert est_parfait_appels(100) == False

#Question 2
def est_parfait_opti(n : int) -> bool :
    """ Pre : n >= 1
    Decide si n est un nombre parfait """
    s : int = 1
    i : int = 2
    if i == 1:
        return False
    while i != int(math.sqrt(n)) + 1 :
        if divise(i, n):
            if i != math.sqrt(n) :
                s = s + i + (n // i)
            else :
                s = s + i
        i = i + 1
    return n == s

assert est_parfait_opti(100)==False

#Suggestion 5 Question 2
def est_parfait_opti_appels(n:int)->int:
    """Précondition : n>=1
    compte le nombre d'appel à divise que fait la fonction est_parfait_opti
    """
    i: int = 2
    s: int = 1
    count: int = 0
    while i != int(math.sqrt(n)) + 1 :
        count = count+1
        if divise(i, n):
            if i != math.sqrt(n) :
                s = s + i + (n // i)
            else :
                s = s + i
        i=i+1
    print(count,"appels à la fonction divise dans la fonction est_parfait_opti_appels \n")
    return count

assert est_parfait_opti_appels(100) == 9

#Question 3
def est_parfait_appels_comparer(n : int) -> int :
    """ Pre : n >= 1
    Affiche le nombre d'appels à divise."""
    i : int = 1
    s : int = 0
    count : int = 0

    while i != n :
        count += 1
        if divise(i, n):
            s = s + i
        i = i + 1

    return count

def comparer(n:int)->bool:
    """précondition : n>=1
    Estime combien d'appels à divise sont faits lors de l'évaluation de est_parfait(n) et de est_parfait_opti(n) en fonction de n.
    """
    return est_parfait_opti_appels(n)<est_parfait_appels(n)

assert comparer(100)==True

#Suggestion 5 Question 4
def image(n:int)->Image:
    """précondition : 1<=n<=200
    produit une image qui représente les courbes du nombre d'appels à divise des deux fonctions (est_parfait(n) et est_parfait_opti(n)), en fonction de n
    """
    return (overlay(draw_line(-1,-1,n,float(est_parfait_appels(n))),draw_line(-1,-1,n,float(est_parfait_appels_comparer(n)))))    

#show_image(image(100))

#6 Suggestion : D'autres fonctions
def celsius_vers_fahrenheit(t : float)->float:
    """Précondition : t>=-273,15°C
    Convertir des Degrés Celsius à Fahrenheit
    """
    return t*9/5 + 32

assert celsius_vers_fahrenheit(100.0) == 212.0
assert celsius_vers_fahrenheit(0.0) == 32.0

def fahrenheit_vers_celsius(t: float) -> float:
    """Précondition : 
    Convertir des Degrés Fahrenheit à Celsius
    """
    return (t-32)*5/9

assert fahrenheit_vers_celsius(212) == 100.0
assert fahrenheit_vers_celsius(32) == 0.0

def temperature(t: float) -> bool:
    """
    Vérifie la validité des deux fonctions précédentes
    """
    return celsius_vers_fahrenheit(fahrenheit_vers_celsius(t))==fahrenheit_vers_celsius(celsius_vers_fahrenheit(t))

assert temperature(100.0)==True
assert temperature(212)==True