#1 Partie Guidée : Occurance des mots
def ouvre_fichier(nom:str)->List[str] :
    """ renvoie la liste des lignes du fichier texte ./nom.txt
    """
    with open(nom+".txt", "r", encoding = "utf-8") as f:
        return f.readlines()

exemple1 : List[str] = ['Je suis belle, ô mortels ! comme un rêve de pierre,\n',
                                                                                         "Et mon sein, où chacun s'est meurtri tour à tour,\n",
                                                                                         'Est fait pour inspirer au poète un amour\n',
                                                                                         'Éternel et muet ainsi que la matière.\n',
                                                                                         '\n',
                                                                                         "Je trône dans l'azur comme un sphinx incompris ;\n",
                                                                                         "J'unis un coeur de neige à la blancheur des cygnes ;\n",
                                                                                         'Je hais le mouvement qui déplace les lignes,\n',
                                                                                         'Et jamais je ne pleure et jamais je ne ris.\n',
                                                                                         '\n',
                                                                                         'Les poètes, devant mes grandes attitudes,\n',
                                                                                         "Que j'ai l'air d'emprunter aux plus fiers monuments,\n",
                                                                                         "Consumeront leurs jours en d'austères études ;\n",
                                                                                         '\n',
                                                                                         "Car j'ai, pour fasciner ces dociles amants,\n",
                                                                                         'De purs miroirs qui font toutes choses plus belles :\n',
                                                                                         'Mes yeux, mes larges yeux aux clartés éternelles !']

assert ouvre_fichier('C:/Data/Etudes/Licence/L1/Semestre 1/INO11/Activités/'+'beaute')==exemple1

#Question 1
def decompose_ligne(li:str,sep:Set[str])->List[str]:
    """Renvoie une liste de chaînes de caractères correspondant au découpage de li selon le caractère sep
    """
    res : List[str] = []
    mot : str = ""
    
    i : str
    for i in li:
            if ((i not in sep) and (i!="\n")):
                mot = mot + i
            else:
                res.append(mot)
                mot = ""
    return [j for j in res if j!=""]

ponctuation : Set[str] = {" ", ",", ";", "'", "(", ")", ".", "!", "?", ":"}

assert decompose_ligne(exemple1[0], ponctuation)==['Je', 'suis', 'belle', 'ô', 'mortels', 'comme', 'un', 'rêve', 'de', 'pierre']
assert decompose_ligne(exemple1[4], ponctuation)==[]
assert decompose_ligne(exemple1[8], ponctuation)==['Et', 'jamais', 'je', 'ne', 'pleure', 'et', 'jamais', 'je', 'ne', 'ris']

#Question 2
def minusculise(m:str)->str:
    """Précondition : m!=''
    Renvoie une chaîne de caractère correspondant à m dans lequel toutes les lettres romaines majuscules sont converties en minuscules
    """
    res : str = ''
    i : str
    for i in m:
        if ((ord(i)>=65) and (ord(i)<=90)):
            res = res + chr(ord(i)+32)
        else:
            res = res + i
    return res

assert minusculise("bonjour")=="bonjour"
assert minusculise("BONJOUR")=="bonjour"
assert minusculise("Bonjour")=="bonjour"

#Question 3
def mots(lis:List[str],sep:Set[str])->List[str]:
    """Précondition : lis!=[] et sep!={}
    Renvoie le liste des sous-chaînes déparées par des éléments de sep des éléments de lis, converties en minuscules
    """
    return [minusculise(j) for i in range(len(lis)) for j in decompose_ligne(lis[i],sep)]

assert mots(exemple1 , ponctuation )[:15]==['je', 'suis', 'belle', 'ô', 'mortels', 'comme', 'un', 'rêve', 'de', 'pierre', 'et', 'mon', 'sein', 'où', 'chacun']

#Question 4
def dictionnaire_occ_mots(ms:List[str])->Dict[str,int]:
    """Précondition : ms!=[]
    Construit le dictionnaire des occurences des mots de ms
    """
    res : Dict[str,int] = dict()
    i : str
    for i in ms:
        if i in res:
            res[i] = res[i] + 1
        else:
            res[i] = 1
    return res

dico1 : Dict[str, int] = dictionnaire_occ_mots(mots(exemple1 , ponctuation))
assert dico1["je"]==5
assert dico1["belle"]==1

#Question 5
def hapax(occ:Dict[str,int])->Set[str]:
    """Précondition : occ!={}
    Renvoie l'ensemble des hapx de occ
    """
    res : Set[str] = set()
    i : str
    for i in occ:
        if occ[i]==1:
            res.add(i)
    return res

assert len(hapax(dico1))==67
assert ("sphinx" in hapax(dico1))==True
assert ("jamais" in hapax(dico1))==False

#Question 6
def plus_frequent(occ:Dict[str,int])->str:
    """Précondition : occ!={}
    Renvoie un des mots (le premier dans l'ordre du dictionnaire) avec le nombre d'occurences le plus élevé
    """
    max_mot :str= ''
    max_occurrence :int= 0
    mot:str

    for mot in occ:
        if occ[mot] > max_occurrence:
            max_mot = mot
            max_occurrence = occ[mot]

    return max_mot

assert plus_frequent(dico1)=="je"

#2 Suggestion: Comparaison de fréquences
#Question 1
def dictionnaire_freq_mots(ms:List[str])->Dict[str,float]:
    """Construit un dictionnaire des fréquences des mots dans la liste ms
    """    
    occurences : Dict[str,int] = dictionnaire_occ_mots(ms)
    longueur : int = len(ms)
    freq_mots : Dict[str,float] = {mot: occ / longueur for mot, occ in occurences.items()}

    return freq_mots

assert dictionnaire_freq_mots(mots(exemple1,ponctuation))=={'je': 0.04065040650406504, 'suis': 0.008130081300813009, 'belle': 0.008130081300813009, 'ô': 0.008130081300813009, 'mortels': 0.008130081300813009, 'comme': 0.016260162601626018, 'un': 0.032520325203252036, 'rêve': 0.008130081300813009, 'de': 0.024390243902439025, 'pierre': 0.008130081300813009, 'et': 0.032520325203252036, 'mon': 0.008130081300813009, 'sein': 0.008130081300813009, 'où': 0.008130081300813009, 'chacun': 0.008130081300813009, 's': 0.008130081300813009, 'est': 0.016260162601626018, 'meurtri': 0.008130081300813009, 'tour': 0.016260162601626018, 'à': 0.016260162601626018, 'fait': 0.008130081300813009, 'pour': 0.016260162601626018, 'inspirer': 0.008130081300813009, 'au': 0.008130081300813009, 'poète': 0.008130081300813009, 'amour': 0.008130081300813009, 'Éternel': 0.008130081300813009, 'muet': 0.008130081300813009, 'ainsi': 0.008130081300813009, 'que': 0.016260162601626018, 'la': 0.016260162601626018, 'matière': 0.008130081300813009, 'trône': 0.008130081300813009, 'dans': 0.008130081300813009, 'l': 0.016260162601626018, 'azur': 0.008130081300813009, 'sphinx': 0.008130081300813009, 'incompris': 0.008130081300813009, 'j': 0.024390243902439025, 'unis': 0.008130081300813009, 'coeur': 0.008130081300813009, 'neige': 0.008130081300813009, 'blancheur': 0.008130081300813009, 'des': 0.008130081300813009, 'cygnes': 0.008130081300813009, 'hais': 0.008130081300813009, 'le': 0.008130081300813009, 'mouvement': 0.008130081300813009, 'qui': 0.016260162601626018, 'déplace': 0.008130081300813009, 'les': 0.016260162601626018, 'lignes': 0.008130081300813009, 'jamais': 0.016260162601626018, 'ne': 0.016260162601626018, 'pleure': 0.008130081300813009, 'ris': 0.008130081300813009, 'poètes': 0.008130081300813009, 'devant': 0.008130081300813009, 'mes': 0.024390243902439025, 'grandes': 0.008130081300813009, 'attitudes': 0.008130081300813009, 'ai': 0.016260162601626018, 'air': 0.008130081300813009, 'd': 0.016260162601626018, 'emprunter': 0.008130081300813009, 'aux': 0.016260162601626018, 'plus': 0.016260162601626018, 'fiers': 0.008130081300813009, 'monuments': 0.008130081300813009, 'consumeront': 0.008130081300813009, 'leurs': 0.008130081300813009, 'jours': 0.008130081300813009, 'en': 0.008130081300813009, 'austères': 0.008130081300813009, 'études': 0.008130081300813009, 'car': 0.008130081300813009, 'fasciner': 0.008130081300813009, 'ces': 0.008130081300813009, 'dociles': 0.008130081300813009, 'amants': 0.008130081300813009, 'purs': 0.008130081300813009, 'miroirs': 0.008130081300813009, 'font': 0.008130081300813009, 'toutes': 0.008130081300813009, 'choses': 0.008130081300813009, 'belles': 0.008130081300813009, 'yeux': 0.016260162601626018, 'larges': 0.008130081300813009, 'clartés': 0.008130081300813009, 'éternelles': 0.008130081300813009}

dico2 : Dict[str , float] = dictionnaire_freq_mots (mots(exemple1 , ponctuation ))

assert dico2["je"]==0.04065040650406504
assert dico2["belle"]==0.008130081300813009


#Question 2
def distance_freq(d1:Dict[str,float],d2:Dict[str,float])->float:
    """Calcule la distance entre deux dictionnaires de fréquence
    """
    score : float = 100.0

    for (mot,freq_d2) in d2.items():
        if mot in d1:
            freq_d1 : float = d1[mot]
            score = score - (100.0 * abs(freq_d1 - freq_d2))
        else:
            score = score - (100.0 * freq_d2)

    return abs(score)

dico3 : Dict[str,float] = {'je': 0.25, 'suis': 0.2, 'belle': 0.1, 'et': 0.1, 'mortelle': 0.1}
dico4 : Dict[str,float] = {'je': 0.3, 'suis': 0.25, 'belle': 0.05, 'et': 0.1, 'nouvelle': 0.1}

#assert distance_freq(dico3,dico4) == 75