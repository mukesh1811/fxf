import requests
import os
from zipfile import ZipFile
import pandas as pd

    # path = "https://www.nseindia.com/content/historical/EQUITIES/2019/OCT/cm03OCT2019bhav.csv.zip"

path = "https://www.nseindia.com/content/historical/EQUITIES/2019/"

months = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT"]

#df_initiated = False

for month in months:

    this_month_path = path + month + "/"

    for day in range(1,32):
        
        this_file = "cm" + str(day).zfill(2) + month + "2019bhav.csv.zip"
        this_file_path = this_month_path + this_file
        local_path = "C://Stuff/FxF/nse/dataAutoDownload/"
        print(this_file_path)

        # URL of the file to be downloaded 
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

            ###adding it to dataframe
            #local_this_file_in_csv = local_this_file.replace(".zip","")

            #if df_initiated:
                
            #    df.append(pd.read_csv(local_this_file_in_csv))
            #    #df.concat(pd.read_csv(local_this_file_in_csv))

            #else:
            #    df = pd.read_csv(local_this_file_in_csv)
            #    df_initiated = True

        else: 
            this_file_as_txt = this_file.replace(".csv.zip",".txt")
            
            with open(local_path + this_file_as_txt,'w') as f:
                f.write("FileNotFound")
                f.close()

        
        
#df.to_excel(local_path + "master_db.xlsx")