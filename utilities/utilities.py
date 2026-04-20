# Contient les fonctions utilitaires pour le projet

######################################################################################################
# Chargement des packages
######################################################################################################
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

######################################################################################################
# Fonctions de la table sujet_tele
######################################################################################################
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


######################################################################################################
# Fonctions de la table audience
######################################################################################################

def audience_par_annee(audience,annee, chaine):
    """
    Affiche l'audience d'une chaîne de télévision en fonction de l'année.

    Paramètres :
    -------------
    audience : DataFrame
        le DataFrame contenant les données d'audience
    annee : str
        le nom de la colonne contenant les années
    chaine : str
        le nom de la chaîne de télévision dont on veut afficher l'audience
    """
    audience.plot(x=annee, y=chaine, kind="line", title=f"Audience de {chaine} en fonction de l'année")

def comparaison_audience(audience, annee, chaines):
    """
    Affiche la comparaison de l'audience de deux chaînes de télévision en fonction de l'année.

    Paramètres :
    -------------
    audience : DataFrame
        le DataFrame contenant les données d'audience
    annee : str
        le nom de la colonne contenant les années
    chaines : list
        la liste des chaînes de télévision dont on veut afficher l'audience
    """
    return audience.plot(x=annee, y=chaines, kind="line", title=f"Comparaison de l'audience des chaînes {', '.join(chaines)} en fonction de l'année")

def comparaison_audience_axes(audience, annee, chaine1, chaine2, titre = None):
    """
    Affiche la comparaison de l'audience de deux groupes de chaînes de télévision en fonction de l'année, avec des axes y séparés.

    Paramètres :
    -------------
    audience : DataFrame
        le DataFrame contenant les données d'audience
    annee : str
        le nom de la colonne contenant les années
    chaines1 : str
        chaîne de télévision
    chaines: str
        chaîne de télévision
    titre : str
        Paramètre qui apparaît dans le titre et remplace chaîne 2
    """
    fig, ax1 = plt.subplots()
    ax1.plot(audience[annee], audience[chaine1], color="blue", label=f"{chaine1}")
    if chaine1 in ["Audience", "Total", "Temps moyen", "Temps cumul"]:
        ax1.set_ylabel(f"{chaine1}", color="blue")
    else:
        ax1.set_ylabel(f"Audience de {chaine1}", color="blue")

    ax2 = ax1.twinx()
    ax2.plot(audience[annee], audience[chaine2], color="darkred", label=f"{chaine2}")
    if chaine2 in ["Audience", "Total", "Temps moyen", "Temps cumul"]:
        ax2.set_ylabel(f"{chaine2}", color="darkred")
    else:
        ax2.set_ylabel(f"Audience de {chaine2}", color="darkred")

    ax1.set_xlabel("Année")

    if titre is not None:
        if chaine1 == "Audience":
            ax1.set_title(f"Comparaison de l'audience et de {titre} en fonction de l'année")
        else:
            ax1.set_title(f"Comparaison de l'audience {chaine1} et {chaine2} en fonction de l'année")
    else:
        if chaine1 == "Audience":
            ax1.set_title(f"Comparaison de l'audience et de {chaine2} en fonction de l'année")
        else:
            ax1.set_title(f"Comparaison de l'audience {chaine1} et {chaine2} en fonction de l'année")
    fig.tight_layout()

def evolution_audience_sujet_chaine(df, sujet, chaine,
                                    Thematique = "Thématique",
                                    Chaine = "Chaîne",
                                    Date = "Date",
                                    Audience = "Audience",
                                    Temps = "Temps moyen"):
    """
    Affiche l'évolution de l'audience d'une chaîne donnée en fonction du de l'année, 
    ainsi que l'évolution du temps moyen des émissions sur le sujet donné.
    
    Paramètres:
    ------------
        df: pd.DataFrame
            Le DataFrame contenant les données d'audience et de sujets télévisés.
        sujet: str
           Le sujet à analyser.
       chaine: str
           La chaîne à analyser.
       Thematique: str
           Le nom de la colonne contenant les thématiques (par défaut "Thématique").
       Chaine: str
          Le nom de la colonne contenant les chaînes (par défaut "Chaîne").
      Date: str
          Le nom de la colonne contenant les dates (par défaut "Date").
      Audience: str
           Le nom de la colonne contenant les audiences (par défaut "Audience").
       Temps: str
           Le nom de la colonne contenant les temps moyens des émissions (par défaut "Temps moyen") ou du 
           temps cumulé.
    """
    if sujet not in df[Thematique].unique():
        raise ValueError(f"Le sujet '{sujet}' n'est pas présent dans la colonne '{Thematique}'.")
    if chaine not in df[Chaine].unique():
        raise ValueError(f"La chaîne '{chaine}' n'est pas présente dans la colonne '{Chaine}'.")
    df_filtre = df[(df[Thematique] == sujet) & (df[Chaine] == chaine)]
    comparaison_audience_axes(df_filtre,
                              Date,
                              chaine1 = Audience,
                              chaine2 = Temps,
                              titre = f"{Temps} de {sujet} sur {chaine}")


######################################################################################################
# Fonctions de la table parité
######################################################################################################

def parite_var_chaine(df, variable: str):
    """
    Renvoie un dataframe contenant pour chaque chaîne et pour chaque valeur de la variable variable
    le temps de parole féminin, masculin, ainsi que la proportion du temps de parole féminin.
    
    Paramètres:
    ------------
        df: pd.DataFrame
            Le DataFrame contenant les données de temps de parole hommes / femmes à la télévision.
        variable: str
           La variable selon laquelle regrouper les temps de parole.
    """

    parite_variable_chaine = df.groupby(['channel_code', variable]).agg(
        channel_name = ('channel_name', 'first'),
        female_duration = ('female_duration', 'sum'),
        male_duration = ('male_duration', 'sum')
    ).reset_index()

    parite_variable_chaine['proportion_female'] = parite_variable_chaine['female_duration'] / (parite_variable_chaine['female_duration'] + parite_variable_chaine['male_duration'])

    return parite_variable_chaine

def diagramme_temps_parole_var(df, variable: str, code_chaine: str, label: str):
    """
    Affiche sous forme de diagramme en barres la proportion de temps de parole féminin pour la chaîne
    code_chaine et pour chaque valeur de la variable variable.
   
    Paramètres:
    ------------
        df: pd.DataFrame
            Le DataFrame contenant les données de temps de parole hommes / femmes à la télévision.
        variable: str
           La variable selon laquelle regrouper les temps de parole.
        code_chaine: str
            Le code de la chaine à considérer
        label: str
            Le nom de la variable à regarder, tel qu'il apparaîtra sur le diagramme.
    """


    parite_variable_chaine = parite_var_chaine(df=df, variable=variable)
    parite_variable = parite_variable_chaine[
        parite_variable_chaine['channel_code'] == code_chaine
    ].reset_index()
    diag = parite_variable.sort_values(by=variable).plot.bar(
        x = variable,
        y = 'proportion_female',
        title = "Temps de parole féminin par " + label + " pour la chaîne " + parite_variable['channel_name'][0],
        legend=False,
        xlabel=label,
        ylabel="Part de temps de parole féminin",
        grid=True
    )
    
    diag.xaxis.grid(False)

def diagramme_temps_parole_evolution(df, code_chaine:str):
    """
    Affiche sous forme de diagramme en ligne
    l'évolution de la proportion de temps de parole féminin
    pour la chaîne code_chaine.
   
    Paramètres:
    ------------
        df: pd.DataFrame
            Le DataFrame contenant les données de temps de parole hommes / femmes à la télévision par mois et chaîne.
        code_chaine: str
            Le code de la chaine à considérer
    """

    parite_evolution = df[
        df['channel_code'] == code_chaine
    ].reset_index()

    diag = parite_evolution.set_index('monthly_date')['proportion_female'].plot(
        title = "Temps de parole féminin par mois pour la chaîne " + parite_evolution['channel_name'][0],
        legend=False,
        xlabel="Mois",
        ylabel="Part de temps de parole féminin",
    )

######################################################################################################
# Fonctions de la table sujet_tele///audience
######################################################################################################

def correlation_theme_audience(df: pd.DataFrame = None,
                               Thematique: str = "Thématique",
                               Chaine: str = "Chaîne",
                               Temps: str = "Temps moyen",
                               Audience: str = "Audience",
                               corr = None):
    """
    Calcule la corrélation entre le temps moyen et l'audience pour chaque thématique et chaque chaîne,
    puis affiche une heatmap de ces corrélations.
    
    Paramètres:
    -----------
    df : pd.DataFrame
        Le DataFrame contenant les données à analyser.
    Thematique : str
        Le nom de la colonne représentant les thématiques.
    Date : str
        Le nom de la colonne représentant les dates.
    Chaine : str
        Le nom de la colonne représentant les chaînes.
    Temps_moyen : str
        Le nom de la colonne représentant le temps moyen ou le temps cumulé.
    Audience : str
        Le nom de la colonne représentant l'audience.
    """
    # S'assure que les colonnes Temps et Audience sont de
    # type numérique pour le calcul de la corrélation
    if df is not None:
        df[Temps] = df[Temps].astype(float)
        df[Audience] = df[Audience].astype(float)

    # Récupère la corrélation entre chaque temps moyen et 
    # audience en fonction de la thématique et de la chaîne
    if corr is None:
        corr = df.groupby([Thematique, Chaine]).apply(
            lambda g: 
                     g[Temps].corr(g[Audience])
            )
        # Transforme la série de corrélation en DataFrame et 
        # pivote pour avoir les thématiques en index et les chaînes en colonnes
        corr = corr.reset_index(name="corr").pivot(index=Thematique, columns=Chaine, values="corr") 

    if df is None and corr is None:
        raise ValueError("Vous devez fournir soit un DataFrame pour calculer la corrélation, soit une matrice de corrélation pré-calculée.")
    # Création de la visualisation de la corrélation
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",)
    plt.title(f"Corrélation entre {Temps} de diffusion au JT et {Audience} moyenne par {Thematique} par année et par chaîne")
    plt.show()

