#Exercice 2 Question 2
def sante(x : float) -> str:
    """Retourne Bonne santé si x vaut 37.5, retourne "Malade" sinon.
    """
    if x == 37.5: 
        return "Bonne santé"
    else:
        return "Malade"
    
assert sante(38) == "Malade"
assert sante(37.5) == "Bonne santé"

#*** La fonction comme l'enonce propose ne marche pas, à cause de ça le '=' de 'x = 37,5'
# était changé par 'x == 37,5" pour que la fonction donne la bonne response
#Le code vérifie si la condition de x est vrai et retourne des responses pour chaque condition

