import pandas as pd
import requests
import os
import numpy as np

##################################################################################################################
# Fonctions de chargement des données
##################################################################################################################

def load_sujet_tele():
    """
    Cette fonction charge le dataset sujet_tele à partir de l'url fournie, le nettoie et le prépare pour l'analyse.
     Elle retourne un DataFrame pandas contenant les données.

    Returns:
    --------
        sujet_tele (pd.DataFrame): Un DataFrame contenant les données de sujet_tele pour les chaînes de télévision.
    """
    # Chargement de l'url du dataset sujet_tele
    url_sujet_tele = (
        "https://static.data.gouv.fr/resources/classement" +
        "-thematique-des-sujets-de-journaux-televises-janvier-2000" +
        "-decembre-2020/20241015-124725/ina-barometre-jt-tv-donnees" +
        "-quotidiennes-2000-2020-nbre-sujets-durees-202410.csv"
    )
    # Récupération du dataset sujet_tele
    req = requests.get(url_sujet_tele)
    # Création d'un fichier temporaire pour stocker le contenu du dataset
    with open('temp.csv', 'w', encoding='latin-1') as f:
        f.write(req.text)

    # Lecture du dataset sujet_tele en utilisant pandas
    colonnes = ["Date", "Chaîne", "Vide", "Thématique", "Nb_sujets", "Duree_sec"]
    sujet_tele = pd.read_csv('temp.csv', sep=';', encoding='latin-1', header=None, names=colonnes)
    os.remove('temp.csv')

    # Nettoyage et préparation du dataset sujet_tele
    sujet_tele = sujet_tele.drop(columns=['Vide'])
    sujet_tele['Date'] = pd.to_datetime(sujet_tele['Date'], dayfirst=True)

    # Calcul de la proportion de temps consacré à chaque 
    # thématique pour chaque chaîne et chaque date
    sujet_tele['Temps_total_JT'] = (
        sujet_tele.groupby(['Date', 'Chaîne'])['Duree_sec'].transform(sum)
    )
    # Calcul de la proportion de temps consacré à chaque thématique
    sujet_tele['Prop'] = sujet_tele['Duree_sec']/sujet_tele['Temps_total_JT']
    return sujet_tele


def load_parite():
    """
    Cette fonction charge le dataset parite à partir de l'url fournie, le 
    nettoie et le prépare pour l'analyse.
     Elle retourne un DataFrame pandas contenant les données de parité pour 
     les chaînes de télévision présentes dans le dataset sujet_tele.

    Returns:
    --------
        parite (pd.DataFrame): Un DataFrame contenant les données de parité pour les chaînes de télévision.
    """
    # Chargement de l'url du dataset parite
    url_parite = (
        "https://static.data.gouv.fr/resources/temps-de-parole-des-hommes-et-des-femmes-a-la-" +
        "television-et-a-la-radio/20190312-191033/20190308-stats.csv"
    )
    req = requests.get(url_parite)

    # Création d'un fichier temporaire pour stocker le contenu du dataset
    with open('temp.csv', 'w', encoding='utf-8') as f:
        f.write(req.text.encode('latin-1').decode('utf-8'))

    # Lecture du dataset parite en utilisant pandas
    parite = pd.read_csv('temp.csv', sep=',', encoding='utf-8', header=0)
    os.remove('temp.csv')

    # Nettoyage et préparation du dataset parite
    parite['date'] = pd.to_datetime(parite['date'])
    # Conserve uniquement les chaînes présentes dans le dataset sujet_tele
    parite = parite[parite['channel_code'].isin(['TF1', 'M6', 'FR2', 'FR3', 'ART'])]
    return parite


def load_audience():
    """
    Cette fonction charge le dataset audience à partir de l'url fournie, le nettoie et le prépare pour l'analyse.
     Elle retourne un DataFrame pandas contenant les données d'audience pour les chaînes de télévision présentes 
     dans le dataset sujet_tele.

    Returns:
    --------
        audience (pd.DataFrame): Un DataFrame contenant les données d'audience pour les chaînes de télévision.
    """
    # Chargement de l'url du dataset audience
    req = requests.get(
        "http://www.cnc.fr/c/document_library/" +
        "get_file?uuid=ac00e68f-871d-4129-ba90-977c84484bdd&groupId=18"
    )
    # Création d'un fichier temporaire pour stocker le contenu du dataset
    with open('temp.xlsx', 'wb') as f:
        f.write(req.content)

    # Lecture du dataset audience en utilisant pandas
    audience = pd.read_excel(
        'temp.xlsx',
        sheet_name='PartdAudience',
        skiprows=5,
        header=1
    )
    os.remove('temp.xlsx')

    # Nettoyage et préparation du dataset audience
    audience = audience.rename(columns={audience.columns[0]: 'Annee'})
    audience = audience.drop(index=[36, 37, 38, 39])
    audience["Annee"] = audience["Annee"].astype(int)
    audience.replace("-", np.nan, inplace=True)

    # Conserve uniquement les chaînes présentes dans
    # le dataset sujet_tele
    sujet_tele = load_sujet_tele()
    audience = audience.loc[:, audience.columns.isin(
        audience.columns[
            (audience.columns.isin(sujet_tele["Chaîne"].unique()))
            | (audience.columns.isin(['Annee']))
        ]
        )
    ]
    return audience
