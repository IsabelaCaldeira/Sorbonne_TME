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
    
#Suggestion Test
def test_parfait(n : int):
    """Precondition: 0 < n <= 137438691328
    Renvoie le résultat de la fonction est parfait est cohérent avec la liste des sept premiers nombres parfaits pour tous les nombres entre 1 et n.
    """
    res = []
    k : int = 1
    while k <= n:
        if est_parfait(k):
            res = res," ", k
        k = k + 1             
             
    return res

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

#Question 3 


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

est_parfait_tableau(9)
assert est_parfait_fichier(6) == True
assert est_parfait_fichier(7) == False