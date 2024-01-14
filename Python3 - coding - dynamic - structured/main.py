# Title: Problem Solving Ventes 
# Date:  2023-11-12
# Author: Olivier LAVAUD / Olivier.Lavaud@gmail.com 
# Object: Ecole IA - Simplon - Microsfot Admission
#
# File:   main.py
# Coding Strategy: Dynamic & Structured
# Comment: Dynamic function call with structured input files (files:  Ventes.csv, queries.json)
#
# Requirements: 
# Ennvironement: Python3 with Json, Plotly Express, Sqlite3, Pandas package
# Input files:  ventes.csv, queries.json
#

import plotly.express as px
import sqlite3
import json
import pandas as pd


def query(conn, params):
    # Execution de la requete SQL
    result = pd.read_sql_query(params['query'], conn)

    # Obtenir la fonction Plotly Express a partir du nom dans le fichier JSON
    plot_function = getattr(px, params['plot_function'])

    # Obtenir les parametres specifiques de la fonction Plotly Express à partir du fichier JSON
    plot_params = params.get('plot_params', {})

    # Creation du graphique avec Plotly Express en utilisant la fonction dynamiquement obtenue et les paramètres specifies
    fig = plot_function(result, **plot_params)

    # Affichage du graphique
    fig.show()

# Chargement du fichier CSV depuis le repertoire par defaut
df = pd.read_csv('ventes.csv')

# Creation d'une connexion a une base de données SQLite en mémoire
conn = sqlite3.connect(':memory:')

# Ecriture du DataFrame dans la base de donnees
df.to_sql('ventes', conn, index=False, if_exists='replace')

# Lecture du fichier JSON contenant les structures JSON des requêtes
with open('queries.json', 'r') as file:
    data = json.load(file)

# Appel de la fonction query pour chaque structure JSON
for query_json in data.get("queries", []):
    query(conn, query_json)

# Fermeture de la connexion
conn.close()
