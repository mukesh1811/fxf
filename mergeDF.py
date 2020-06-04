import os
import pandas as pd

df = pd.DataFrame()

dest_path = "D://myMisc/dev/pp/data/"
daily_files_path = "D://myMisc/dev/pp/data/daily/"

count = 0


for file in os.listdir(daily_files_path):
    
    count = count + 1

    df = df.append(pd.read_csv(daily_files_path + file),sort=False)
    
print(count)
print(len(df)) 
df.to_csv(dest_path + "master_db.csv",index=False)