import pandas as pd
import building
import infrastructure
df = pd.read_csv('reseau_en_arbre.csv')

infra = infrastructure.Infra(df)
bat = building.Batiment(infra)
