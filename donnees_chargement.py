import pandas as pd
import requests
url_sujet_tele = "https://static.data.gouv.fr/resources/classement-thematique-des-sujets-de-journaux-televises-janvier-2000-decembre-2020/20241015-124725/ina-barometre-jt-tv-donnees-quotidiennes-2000-2020-nbre-sujets-durees-202410.csv"
requests.get(url_sujet_tele)
# Vérification que l'url fonctionne

req = requests.get(url_sujet_tele)
print(req.content[:20])
# Observe le format des données
colonnes = ["Date", "Chaîne","Vide", "Thématique", "Nb_sujets", "Duree_sec"]