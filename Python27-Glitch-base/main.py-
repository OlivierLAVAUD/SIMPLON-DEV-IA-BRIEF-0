# Title: Problem Solving Ventes 
# Date:  2023-11-12
# Author: Olivier LAVAUD / Olivier.Lavaud@gmail.com 
# Object: Ecole IA - Simplon - Microsfot Admission
#
# File:   main.py
# Coding Strategy: All in one
# Comment: Dynamic function call of plotly.express with all input in the code and Json querie inside to get data. 
#          We simply for running into Glitch 
#
# Requirements: 
# Python 2.7 with Json, Plotly Express Pandas package
# Input files:  ventes.csv
#
# Remarks: We have compatibility problem of package and R/W problem on system, also memory limited on glitch environement
#          this is why we simplify the code extremly. 


import plotly.express as px
import pandas as pd
import json

def query(df, params):
    # Execution de la requete SQL
    result = df.query(params['query'])

    # Obtenir les parametres specifiques de la fonction Plotly Express a partir du fichier JSON
    plot_params = params.get('plot_params', {})

    # Creation du graphique avec Plotly Express en utilisant la fonction dynamiquement obtenue et les parametres specifies
    fig = px.bar(result, **plot_params)

    # Affichage du graphique
    fig.show()

# Donnees JSON directement incluses dans le code
data_json = '''
{
  "queries": [
    {
      "query": "prd = 'Tous les produits'; ca = df['prix'] * df['qte'];",      
      "plot_params": {
        "x": "prd",
        "y": "ca",       
        "title": "Chiffre d'affaires global"
      }
    },
    {
      "query": "ca = df.groupby('produit')['prix', 'qte'].sum();",     
      "plot_params": {
        "x": "produit",
        "y": "ca",
        "color": "produit",        
        "title": "Chiffre d'affaires par produit"
      }
    },
    {
      "query": "ca = df.groupby('region')['prix', 'qte'].sum();",      
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

# Chargement du fichier CSV depuis le repertoire par defaut
csv_data = '''date,produit,prix,qte,region
2022-01-01,Produit A,10,100,Nord
2022-01-02,Produit B,15,50,Nord
2022-01-02,Produit A,10,75,Sud
2022-01-03,Produit C,20,30,Nord
2022-01-03,Produit A,10,150,Sud
2022-01-04,Produit B,15,75,Nord
2022-01-04,Produit C,20,50,Sud
2022-01-05,Produit A,10,125,Nord
2022-01-05,Produit B,15,100,Sud
2022-01-06,Produit C,20,25,Nord
2022-01-06,Produit A,10,100,Sud
2022-01-07,Produit B,15,60,Nord
2022-01-07,Produit C,20,40,Sud
2022-01-08,Produit A,10,80,Nord
2022-01-08,Produit B,15,90,Sud
2022-01-09,Produit C,20,35,Nord
2022-01-09,Produit A,10,120,Sud
2022-01-10,Produit B,15,70,Nord
2022-01-10,Produit C,20,60,Sud
2022-01-11,Produit A,10,150,Nord
2022-01-11,Produit B,15,80,Sud
2022-01-12,Produit C,20,40,Nord
2022-01-12,Produit A,10,200,Sud
2022-01-13,Produit B,15,100,Nord
2022-01-13,Produit C,20,60,Sud
2022-01-14,Produit A,10,120,Nord
2022-01-14,Produit B,15,50,Sud
2022-01-15,Produit C,20,30,Nord
2022-01-15,Produit A,10,75,Sud
2022-01-16,Produit B,15,90,Nord
2022-01-16,Produit C,20,75,Sud
2022-01-17,Produit A,10,180,Nord
2022-01-17,Produit B,15,100,Sud
2022-01-18,Produit C,20,50,Nord
2022-01-18,Produit A,10,150,Sud
2022-01-19,Produit B,15,70,Nord
2022-01-19,Produit C,20,80,Sud
2022-01-20,Produit A,10,125,Nord
2022-01-20,Produit B,15,120,Sud
'''

df = pd.read_csv(pd.compat.StringIO(csv_data))

# Appel de la fonction query pour chaque structure JSON
for query_json in data.get("queries", []):
    query(df, query_json)