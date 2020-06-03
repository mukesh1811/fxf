import os
import pandas as pd

df_initiated = False
local_path = "C://Stuff/FxF/nse/dataAutoDownload/"

count = 0

for file in os.listdir(local_path):
    
    count = count + 1

    if df_initiated:
                
        df = df.append(pd.read_csv(local_path + file))

    else:
        df = pd.read_csv(local_path + file)
        df_initiated = True

    
print(count)
print(len(df)) 
df.to_csv(local_path + "master_db.csv",index=False)