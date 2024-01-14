import pandas as pd
import plotly.graph_objs as go

# Affiche "Hello World"
print("Hello World")

# Donnees de vente
data = {
    'Produit': ['A', 'B', 'C'],
    'Chiffre_d_affaires': [100, 150, 200]
}

# Creation d'un DataFrame pandas
df = pd.DataFrame(data)

# Creation d'une trace de barre avec Plotly
trace = go.Bar(x=df['Produit'], y=df['Chiffre_d_affaires'])

# Creation de la mise en page du graphique
layout = go.Layout(title='Statistique de Ventes', xaxis=dict(title='Produit'), yaxis=dict(title='Chiffre d\'affaires'))

# Creation de la figure
figure = go.Figure(data=[trace], layout=layout)

# Affichage du graphique
figure.show()
