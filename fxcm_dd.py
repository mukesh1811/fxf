import fxcmpy
import socketio
TOKEN = "48da91a971d8a7f519bfbf6ab60921a20936e6f0"
con = fxcmpy.fxcmpy(access_token=TOKEN, log_level='error', server='demo', log_file='log.txt')
import pandas as pd
import datetime as dt
df1=pd.DataFrame()
df1 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2010,1,1), end=dt.datetime(2010,7,1))
df2=pd.DataFrame()
df2 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2010,7,1), end=dt.datetime(2011,1,1))
df3=pd.DataFrame()
df3 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2011,1,1), end=dt.datetime(2011,7,1))
df4=pd.DataFrame()
df4 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2011,7,1), end=dt.datetime(2012,1,1))
df5=pd.DataFrame()
df5 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2012,1,1), end=dt.datetime(2012,7,1))
df6=pd.DataFrame()
df6 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2012,7,1), end=dt.datetime(2013,1,1))
df7=pd.DataFrame()
df7 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2013,1,1), end=dt.datetime(2013,7,1))
df8=pd.DataFrame()
df8 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2013,7,1), end=dt.datetime(2014,1,1))
df9=pd.DataFrame()
df9 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2014,1,1), end=dt.datetime(2014,7,1))
df10=pd.DataFrame()
df10 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2014,7,1), end=dt.datetime(2015,1,1))
df11=pd.DataFrame()
df11 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2015,1,1), end=dt.datetime(2015,7,1))
df12=pd.DataFrame()
df12 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2015,7,1), end=dt.datetime(2016,1,1))
df13=pd.DataFrame()
df13 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2016,1,1), end=dt.datetime(2016,7,1))
df14=pd.DataFrame()
df14 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2016,7,1), end=dt.datetime(2017,1,1))
df15=pd.DataFrame()
df15 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2017,1,1), end=dt.datetime(2017,7,1))
df16=pd.DataFrame()
df16 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2017,7,1), end=dt.datetime(2018,1,1))
df17=pd.DataFrame()
df17 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2018,1,1), end=dt.datetime(2018,7,1))
df18=pd.DataFrame()
df18 = con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2018,7,1), end=dt.datetime(2019,1,1))
df19=pd.DataFrame()
df19= con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2019,1,1), end=dt.datetime(2019,7,1))
df20=pd.DataFrame()
df20= con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2019,7,1), end=dt.datetime(2020,1,1))
df21=pd.DataFrame()
df21= con.get_candles('GBP/JPY', period='m15', start=dt.datetime(2020,1,1), end=dt.datetime(2020,5,1))
frame = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21]
result = pd.concat(frame)
result.to_csv('D:\final work\result123.csv')
 