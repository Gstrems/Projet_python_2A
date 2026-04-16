import pandas as pd
from load_data.donnees_chargement import load_parite

parite = load_parite()

parite_chaines_jt = parite[parite['channel_code'].isin(['TF1', 'M6', 'FR2', 'FR3', 'ART'])]
print(parite_chaines_jt.head())
