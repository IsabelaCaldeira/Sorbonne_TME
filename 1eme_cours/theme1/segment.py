#Exercice 1.9
def segment(x0: float, y0:float, x1:float, y1:float)-> Image:
    """Construit l'image d'un segment (x0, y0) et (x1, y1)"""
    d = draw_line(x0,y0,x1,y1)
    return show_image(d)