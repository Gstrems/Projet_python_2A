### Projet python pour la data science : "Thématiques des journaux télévisés, audience et parité du temps de parole Homme-femme : des interconnexions ?"

## L'objectif du projet 
L'objectif de ce projet est de :
- connaitre l'influence des sujets abordés aux jt sur l'audience des chaînes
- analyser si certaines thématiques d'actualité changent dans un sens ou dans l'autre la part de femmes à l'antenne

## Pour éxécuter le code : 
1. charger les paquets nécessaires depuis le terminal avec la commande suivante : pip install -r requirements.txt
2. Le fichier du rapport est "rapport.ipynb", une fois dessus cliquez sur "Run All"
3. Les autres fichiers contiennent une documentation qui indique leur rôle, ils sont tous importés dans "rapport.ipynb"

## Les données utilisées : 
la source de nos données provient de 3 tables toutes issues du site data.gouv et dont on donne un bref aperçu 



L'objectif de ce projet est de 
- Connaitre l'influence des sujets abordés aux jt sur l'audience des chaînes
- Analyser si certaines thématiques d'actualité changent dans un sens ou dans l'autre la part de femmes à l'antenne

Le projet se trouve dans le Notebook Jupyter rapport.ipynb.
Les fonctions utilisées dans le projet sont regroupées dans le fichier utilities/utilities.py.

## Jeux de données
Nous avons à notre disposition trois tables que nous mettons en relation afin de répondre aux questions précédentes.
- sujet_tele: indique le temps en secondes et la thématique des sujets abordés aux JT du soir de différentes chaînes entre janvier 2000 et décembre 2020. Pour ce jeu de données, nous avons fait l'hypothèse que les colonnes 5 et 6 représentent respectivement le nombre de sujets au JT et le temps total des sujets en seconde. Cela est cohérent avec la durée approximative d'un journal télévisé.
- audience: indique la part d'audience des chaînes entre 1989 et 2020
- parite: indique la part de temps de parole des femmes et des hommes ainsi que le temps de musique selon les chaînes, le jour et l'heure de diffusion  entre janvier 2010 et février 2019

## Statistique exploratoire :
- prop type de sujet par mois/jour - table sujet_types
- évolution pour chaque chaîne de JT de cette proportion
- évolution temps de parole femmes / hommes : on se restreint aux 5 chaînes présentes dans le jeu de données sur les sujets du JT. Le temps de parole féminin est plus important sur les chaînes privées que sur les chaînes publiques. Il augmente globalement entre 2010 et 2019.

## Modélisation :
- Régression de la proportion du temps de parole féminin à la télévision sur les sujets du JT, pour chaque mois. Seul la thématique "Sport" est corrélée à la répartition de la parole femmes / hommes, une fois retirée la tendance linéaire du temps de parole féminin.