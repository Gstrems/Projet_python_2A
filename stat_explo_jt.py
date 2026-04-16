import pandas as pd
from load_data.donnees_chargement import load_sujet_tele

sujet_tele = load_sujet_tele()


#on veut transformer la variable Date en objet date
print(sujet_tele['Date'].dtypes)