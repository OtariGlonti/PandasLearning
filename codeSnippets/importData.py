import pandas as pd
from pathlib import Path

#path = os.path.dirname(os.path.realpath("/Users/otariglonti/Desktop/pokemon_dataFromDesktop.csv"))
#sys.path.append(path)
#print(path)
#pokemon_data = pd.read_csv("resources/pokemon_data.csv")
#chunksize = 10 ** 6
#for chunk in pd.read_csv("resources/pokemon_data.csv", chunksize=chunksize):
#    process(chunk)

#print(pokemon_data.head(15))
#print(pokemon_data['Name'].head(5))
#print(pokemon_data.shape)
#pokemon_data1= pd.read_csv(path)
filepath = f"{Path(__file__).parent.parent}/resources/pokemon_data.csv"
TextFileReader = pd.read_csv(filepath, chunksize=100)  # the number of rows per chunk
dfList = []
for df in TextFileReader:
    dfList.append(df)

df = pd.concat(dfList,sort=False)
print(dfList)
