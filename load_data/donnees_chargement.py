import pandas as pd
import requests
import os


def load_sujet_tele():
    url_sujet_tele = "https://static.data.gouv.fr/resources/classement-thematique-des-sujets-de-journaux-televises-janvier-2000-decembre-2020/20241015-124725/ina-barometre-jt-tv-donnees-quotidiennes-2000-2020-nbre-sujets-durees-202410.csv"
    requests.get(url_sujet_tele)
    req = requests.get(url_sujet_tele)
    colonnes = ["Date", "Chaîne","Vide", "Thématique", "Nb_sujets", "Duree_sec"]
    with open('temp.csv', 'w', encoding='latin-1') as f:
        f.write(req.text)
    sujet_tele = pd.read_csv('temp.csv', sep=';', encoding='latin-1', header=None, names=colonnes)
    os.remove('temp.csv')
    sujet_tele = sujet_tele.drop(columns=['Vide'])
    sujet_tele['Date'] = pd.to_datetime(sujet_tele['Date'], dayfirst= True)
    return sujet_tele


def load_parite():
    url_parite = "https://static.data.gouv.fr/resources/temps-de-parole-des-hommes-et-des-femmes-a-la-television-et-a-la-radio/20190312-191033/20190308-stats.csv"
    req = requests.get(url_parite)
    with open('temp.csv', 'w', encoding='utf-8') as f:
        f.write(req.text.encode('latin-1').decode('utf-8'))
    parite = pd.read_csv('temp.csv', sep=',', encoding='utf-8', header=0)
    os.remove('temp.csv')
    parite['date'] = pd.to_datetime(parite['date'])
    parite = parite[parite['channel_code'].isin(['TF1', 'M6', 'FR2', 'FR3', 'ART'])]
    parite['week_day_number'] = parite['week_day'].replace({
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6,
        'Sunday': 7
    })
    return parite


def load_audience():
    url_audience = "http://www.cnc.fr/c/document_library/get_file?uuid=ac00e68f-871d-4129-ba90-977c84484bdd&groupId=18"
    req = requests.get(url_audience)
    with open('temp.xlsx', 'wb') as f:
        f.write(req.content)
    audience = pd.read_excel('temp.xlsx',
                         sheet_name='PartdAudience',
                         skiprows=5,
                         header = 1
                        )
    audience = audience.rename(columns={audience.columns[0]: 'Annee'})
    os.remove('temp.csv')
    sujet_tele = load_sujet_tele()
    audience = audience.loc[:, audience.columns.isin(
        audience.columns[
            (audience.columns.isin(sujet_tele["Chaîne"].unique()))
            | (audience.columns.isin(['Annee']))
        ]
        )
    ]
    audience = audience.drop(index=[36,37,38,39])
    audience["Annee"] = audience["Annee"].astype(int)
    return audience
