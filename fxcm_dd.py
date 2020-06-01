import fxcmpy
import socketio
TOKEN = "48da91a971d8a7f519bfbf6ab60921a20936e6f0"
con = fxcmpy.fxcmpy(access_token=TOKEN, log_level='error', server='demo', log_file='log.txt')
import pandas as pd
import datetime as dt

df = []
year_list = range(2010,2019)
month_list = [1,7]

for yr in year_list:
    df_temp1 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(yr,1,1), end=dt.datetime(yr,6,30))
    df_temp2 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(yr,7,1), end=dt.datetime(yr,12,31))
    df.append(df_temp1)
    df.append(df_temp2)


result = pd.concat(df)
result.to_csv('/workspace/fxf/test.csv')
 