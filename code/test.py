import pandas as pd 

df = pd.read_csv('reseau_en_arbre.csv')
df_importance = df[(df['infra_type']=='a_remplacer')]
df_i  = df_importance.groupby(by='id_batiment')
for id_batiment, bat in df_i:
    print(id_batiment)
    print(bat)
    print('_'*30)
