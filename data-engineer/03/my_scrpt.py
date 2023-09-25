import os
from sqlalchemy import create_engine
import pandas as pd

# Connexion à la base de données PostgreSQL
# conn = psycopg2.connect(
#     host="localhost",
#     port=5433,
#     database="postgres",
#     user="alukongo",
#     password="mysecretpassword"
# )

engine = create_engine('postgresql://alukongo:mysecretpassword@localhost:5433/postgres')

# Répertoire contenant les fichiers CSV
directory = '/Users/axellukongo/Downloads/subject/customer'

# Parcours des fichiers CSV dans le répertoire
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        table_name = os.path.splitext(filename)[0]  # Nom de table sans l'extension
        file_path = os.path.join(directory, filename)

        # Lecture des données CSV en utilisant pandas
        df = pd.read_csv(file_path, delimiter=',')  # Assurez-vous d'utiliser le bon délimiteur

        # Création de la table dans la base de données
        df.to_sql(table_name, engine, if_exists='replace', index=False, schema='public')


# Fermeture de la connexion à la base de données
engine.dispose()