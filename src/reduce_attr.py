import pandas as pd
import numpy as np
import calendar

df = pd.read_csv('../data/crime.csv', iterator=True, chunksize=100000)
chunks=[]
for chunk in df:
	ch1=chunk[["ID", "Date","IUCR","Primary Type","Arrest","Domestic","District","Ward","Community Area","FBI Code"]]
	ch2=ch1.copy()	
	ch2['Time'] = pd.to_datetime(ch2['Date']).dt.time
	ch2['Date'] = pd.to_datetime(ch2['Date']).dt.date
	[ch2['Hours'],ch2['Minutes'],ch2['Seconds']] =[ch2['Time'].apply(lambda x: x.hour),ch2['Time'].apply(lambda x: x.minute),ch2['Time'].apply(lambda x: x.second)]
	[ch2['Years'],ch2['Months'],ch2['Days']] =[ch2['Date'].apply(lambda x: x.year),ch2['Date'].apply(lambda x: x.month),ch2['Date'].apply(lambda x: x.day)]
	ch2['Months']=ch2['Months'].apply(lambda x: calendar.month_abbr[x])
	ch2.drop(['Time'],axis=1,inplace=True)
	ch2=ch2[['ID','Date','Years','Months','Days','Hours','Minutes','Seconds','IUCR','Primary Type','Arrest','Domestic','District','Ward','Community Area','FBI Code']]
	ch2["Time Of Day"]=ch2["Hours"].apply(lambda x:"Morning" if x>6 and x<=12 else "Afternoon" if x>12 and x<=17 else "Evening" if x>17 and x<=20 else "Night")
	ch2=ch2[(ch2.Years>=2010) & (ch2.Years<=2017)]	
	chunks.append(ch2)
	print(ch2.shape)
	print('a')
df_ac = pd.concat(chunks, ignore_index=True)
print df_ac.shape
df_ac.to_csv('../data/crime_red.csv',index=False)




