import pandas as pd
from load_data.donnees_chargement import load_sujet_tele

sujet_tele = load_sujet_tele()
#on calcule le temps total du JT de chaque jour pour chaque chaîne:
sujet_tele['Temps_total_JT'] = sujet_tele.groupby(['Date','Chaîne'])['Duree_sec'].transform(sum)

#on créer une colonne "prop" qui contient la proportion de temps dans l'émission dédiée à un type de sujet 
sujet_tele['Prop']=sujet_tele['Duree_sec']/sujet_tele['Temps_total_JT']
