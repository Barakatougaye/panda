import pandas as pd
import numpy as np


exam_data = {'nom': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'tentatives': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualifier': ['oui', 'non', 'oui', 'non', 'non', 'oui', 'oui', 'non', 'non', 'oui']}


etiquettes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


df = pd.DataFrame(exam_data, index=etiquettes)


print("Les trois premières lignes du DataFrame :")
print(df.head(3))

df=df.dropna()
print("\n Suppression des lignes avec des valeurs NaN \n:", df)

print("\nColonnes 'nom' et 'score' :")
print(df[['nom', 'score']])

df.loc['k'] = ['Suresh', 15.5, 1, 'oui']
print("\n Ajout d'une nouvelle ligne 'k' :", df)

df = df.drop(columns='tentatives')
print("\n suppression de la colonne 'tentatives' : \n", df)

df['Succès'] = df['score'].apply(lambda x: 1 if x > 10 else 0)
print("\n ajout de la colonne 'Succès' : \n", df)

df.to_csv('my_data.csv', index=True)
