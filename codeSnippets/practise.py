import pandas as pd
from numpy import mean
import numpy as np

data1 = pd.read_csv("resources/peopleDataJoin1.csv")
data2 = pd.read_csv("resources/peopleDataJoins2.csv")
#data1.reset_index(drop=True, inplace=True)
#data2.reset_index(drop=True, inplace=True)



data3 = pd.merge(data1, data2, on="id")
print(data3.head(10))


#peopleData1 = pd.read_csv("resources/peopleDataPractise1.csv")
#peopleData1.index += 1 
#peopleData2 = peopleData1[['first_name','id']]

#print(peopleData1.pivot_table(values=["height","weight"], index="gender", margins=True))

"""
print(peopleData1.head(10))
print(peopleData1.groupby("gender")["height","weight"].mean())
print(peopleData1.groupby("gender")["height"].agg([min, max, mean,]))

peopleData2 = pd.read_csv("resources/peopleDataPractise1_duplicates.csv")
print(peopleData2.head(10))
print(peopleData2.duplicated().sum())
peopleData3 = peopleData2.drop_duplicates(subset=['first_name']).reset_index(drop=True)
print(peopleData3.duplicated().sum())
#peopleData4 = peopleData3.reset_index(drop=True)
print(peopleData3.head(10))

peopleData3 = peopleData2.drop_duplicates(subset=['id'], keep='last')
print(peopleData3.duplicated().sum())
peopleData3.index += 0 
print(peopleData3.head(10))
"""