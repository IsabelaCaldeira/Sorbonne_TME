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

def ouvre_fichier(nom : str) -> List[str] :
    """ renvoie la liste des lignes du fichier texte ./nom.csv """
    with open("./"+nom+".csv", "r") as f:
        return f.readlines()
