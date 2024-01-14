# main.py

import pandas as pd
import sqlite3
import plotly.express as px
import json

def handle_exception(exception):
    print(f"Une exception a ete levee : {exception}")

def query(conn, query_json):
    try:
        # Charger la structure JSON
        params = json.loads(query_json)

        # Execution de la requête SQL
        result = pd.read_sql_query(params['query'], conn)

        # Obtenir la fonction Plotly Express à partir du nom dans le fichier JSON
        plot_function = getattr(px, params['plot_function'])

        # Obtenir les parametres specifiques de la fonction Plotly Express à partir du fichier JSON
        plot_params = params.get('plot_params', {})

        # Creation du graphique avec Plotly Express en utilisant la fonction dynamiquement obtenue et les parametres specifies
        fig = plot_function(result, **plot_params)

        # Affichage du graphique
        fig.show()

    except json.JSONDecodeError as e:
        handle_exception(f"Erreur lors de la lecture du fichier JSON : {e}")
    except pd.errors.EmptyDataError:
        handle_exception("Le fichier de ventes est vide ou mal formate.")
    except Exception as e:
        handle_exception(f"Erreur inattendue : {e}")

# Chargement du fichier CSV depuis le repertoire par defaut
try:
    df = pd.read_csv('ventes.csv')
except Exception as e:
    handle_exception(f"Erreur lors du chargement du fichier de ventes : {e}")
    df = pd.DataFrame()

# Creation d'une connexion à une base de donnees SQLite en memoire
conn = sqlite3.connect(':memory:')

# ecriture du DataFrame dans la base de donnees
df.to_sql('ventes', conn, index=False, if_exists='replace')

# Lecture du fichier JSON contenant les structures JSON des requêtes
try:
    with open('queries.json', 'r') as file:
        data = json.load(file)
except json.JSONDecodeError as e:
    handle_exception(f"Erreur lors de la lecture du fichier JSON : {e}")
    data = {"queries": []}

# Appel de la fonction query pour chaque structure JSON
for query_json in data["queries"]:
    query(conn, json.dumps(query_json))

# Fermeture de la connexion
conn.close()
