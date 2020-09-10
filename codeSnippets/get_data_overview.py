import pandas as pd

pokemon_data = pd.read_csv("resources/pokemon_data.csv")

# .head() retuns the first few rows of the DataFrame and is usefull when you have many rows
#print(pokemon_data.head(5))

# .info() returns names of the columns, the data type they contain and whether they have any missing values
#print(pokemon_data.info())

# DataFrame’s shape attribute contains a tuple that holds the number of rows followed by the number of columns
#print(pokemon_data.shape)

# the .describe() method computes some summery statistics for numerical columns, like mean and median
# count is the number of non-missing values in each column
# .describe is good for a quick overview of numeric variables
#print(pokemon_data.describe())

#print(pokemon_data.values)

#print(pokemon_data.columns)
#print(pokemon_data.index)

#print(pokemon_data.head(10))

# print(pokemon_data.sort_values("Defense").head(10))
#print(pokemon_data.sort_values("Defense",ascending=False).head(10))

#print(pokemon_data.sort_values(["Defense","Attack"]).head(10))
#print(pokemon_data.sort_values(["Defense","Attack"],ascending=[False, False]).head(10))

#subsetting columns
#columns = ["Name","Attack","Defense","HP"]
#print(pokemon_data[["Name","Attack","Defense"]])
#print(pokemon_data[columns])

#subsetting rows
#print(pokemon_data[pokemon_data["Attack"]>100].sort_values("Attack", ascending=False).head(10))

#subsetting rows based on text data
#print(pokemon_data[pokemon_data["Type 1"] =="Dragon"])

#subsetting based on multiple conditions
#is_dragon = pokemon_data["Type 1"] =="Dragon"
#is_ice = pokemon_data["Type 2"] =="Ice"
#print(pokemon_data[is_dragon & is_ice])

#print(pokemon_data["Type 1"].isin(["Fire","Water"]))
#is_fire_or_water = pokemon_data["Type 1"].isin(["Fire","Water"])
#print(pokemon_data[is_fire_or_water])

print(pokemon_data.head(5))
# new column
pokemon_data["Att-Def"] = pokemon_data["Attack"] - pokemon_data["Defense"]
print(pokemon_data.sort_values("Att-Def", ascending=False).head(5))