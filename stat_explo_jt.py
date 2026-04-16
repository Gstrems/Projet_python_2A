import pandas as pd
from load_data.donnees_chargement import load_sujet_tele

sujet_tele = load_sujet_tele()
#on calcule le temps total du JT de chaque jour pour chaque chaîne:
sujet_tele['Temps_total_JT'] = sujet_tele.groupby(['Date','Chaîne'])['Duree_sec'].transform(sum)
print(sujet_tele)
#on créer une colonne "prop" qui 