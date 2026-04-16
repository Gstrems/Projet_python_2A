# Contient les fonctions utilitaires pour le projet

# Fonctions de la table sujet_tele
def sujet_convert(indic,
                  table,
                  Date = 'Date',
                  Thématique = 'Thématique',
                  Duree_sec = 'Duree_sec',
                  Chaine = 'Chaîne'):
    """
    Convertit la table sujet_tele en fonction de l'indicateur choisi (Y pour year ou M pour Month)
    et calcule le temps cumul et le temps moyen pour chaque thème et chaque chaîne
    
    Paramètres :
    ------------
    indic : str
        "Y" pour year ou "M" pour Month à mettre en entrée
    table : pd.DataFrame
        La table sujet_tele à convertir
    Date : str
        Le nom de la colonne contenant les dates dans la table sujet_tele (par défaut "Date")
    Thématique : str
        Le nom de la colonne contenant les thématiques dans la table sujet_tele (par défaut "Thématique")
    Duree_sec : str
        Le nom de la colonne contenant les durées en secondes dans la table sujet_tele (par défaut "Duree_sec")
    Chaine : str
        Le nom de la colonne contenant les chaînes dans la table sujet_tele (par défaut "Chaîne")
    
    Retour :
    ------------
    table_convert : pd.DataFrame
        La table convertie avec les temps cumul et les temps moyens pour chaque thème et chaque chaîne
    """
    if indic not in ("Y", "M"):
        raise ValueError("Y pour year ou M pour Month à mettre en entrée")
    table_convert= table.groupby([table[Date].dt.to_period(indic), Chaine, Thématique])[Duree_sec].sum().reset_index()
    table_convert.rename(columns={Duree_sec: 'Temps cumul'}, inplace=True)
    table_convert_mean = table.groupby([table[Date].dt.to_period(indic), Chaine, Thématique])[Duree_sec].mean().reset_index()
    table_convert_mean.rename(columns={Duree_sec: 'Temps moyen'}, inplace=True)
    table_convert['Temps moyen'] = table_convert_mean['Temps moyen']
    return table_convert

# Fonctions de la table audience
import matplotlib.pyplot as plt

def audience_par_annee(audience,annee, chaine):
    """
    Affiche l'audience d'une chaîne de télévision en fonction de l'année.

    Paramètres :
    -------------
    audience (DataFrame) : le DataFrame contenant les données d'audience
    annee (str) : le nom de la colonne contenant les années
    chaine (str) : le nom de la chaîne de télévision dont on veut afficher l'audience
    """
    audience.plot(x=annee, y=chaine, kind="line", title=f"Audience de {chaine} en fonction de l'année")

def comparaison_audience(audience, annee, chaines):
    """
    Affiche la comparaison de l'audience de deux chaînes de télévision en fonction de l'année.

    Paramètres :
    -------------
    audience (DataFrame) : le DataFrame contenant les données d'audience
    annee (str) : le nom de la colonne contenant les années
    chaines (list) : la liste des chaînes de télévision dont on veut afficher l'audience
    """
    return audience.plot(x=annee, y=chaines, kind="line", title=f"Comparaison de l'audience des chaînes {', '.join(chaines)} en fonction de l'année")

def comparaison_audience_axes(audience, annee, chaine1, chaine2):
    """
    Affiche la comparaison de l'audience de deux groupes de chaînes de télévision en fonction de l'année, avec des axes y séparés.

    Paramètres :
    -------------
    audience (DataFrame) : le DataFrame contenant les données d'audience
    annee (str) : le nom de la colonne contenant les années
    chaines1 (str) : chaîne de télévision
    chaines2 (str) : chaîne de télévision
    """
    fig, ax1 = plt.subplots()
    ax1.plot(audience[annee], audience[chaine1], color="blue", label=f"{chaine1}")
    ax1.set_ylabel(f"Audience {chaine1}", color="blue")

    ax2 = ax1.twinx()
    ax2.plot(audience[annee], audience[chaine2], color="darkred", label=f"{chaine2}")
    ax2.set_ylabel(f"Audience {chaine2}", color="darkred")

    ax1.set_xlabel("Année")
    fig.tight_layout()