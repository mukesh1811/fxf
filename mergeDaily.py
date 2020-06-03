import requests
from datetime import datetime
import os
from zipfile import ZipFile
import pandas as pd

year = datetime.now().strftime("%Y")
month = datetime.now().strftime("%b").upper()
day = str(int(datetime.now().strftime("%d")))


# path = "https://www.nseindia.com/content/historical/EQUITIES/2019/OCT/cm03OCT2019bhav.csv.zip"
this_file_path = "https://www.nseindia.com/content/historical/EQUITIES/" + year + "/" + month + "/cm" + day + month + year + "bhav.csv.zip"
this_file = "/cm" + day + month + year + "bhav.csv.zip"

local_path = "C://Stuff/FxF/nse/dataAutoDownload/"

r = requests.get(this_file_path) # create HTTP response object

if r.status_code == 200:

    local_this_file = local_path + this_file
                
    with open(local_this_file,'wb') as f:
            
                # Saving received content as a zip file in 
                # binary format 
            
                # write the contents of the response (r.content) 
                # to a new file in binary mode. 
        f.write(r.content)
        f.close()

    with ZipFile(local_this_file, 'r') as zip: 
        zip.extractall(path=local_path)

    
    os.remove(local_this_file)

    #merging to master_db
    df = pd.read_csv(local_this_file.replace(".zip",""))
    df = df.append(pd.read_csv(local_path + "master_db.csv"))
    df.to_csv(local_path + "master_db.csv",index=False)

else: 
            
    this_file_as_txt = this_file.replace(".csv.zip",".txt")
            
    with open(local_path + this_file_as_txt,'w') as f:
        
        f.write("FileNotFound")
        f.close()