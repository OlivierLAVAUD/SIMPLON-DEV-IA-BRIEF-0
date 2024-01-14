# Title: Problem Solving Ventes 
# Date:  2023-11-12
# Author: Olivier LAVAUD / Olivier.Lavaud@gmail.com 
# Object: Ecole IA - Simplon - Microsfot Admission
#
# File:   main.py
# Coding Strategy: All in one dynamic with JSON inside
# Comment: Dynamic function call of plotly.express with on input file (Ventes.csv) and Json querie inside. 
#
# Requirements: 
# Python 3.9.17 with Json, Plotly Express, Sqlite3, Pandas package
# Input files:  ventes.csv
#
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

    # Obtenir les paramètres specifiques de la fonction Plotly Express a partir du fichier JSON
    plot_params = params.get('plot_params', {})

    # Creation du graphique avec Plotly Express en utilisant la fonction dynamiquement obtenue et les parametres specifies
    fig = plot_function(result, **plot_params)

    # Affichage du graphique
    fig.show()
#eof query

# Donnees JSON directement incluses dans le code
data_json = '''
{
  "queries": [
    {
      "query": "SELECT 'Tous les produits' as prd , SUM(prix * qte) AS ca FROM ventes;",      
      "plot_function": "bar",
      "plot_params": {
        "x": "prd",
        "y": "ca",       
        "title": "Chiffre d'affaires global"
      }
    },
    {
      "query": "SELECT produit, SUM(prix * qte) AS ca FROM ventes GROUP BY produit;",     
      "plot_function": "bar",
      "plot_params": {
        "x": "produit",
        "y": "ca",
        "color": "produit",        
        "title": "Chiffre d'affaires par produit"
      }
    },
    {
      "query": "SELECT region, SUM(prix * qte) AS ca FROM ventes GROUP BY region;",      
      "plot_function": "bar",
      "plot_params": {
        "x": "region",
        "y": "ca",
        "color": "region",        
        "title": "Chiffre d'affaires par region"
      }
    }
  ]
}
'''

# Conversion de la chaine JSON en objet Python
data = json.loads(data_json)

# Chargement du fichier CSV depuis le repertoire par défaut
df = pd.read_csv('ventes.csv')

# Creation d'une connexion à une base de données SQLite en memoire
conn = sqlite3.connect(':memory:')

# Ecriture du DataFrame dans la base de donnees
df.to_sql('ventes', conn, index=False, if_exists='replace')

# Appel de la fonction query pour chaque structure JSON
for query_json in data.get("queries", []):
    query(conn, query_json)

# Fermeture de la connexion
conn.close()