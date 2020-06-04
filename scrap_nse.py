import requests
import os
from zipfile import ZipFile
import pandas as pd
import calendar
from datetime import datetime as dt


yr = 2010
months_list = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]

# path = "https://archives.nseindia.com/content/historical/EQUITIES/2019/OCT/cm03OCT2019bhav.csv.zip"
path = "https://archives.nseindia.com/content/historical/EQUITIES/" + str(yr) + "/"

months = months_list #["AUG","SEP","OCT","NOV","DEC"]

for month in months:

    this_month_path = path + month + "/"

    for day in range(1,32):
        
        valid_date = True
        try:
            calendar.weekday(yr,months_list.index(month) + 1,day)
        except:
            # Feb does not contain 30 and 31
            valid_date = False
        
        if valid_date and calendar.weekday(yr,months_list.index(month) + 1,day) not in [5,6]: #ignoring sat and sun
        
            this_file = "cm" + str(day).zfill(2) + month + str(yr) + "bhav.csv.zip"
            this_file_path = this_month_path + this_file
            local_path = "D://myMisc/dev/pp/data/"
            print(this_file_path)
            print(dt.now())
            # URL of the file to be downloaded 
            try:
                
                r = requests.get(url=this_file_path) # create HTTP response object    
            
            except :
                
                this_file_as_txt = this_file.replace(".csv.zip",".txt")
                
                with open(local_path + this_file_as_txt,'w') as f:
                    f.write("FileNotFound")
                    f.close()

            else:
                
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
                # local_this_file_in_csv = local_this_file.replace(".zip","")

                # df = df.append(pd.read_csv(local_this_file_in_csv))
                
                # if df_initiated:
                    
                #    df.append(pd.read_csv(local_this_file_in_csv))
                #    #df.concat(pd.read_csv(local_this_file_in_csv))

                # else:
                #    df = pd.read_csv(local_this_file_in_csv)
                #    df_initiated = True

        
        
# df.to_excel(local_path + "master_db.xlsx")