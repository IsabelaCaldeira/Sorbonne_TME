from typing import List
#Partie Guidée : Le Tic-Tac-Toe
CaseT = str
# les elements de CaseT sont soit " " soit "O" soit "X"
PlateauT = List[List[CaseT]]
# les elements de PlateauT sont des matrices 3x3

#Question 1
def plateau_vide()->PlateauT:
    """Renvoie un plateau de jeu vide pour le tic-tac-toe
    """
    return [[" "," "," "],[" "," "," "],[" "," "," "]]

pla1 : PlateauT = plateau_vide()
assert pla1[1][1] == " "
assert pla1[0][2] == " "

#Question 2
def videt(pla:PlateauT,i:int,j:int)->bool:
    """Précondition : 0<=i<=2 et 0<=j<=2
    décide si la case de coordonnées (i,j) du plateau est vide
    """
    return pla[i][j]==" "

assert videt(pla1,1,1) == True
assert videt(pla1,0,2) == True

#Question 3
def jouex(pla:PlateauT,i:int,j:int)->None:
    """inscrie le symbole "X" dans la case de coordonnées (i,j)
    """
    pla[i][j] = "X"
    return None

def joueo(pla:PlateauT,i:int,j:int)->None:
    """inscrie le symbole "O" dans la case de coordonnées (i,j)
    """
    pla[i][j] = "O"
    return None

assert videt(pla1 , 0, 2) == True
assert jouex(pla1 , 1, 1) == None
assert joueo(pla1 , 0, 2) == None
assert videt(pla1 , 0, 2) == False

#Question 4
def dessine_plateaut(pla:PlateauT)->str:
    """Renvoie une chaîne de caractère correspondant à un affichage du plateau
    """
    res : str = "/---\\\n"
    i : int
    for i in range(len(pla)):
        j : int = 2
        while j>=0:
            if j==2:
                res = res + "|" + pla[i][j]
            elif j==1:
                res = res + pla[i][j]
            elif j==0:
                res = res + pla[i][j] + "|\n"
            j = j - 1
    return res + "\\---/"

assert dessine_plateaut(pla1) == '/---\\\n|O  |\n| X |\n|   |\n\\---/'
print(dessine_plateaut(pla1))

#Question 5
def gagnet(pla:PlateauT,s:str)->bool:
    """Précondition : s="X" ou s="O"
    Décide si le plateau est gagnant pour s
    """
    i : int
    for i in range(len(pla)):
        j : int
        for j in range(len(pla[i])):
            if pla[i][j]==s and pla[i+1][j]==s and pla[i+2][j]==s:
                return True
            elif j==0 and pla[i][j]==s and pla[i][j+1]==s and pla[i][j+2]==s:
                return True
            elif j==0 and pla[i][j]==s and pla[i+1][j+1]==s and pla[i+2][j+2]==s:
                return True
            elif j==2 and pla[i][j]==s and pla[i+1][j-1]==s and pla[i+2][j-2]==s:
                return True
        return False

assert gagnet([["O", " ", "X"], ["O", "X", " "], ["X", " ", " "]], "X") == True
assert gagnet([["O", " ", "X"], ["O", "X", " "], ["X", " ", " "]], "O") == False
assert gagnet([["X", " ", "O"], ["X", "O", " "], ["X", " ", " "]], "X") == True
assert gagnet([["X", " ", "O"], ["O", "X", " "], ["X", " ", " "]], "X") == False
assert gagnet([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]], "O") == True

