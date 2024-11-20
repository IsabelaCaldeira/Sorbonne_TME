from typing import List, Tuple, Dict, Optional

def ouvre_fichier(nom:str)->List[str]:
    """renvoie la liste des lignes du fichier texte ./nom.csv
    """
    with open("./"+nom+".csv", "r") as f:
        return f.readlines()

#Partie Guidée : Extraction d'information
exemple1 : List[str] = ['"sport";"date";"participants";"vainqueur"\n',
                        '"boxe";2021-09-18;12;"Alice"\n',
                        '"boxe";2021-09-25;10;"Alice"\n',
                        '"karate";2021-09-26;19;"Carole"\n',
                        '"boxe";2021-10-02;8;"Bob"\n',
                        '"karate";2021-10-03;20;"Carole"\n',
                        '"tennis";2021-10-04;3;"Alice"\n',
                        '"boxe";2021-10-09;5;"Alice"\n',
                        '"karate";2021-10-10;20;"Damien"\n',
                        '"boxe";2021-10-16;6;"Carole"\n',
                        '"echecs";2021-09-17;120;"Bob"\n',
                        '"echecs";2021-09-24;120;"Bob"\n',
                        '"echecs";2021-10-01;120;"Carole"\n']

#Partie Guidée Question 1
def decompose_ligne(li:str,sep:str)->List[str]:
    """Précondition : len(sep)=1
    Renvoie la liste des différentes sous-chaînes de la ligne qui se trouve entre les sep
    """
    res : List[str] = []
    temp : str =''
    i : str
    for i in li:
        if ((i!=sep) and (i!='\n')):
            temp = temp + i
        else:
            res.append(temp)
            temp = ''
        
    return res

assert decompose_ligne(exemple1[0], ";")==['"sport"', '"date"', '"participants"', '"vainqueur"']
assert decompose_ligne(exemple1[3], ";")==['"karate"', '2021-09-26', '19', '"Carole"']
assert decompose_ligne(exemple1[3], ",")==['"karate";2021-09-26;19;"Carole"']

#Partie Guidée Question 2
def enleve_guillemets(s:str)->str:
    """Renvoie s sans les guillemets ""
    """
    res : str = ''
    i : str
    for i in s:
        if i!='"':
            res = res + i
    return res

assert enleve_guillemets('"sport"') == 'sport'
assert enleve_guillemets('sport') == 'sport'

#Partie Guidée Question 3
def enleve_guillemets_ligne(li:List[str])->List[str]:
    """Précondition : li!=[]
    Renvoie la liste correspondant à li dans laquelle on a enlevé les guillements ""
    """
    return [enleve_guillemets(i) for i in li]

assert enleve_guillemets_ligne(['"sport"', '"date"', '"participants"', '"vainqueur"'])==['sport', 'date', 'participants', 'vainqueur']
assert enleve_guillemets_ligne(['"karate"', '2021-09-26', '19', '"Carole"'])==['karate', '2021-09-26', '19', 'Carole']

#Partie Guidée Question 4
def lignes_propres(lis:List[str],sep:str)->List[List[str]]:
    """Précondition : len(sep)=1
    renvoie la décomposition de chacune des lignes de lis dans laquelle on a enlevé les guillemets qui entoure chaque élément
    """
    return [enleve_guillemets_ligne(decompose_ligne(i,sep)) for i in lis]

assert lignes_propres(exemple1,";")==[['sport', 'date', 'participants', 'vainqueur'],
                                      ['boxe', '2021-09-18', '12', 'Alice'],
                                      ['boxe', '2021-09-25', '10', 'Alice'],
                                      ['karate', '2021-09-26', '19', 'Carole'],
                                      ['boxe', '2021-10-02', '8', 'Bob'],
                                      ['karate', '2021-10-03', '20', 'Carole'],
                                      ['tennis', '2021-10-04', '3', 'Alice'],
                                      ['boxe', '2021-10-09', '5', 'Alice'],
                                      ['karate', '2021-10-10', '20', 'Damien'],
                                      ['boxe', '2021-10-16', '6', 'Carole'],
                                      ['echecs', '2021-09-17', '120', 'Bob'],
                                      ['echecs', '2021-09-24', '120', 'Bob'],
                                      ['echecs', '2021-10-01', '120', 'Carole']]

#Partie Guidée Question 5
def cherche_indice(e:str,li:List[str])->Optional[int]:
    """Précondition : len(e)=1 et li!=[]
    renvoie le premier indice de li auquel apparaît e si c'est le cas, et None sinon
    """
    i : int
    for i in range(len(li)):
        if li[i]==e:
            return i
        
assert cherche_indice("sport", ['sport', 'date', 'participants', 'vainqueur'])==0
assert cherche_indice("vainqueur", ['sport', 'date', 'participants', 'vainqueur'])==3
assert cherche_indice("deces", ['sport', 'date', 'participants', 'vainqueur'])==None

#Partie Guidée Question 6
def dictionnaire_compte(lis:List[List[str]],clef:str)-> Dict[str,int]:
    """Précondition : lis!=[]
    Renvoie un dictionnaire dont les clefs sont les données de la colonne clef du fichier et les valeurs sont leur nombre d'occurences
    """
    res : Dict[str,int] = dict()
    indice : Optional[int] = cherche_indice(clef,lis[0])
    i : int
    
    for i in range(1,len(lis)):
        if lis[i][indice] in res:
            res[lis[i][indice]] = res[lis[i][indice]] + 1
        else:
            res[lis[i][indice]] = 1
    return res
        
lignes_ex1 : List[List[str]] = lignes_propres(exemple1 , ";")

assert dictionnaire_compte(lignes_ex1 , "vainqueur")=={'Alice': 4, 'Carole': 4, 'Bob': 3, 'Damien': 1}
assert dictionnaire_compte(lignes_ex1 , "sport")=={'boxe': 5, 'karate': 3, 'tennis': 1, 'echecs': 3}

#Partie Guidée Question 7
def dictionnaire_somme(lis:List[List[str]],clef:str,valeur:str)->Dict[str,int]:
    """Précondition : lis!=[]
    Renvoie un dictionnaire dont les clefs sont les données de la colonne clef du fichier et la valeur associée à la clef k est la somme des données de la colonne valeur des lignes où k apparaît dans la colonne clef
    """
    res : Dict[str,int] = dict()
    indice_clef : int = 0
    indice_valeur : int = 0
    
    i : int
    for i in range(len(lis[0])):
        if lis[0][i]==clef:
            indice_clef = i
        elif lis[0][i]==valeur:
            indice_valeur = i
    
    j:int
    for j in range(1,len(lis)):
        if lis[j][indice_clef] not in res:
            res[lis[j][indice_clef]] = int(lis[j][indice_valeur])
        else:
            res[lis[j][indice_clef]] = int(res[lis[j][indice_clef]]) + int(lis[j][indice_valeur])
    
    return res

assert dictionnaire_somme(lignes_ex1,"sport","participants")=={'boxe': 41, 'karate': 59, 'tennis': 3, 'echecs': 360}

#Partie Guidée Ensuite 
def tri_dico(dico:Dict[str,int])-> List[Tuple[str,int]]:
    """PreDico != vide
    Renvoie la façon decroissant des valeurs du dictionnaire"""
    list_dico : List[Tuple[str,int]] = [(k, v) for k, v in dico.items()]
    
    for i in range(1,len(list_dico)):
        cle : Tuple[str,int] = list_dico[i]
        j : int = i-1 
        cle0, cle1 = cle
        cle0j, cle1j = list_dico[j]
        while j >= 0 and cle1 > cle1j:
            list_dico[j+1] = list_dico[j]
            j = j - 1
            cle0j_temp, cle1j_temp = list_dico[j]
            cle1j = cle1j_temp
            list_dico[j+1] = cle
    return list_dico


def classement(dico:Dict[str,int])-> str:
    """Renvoie un classement des vainqueurs"""
    list_dec: List[Tuple[str, int]] = tri_dico(dico)
    temp : int = 0
    res : str = ''
    compt : int = 1
    for personne, victories in list_dec:
        if victories == temp and compt != 1:
            res = res + ' et '+ personne 
        if compt == 1:
            res = '1° place ' + personne
            compt = compt + 1
            temp = victories
        if victories != temp:
            temp = victories
            res = res + '\n' + str(compt) + '° place ' + personne 
            compt = compt + 1
            
    return res

print(classement(dictionnaire_compte(lignes_ex1 , "sport")))

#2 Suggestion : Courbes temporelles
def annee(date:str)->List[int]:
    """Précondition : date est sous la forme année-moi-jour
    Renvoie date sous forme de liste
    """
    c : str = ''
    i : str
    res : List[int] = []
    for i in date:
        if i == '-':
            res.append(int(c))
            c = ''
        else:
            c = c + i
    res.append(int(c))
    return res

assert annee('2021-10-01')==[2021, 10, 1]
assert annee('2021-09-25')==[2021, 9, 25]

def jours(date:str,date_ini:str)->int:
    """Précondition : On suppose que 1 mois est constitué de 30 jours et 1 an de 365 jours et date et date_ini sont de la forme année-moi-jour
    Renvoie le nombre de jours qui séparent date et date_ini
    """
    l_date : List[int] = annee(date)
    l_date_ini : List[int] = annee(date_ini)
    
    ann : int = l_date[0]
    mois : int = l_date[1]
    jour : int = l_date[2]
    
    ann_ini : int = l_date_ini[0]
    mois_ini : int = l_date_ini[1]
    jour_ini : int = l_date_ini[2]

    calcul : int = 30 - jour_ini + jour + ((mois - mois_ini - 1)%12)*30
    
    if ann == ann_ini:
        if mois == mois_ini:
            return jour - jour_ini
        else:
            return calcul
    
    else:
        if mois == mois_ini:
            return jour - jour_ini + (ann - ann_ini)*365
        else:
            return calcul + (ann - ann_ini - 1)*365

assert jours('2021-10-01','2021-09-25')==6
assert jours('2021-09-18','2021-10-10')==338

def convertir_dico(dico:Dict[str,int])->Dict[int,int]:
    """Convertit un dictionnaire associant date et valeur en dictionnaire associant durée depuis la première date du dictionnaire et valeur
    """
    date : str
    res : Dict[int,int] = dict()
    for (date,valeur) in dico.items():
        c : str = date
        res[jours(c,next(iter(dico)))] = valeur
    return res


def convertir_tuple(dico:Dict[str,int])->List[Tuple[int,int]]:
    """Convertit le dictionnaire en une liste d’associations
    """
    d : Dict[int,int] = convertir_dico(dico)
    return [(clef,valeur) for clef,valeur in d.items()]

def trier(l: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
    """On trie maintenant la liste d'association
    """
    temp : Tuple[int,int]
    i : int
    for i in range(len(l)):
        j : int
        for j in range(0, len(l)-i-1):
            x,y = l[j]
            x1,y1 = l[j+1]
            if x > x1:
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp
    return l



'''def trace(l : List[Tuple[int, int]]) -> Image :
    """On trace maintenant le grafique representant l'affluence aux tournois"""
    dur : List[int] = [m for m,_ in l]
    nb : List[int] = [t for _,t in l]
    a1 : int = dur[0]
    a2 : int = dur[-1]
    b1 : int = nb[0]
    b2 : int = nb[0]
    i : int
    for i in nb:
        if i > b1:
            b1 = i
        elif i<b2:
            b2 = i
    e1 : int = a2 - a1
    e2 : int = b1 - b2
    j : int
    image : Image = draw_line(0,0,0,0)
    for j in range(len(l)-1) :
        x1, y1 = l[j]
        x2, y2 = l[j+1]
        x1bis : float = 2*((x1 - a1)/e1) - 1
        x2bis : float = 2*((x2 - a1)/e1) - 1
        y1bis : float = 2*((y1 - b2)/e2) - 1
        y2bis : float = 2*((y2 - b2)/e2) - 1
        image = overlay(image, draw_line(x1bis,y1bis,x2bis,y2bis))
    return image

donnees : List[Tuple[int, int]] = trier(convertir_tuple(dictionnaire_somme(lignes_propres(exemple1 , ";"),"date","participants")))

#show_image(trace(donnees))'''