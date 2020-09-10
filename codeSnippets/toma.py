import pandas as pd

tomaData1 = pd.read_csv("resources/TomaData1.csv")
#print(tomaData1.head())
print(tomaData1.columns)
#print(tomaData1.dtypes)
#print(tomaData1["installs"].unique())
tomaData1NanClean = tomaData1.fillna(-1) 
#print(tomaData1NanClean["installs"].unique())

tomaData1NanClean["installs"] = tomaData1NanClean["installs"].str.replace("APP_INSTALLS", "-2")
tomaData1NanClean["installs"] = tomaData1NanClean["installs"].astype("float")
#print(tomaData1NanClean.dtypes)
#tomaData2 = tomaData1NanClean
print(tomaData1NanClean["status"].unique())
tomaData1NanClean["status"] = tomaData1NanClean["status"].astype("category")
#print(tomaData1NanClean.dtypes)
#print(tomaData1NanClean["status"].unique())
#print(tomaData1NanClean.groupby("status")["installs"].count())
#print(tomaData1NanClean.dtypes)
print(tomaData1NanClean["budget_spend"].unique())
tomaData1NanClean["budget_spend"] = tomaData1NanClean["budget_spend"].str.replace('#23842976092010171', "-2")
print(tomaData1NanClean["budget_spend"].unique())
tomaData1NanClean["budget_spend"] = tomaData1NanClean["budget_spend"].astype("float")
print(tomaData1NanClean.dtypes)
print(tomaData1NanClean["revenue"].unique())
tomaData1NanClean["revenue"] = tomaData1NanClean["revenue"].str.replace('-1', "UNCLEAR")
tomaData1NanClean["revenue"] = tomaData1NanClean["revenue"].astype("category")
print(tomaData1NanClean.dtypes)
tomaData1NanClean["objective"] = tomaData1NanClean["objective"].astype("category")
print(tomaData1NanClean["objective"].unique())
print(tomaData1NanClean.info())
tomaDataClean = tomaData1NanClean.to_csv("resources/TomaDataClean.csv")

#tomaDataRemoved1 = tomaData1.loc[tomaData1["installs"] == "APP_INSTALLS"]

#tomaData1.drop(tomaData1[tomaData1.installs].str.contains("APP_INSTALLS"))

#df[df['Product ID'].str.contains("foo") == True]
#print(tomaData1["installs"].unique())
#tomaData1["installs"] = tomaData1["installs"].astype('float')
#print(tomaData1.dtypes)
