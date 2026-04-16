import pandas as pd
import requests


def load_sujet_tele():
    url_sujet_tele = "https://static.data.gouv.fr/resources/classement-thematique-des-sujets-de-journaux-televises-janvier-2000-decembre-2020/20241015-124725/ina-barometre-jt-tv-donnees-quotidiennes-2000-2020-nbre-sujets-durees-202410.csv"
    requests.get(url_sujet_tele)
    req = requests.get(url_sujet_tele)
    print(req.content[:20])
    colonnes = ["Date", "Chaîne","Vide", "Thématique", "Nb_sujets", "Duree_sec"]
    with open('temp.csv', 'w', encoding='latin-1') as f:
        f.write(req.text)
    sujet_tele = pd.read_csv('temp.csv', sep=';', encoding='latin-1', header=None, names=colonnes) 
    return sujet_tele
