import pandas as pd

data1 = pd.read_csv("resources/TomaDataClean.csv")
#print(data1["clicks"].unique())
data1.drop(data1[data1.clicks == -1.].index, inplace=True)
#print(data1["installs"].unique())
data1.drop(data1[data1.installs == -2.].index, inplace=True)
#print(data1["budget_spend"].sort_values(ascending=True).head())
print(data1.info())