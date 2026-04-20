# Projet python pour la data science : "Thématiques des journaux télévisés, audience et parité du temps de parole Homme-femme : des interconnexions ?"

## L'objectif du projet 
L'objectif de ce projet est de :
- connaitre l'influence des sujets abordés aux journaux télévisés sur l'audience des chaînes
- analyser si certaines thématiques d'actualité changent dans un sens ou dans l'autre la part de femmes à l'antenne

Le plan du rapport est le suivant : 
1. <b>traitement préalable des données brutes<b>

2. <b>Statistique exploratoire sur les données relatives à l'audience <b>: 
- représentation du temps moyen de diffusion à l'année et de l'évolution de l'audience
- corrélation entre temps de parole moyen ou cummulé avec l'évolution de l'audience.
- proportion du temps de parole féminin par chaîne
- proportion du temps de parole féminin selon le jour de la semaine
- proportion du temps de parole féminin selon le mois de l'année

3. <b>Modélisation de la de la proportion du temps de parole féminin à la télévision sur les sujets du JT, pour chaque mois<b> 

Conclusion : Seule la thématique "Sport" est corrélée à la répartition de la parole femmes / hommes, une fois retirée la tendance linéaire du temps de parole féminin.

## Pour éxécuter le code : 
1. charger les paquets nécessaires depuis le terminal avec la commande suivante : pip install -r requirements.txt
2. Le fichier du rapport est "rapport.ipynb", une fois dessus cliquer sur "Run All"
3. Les autres fichiers contiennent une documentation qui indique leur rôle, ils sont tous importés dans "rapport.ipynb"

## Les données utilisées : 
la source de nos données provient de 3 tables toutes issues du site data.gouv et dont on donne un bref aperçu ci-dessous.
1. la table <b>"sujet_tele"<b>: indique le temps en secondes et la thématique des sujets abordés aux JT du soir de différentes chaînes entre janvier 2000 et décembre 2020. Pour ce jeu de données, nous avons fait l'hypothèse que les colonnes 5 et 6 représentent respectivement le nombre de sujets au JT et le temps total des sujets en seconde. Cela est cohérent avec la durée approximative d'un journal télévisé.
2. la table <b>"audience"<b>: indique la part d'audience des chaînes entre 1989 et 2020
3. la table <b>"parite"<b>: indique la part de temps de parole des femmes et des hommes ainsi que le temps de musique , le tout selon les chaînes, le jour et l'heure de diffusion  entre janvier 2010 et février 2019

Toutes ces tables proviennent du site data.gouv et leur chargement est opéré via un lien url.
Un traitement préalable des données pour les rendre exploitables a été mené et se trouve en première partie de rapport.
