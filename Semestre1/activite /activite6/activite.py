import math
from typing import Tuple, List

Point = Tuple[float , float]
Courbe = List[Point]

O : Point = (0.0 , 0.0)
tri1 : Courbe = [O, (0.0 ,0.3) , (0.4 ,0.0) , O]

#Partie Guidée - Question 1
def distance_entre_points(point1: Point, point2: Point) -> float:
    """Calcule la distance entre deux points."""
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

p1 :Point= (0.0, 0.0)
p2 :Point= (3.0, 4.0)
assert distance_entre_points(p1, p2) == 5.0
assert distance_entre_points(p2, p1) == 5.0

def longueur_courbe (c:Courbe)-> float:
    """Retourne la longueur de la courbe c"""
    res :float = 0.0
    i:int
    for i in range(len(c)):
        res =res + distance_entre_points(c[i], c[i - 1])
    return res

assert abs((longueur_courbe (tri1) - 1.2)) < 10**(-12)

#Question 2 :
def segment(p1: Point, p2: Point) -> Image:
    """Renvoie une liste de points représentant le segment entre point1 et point2."""
    x1, y1 = p1
    x2, y2 = p2
    return draw_line(x1,y1,x2,y2, "purple")

#show_image(segment((0.0,0.0),(3.0,4.0)))

#Question 3 :
def image_courbe(c: Courbe) -> Image:
    """Renvoie l'image correspondant à la courbe en reliant les points par des segments."""
    i:int
    image :Image = segment((0,0),(0,0))
    for i in range(len(c)-1):
        image = overlay(image,segment(c[i], c[i + 1]))
    return image

#Question 4 :
def deplace(point: Point, direction: str, distance: float) -> Point:
    """Déplace le point dans la direction donnée d'une certaine distance.
distance =='H'or 'B'or 'G' or 'D'"""
    x, y = point
    new_point :Point
    if direction == "H":
        new_point = (x, y + distance)
    elif direction == "B":
        new_point = (x, y - distance)
    elif direction == "G":
        new_point = (x - distance, y)
    elif direction == "D":
        new_point = (x + distance, y)
    return new_point

assert deplace (O, "G", 1) == (-1.0, 0.0)
assert deplace (O, "H", 0.5) == (0.0 , 0.5)


#Question 5
def spirale (ori:Point, dec :float, n_tours : int)-> Image:
    """Retourne une image de spirale commencant au point ori"""
    point :Point=ori
    x1,y1=point
    res : Courbe = [ori]
    d:int=1
    i:int

    for i in range (n_tours):
        point=deplace(point,'H',dec+d*dec)
        res.append (point)
        d=d+1
        point=deplace(point,'G',dec+d*dec)
        res.append (point)
        d=d+1
        point=deplace(point,'B',dec+d*dec)
        res.append (point)
        d=d+1
        point=deplace(point,'D',dec+d*dec)
        res.append (point)
        d=d+1
    
    return image_courbe(res)


#Suggestion 2 flocon de Koch
def courbe_flocon(p : Point, r : float, n : int) -> Courbe:
    """Precondition : r > 0
    Renvoie la courbe correspondant au flocon de Koch à l'étape n"""
    p2 : Point = deplace(p, "H", r)
    p3 : Point = deplace(p, "B", r/2)
    tri : Courbe = [p2, deplace(p3, "G",r), deplace(p3, "D",r), p2]
    tri2 : Courbe = []

         
    tour : int
    for tour in range(n):
        i : int
        for i in range(len(tri) -1):
            x1,y1 = tri[i]
            x2 ,y2 = tri[i+1]
            x3 :float = x1 + 1/3*(x2 -x1)
            y3 :float = y1 + 1/3*(y2-y1)
            x4 :float = x1 + 2/3*(x2-x1)
            y4:float = y1 + 2/3*(y2-y1)
            p3 : Point = (x3+1/2*(x4-x3)+(3**0.5)/2*(y4-y3),y3+1/2*(y4 -y3) - (3** 0.5)/2*(x4-x3))
            tri2.append(tri[i])
            tri2.append((x3, y3))
            tri2.append(p3)
            tri2.append((x4,y4))
            tri2.append(tri[i+1])
        tri = tri2
        tri2 = []
                
    return tri

show_image(image_courbe(courbe_flocon(O,0.8,5)))
