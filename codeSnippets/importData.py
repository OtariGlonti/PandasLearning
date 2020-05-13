import pandas as pd

pokemon_data = pd.read_csv("resources/pokemon_data.csv")
#print(pokemon_data.head(5))
print(pokemon_data['Name'].head(5))
