import os
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://alukongo:mysecretpassword@localhost:5433/postgres')

# Répertoire contenant les fichiers CSV
directory = '/home/alukongo/Téléchargements/subject/customer'

# Parcours des fichiers CSV dans le répertoire
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        print("tables en cours de creation")
        table_name = os.path.splitext(filename)[0]
        file_path = os.path.join(directory, filename)

        # Lecture des données CSV en utilisant pandas
        df = pd.read_csv(file_path, delimiter=',')

        # Création de la table dans la base de données
        df.to_sql(table_name, engine, if_exists='replace', index=False, schema='public')


# Fermeture de la connexion à la base de données
print("======>>>>>  creation terminer  <<<<<======")
engine.dispose()