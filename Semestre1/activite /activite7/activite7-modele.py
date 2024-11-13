#Chemins et Labyrinthes 
from typing import Tuple, List

Coord = Tuple[int, int]
Dir = str

#Partie Guidée Question 1 
ori : Coord = (0, 0)
p1 : Coord = (3, 3)
p2 : Coord = (0, 2)

def deplace(c : Coord, d: Dir) -> Coord:
    """Précondition d est soit "N", soit "S", soit "E", soit "O"
    Renvoie les coordonnées de la case dans laquelle on se trouve après un déplacement dans la direction
d depuis la case de coordonnées c.
    """
    x, y =  c
    res : Coord 
    if d == "N":
        res = (x,y+1)
    elif d == "S":
        res = (x,y-1)
    elif d == "E":
        res = (x+1,y) 
    else:
        res = (x-1,y)

    return res

assert deplace (ori , "N") == (0, 1)
assert deplace (p1 , "E") == (4, 3)
assert deplace ( deplace (p2 , "N"), "S") == p2
        
#Partie Guidée Question 2
def deplace_chemin(c : Coord, ch:List[Dir]) -> Coord:
    """Renvoie les coordonnées de la case dans laquelle on arrive après avoir suivi toutes les directions de ch dans l'ordre
    """
    if ch == []:
        return c
    
    d : str = ch[0]    

    res : Coord =  deplace(c, d)   
    return deplace_chemin(res, ch[1:])

assert deplace_chemin (ori , ["N", "N"]) == p2
assert deplace_chemin (ori , ["N", "E", "S", "O"]) == ori
assert deplace_chemin (ori , []) == ori

#Partie Guidée Question 3
Case = Tuple [bool ,bool ,bool ,bool ,str]
Laby = List[List[Case ]]
laby1 : Laby = [[( True , True , False , False , ""),
                ( False , False , True , False , "ENTREE")],
                [( True , False , False , True , ""),
                ( False , False , True , False , "SORTIE")]]

laby2 : Laby = [[( True , False , False , False , ""),
                ( False , True , True , False , ""),
                (True , True , False , False , ""),
                ( False , False , True , False , " ENTREE ")],
                [( False , False , False , False , ""),
                (True , True , False , True , ""),
                (True , False , True , True , ""),
                ( False , True , True , False , "")],
                [( True , False , False , False , ""),
                ( False , False , True , True , ""),
                (True , True , False , False , ""),
                ( False , False , True , True , "")],
                [( True , False , False , False , " SORTIE "),
                (True , False , True , False , ""),
                (True , False , True , True , ""),
                (False , False , True , False , "")]
                ]

def deplace_possible(la:Laby,c:Coord,d:Dir)->bool:
    """Précondition : d="N" or d="S" or d="E" or d="O"
    décide si le déplacement depuis c dans la dans la direction d est possible
    """
    x,y = c
    (n,e,s,o,nat)=la[x][y]
    if (n and (d=='N')):
        return True
    elif (e and (d=='E')):
        return True
    elif (s and (d=='S')):
        return True
    elif (o and (d=='O')):
        return True
    else: 
        return False 

assert deplace_possible(laby1 , (0, 1), "S")
assert not(deplace_possible(laby1 , (0, 1), "N"))
assert not(deplace_possible(laby1 , (0, 1), "E"))
#Question 4
def chemin_possible(la:Laby,c:Coord,ch:List[Dir])->bool:
    """décide si l'iténaire partant de la case de coordonnées c dans la et suivant le chemin ch est possible
    """
    if ch==[]:
        return True
    d : Dir = ch[0]
    if deplace_possible(la,c,d):
        return chemin_possible(la,deplace(c,d),ch[1:])

assert chemin_possible(laby1 , (0, 1), ["S", "E", "N"])
assert chemin_possible(laby1 , (0, 1), ["S", "N", "S", "E", "N"])
assert not(chemin_possible(laby1 , (0, 1), ["S", "O"]))
assert not(chemin_possible(laby1 , (0, 1), ["S", "E", "N", "O"]))

#Question 5
def est_solution(la:Laby,c:Coord,ch:List[Dir])->bool:
    """décide si oui ou non le couple (c,ch) est une solution du labyrinthe la
    """
    x,y = c
    _,_,_,_,nat = la[x][y]
  
    if ((nat == 'ENTREE') and (chemin_possible(la,c,ch))):
        u,v = deplace_chemin(c,ch)
        _,_,_,_,nat1 = la[u][v]
        
        if nat1 =="SORTIE":
            return True
        else:
            return False

assert est_solution(laby1,(0, 1),["S", "E", "N"])
assert est_solution(laby1,(0, 1),["S", "E", "O", "E", "N"])
assert not(est_solution(laby1,(0, 0),["E", "N"]))
assert not(est_solution(laby1,(0, 1),["S", "E"]))
assert not(est_solution(laby1 , (0, 1), ["E"]))


#3 Suggestion : Main droite
def droite(la:Laby,c:Coord,ch:List[Dir])->List[Dir]:
    """Précondition : len(ch)==0 et c est l'entrée
    Trouve un chemin ch du labyrinthe la qui relie la case de départ c à la case d'arrivée
    """
    x,y = c
    _,_,_,_,nat = la[x][y]
    tab_coord : List[Dir] = ["N","E","S","O","N","E","S"]
    if ((nat=="ENTREE") and (len(ch)==0)):

        if deplace_possible(la,c,"E"):
            new_c : Coord = deplace(c,"E")
            return droite(la,new_c,ch+["E"])

        elif deplace_possible(la,c,"N"):
            new_c : Coord = deplace(c,"N")
            return droite(la,new_c,ch+["N"])

        elif deplace_possible(la,c,"O"):
            new_c : Coord = deplace(c,"O")
            return droite(la,new_c,ch+["O"])
        
        else:
            new_c : Coord = deplace(c,"S")
            return droite(la,new_c,ch+["S"])
        
    elif nat == "SORTIE":
        return ch
    
    else:
        indice : int
        if ch[-1] == "N":
            indice = 0
        elif ch[-1] == "E":
            indice = 1
        elif ch[-1] == "S":
            indice = 2
        else:
            indice = 3

        dir_devant : Dir = ch[-1]
        dir_droite : Dir = tab_coord[indice+1]
        dir_gauche : Dir = tab_coord[indice+3]
        dir_derriere : Dir = tab_coord[indice+2]

        if deplace_possible(la,c,dir_droite):
            new_c : Coord = deplace(c,dir_droite)
            return droite(la,new_c,ch+[dir_droite])

        elif deplace_possible(la,c,dir_devant):
            new_c : Coord = deplace(c,dir_devant)
            return droite(la,new_c,ch+[dir_devant])

        elif deplace_possible(la,c,dir_gauche):
            new_c : Coord = deplace(c,dir_gauche)
            return droite(la,new_c,ch+[dir_gauche])
        
        else:
            new_c : Coord = deplace(c,dir_derriere)
            return droite(la,new_c,ch+[dir_derriere])

assert droite(laby1,(0,1),[]) == ['S', 'E', 'N']
assert droite(laby2,(0,3),[]) == ['S', 'E', 'S', 'O', 'S', 'N', 'E', 'E', 'S', 'N', 'O', 'N', 'N', 'E', 'S', 'E', 'S', 'S']
