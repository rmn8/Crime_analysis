import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.colors as colors
print "A"
df = pd.read_csv('../data/crime_red.csv')
df_arrest=df[(df['Arrest']==True) | (df['Domestic']==True)]
#Year Bar Plot

Year_count=pd.DataFrame({'count' : df.groupby( [ "Years"] ).size()}).reset_index()
width = 1/1.5
y_pos = np.arange(len(Year_count['Years']))
fig1 = plt.figure()
plt.bar(y_pos, Year_count['count'], width, color="blue")
plt.xlabel('Year')
plt.ylabel('No. of Crimes commited')
plt.xticks(y_pos, Year_count['Years'])
plt.title('Crimes Commited in Chicago from 2010-2017')
fig1.savefig('../graph/Bar_Crime.png')

# Crime by Year

Date_count=pd.DataFrame({'count' : df.groupby( [ "Date"] ).size()}).reset_index()
Date_Arrest_count=pd.DataFrame({'count' : df_arrest.groupby( [ "Date"] ).size()}).reset_index()
All_Arrest_df= pd.merge(Date_count,Date_Arrest_count, on=['Date'])

fig2 = plt.figure()
plt.plot(np.arange(len(All_Arrest_df['Date'])),All_Arrest_df['count_x'], 'b-', label='Crime')
plt.ylabel('No. of Crimes')
plt.xlabel('Year')
plt.xticks([0,0+365,365+366,365+366+365,365+366+365+365,365+366+365+365+365,365+366+365+365+365+366,365+366+365+365+365+366+365],['2010','2011','2012','2013','2014','2015','2016','2017'])
plt.title('Crimes Commited in Chicago from 2010-2017 Time Line')
fig2.savefig('../graph/Line_Crime.png')

#Arrest/Crime 

Date_count=pd.DataFrame({'count' : df.groupby( [ "Date"] ).size()}).reset_index()
Date_Arrest_count=pd.DataFrame({'count' : df_arrest.groupby( [ "Date"] ).size()}).reset_index()
All_Arrest_df= pd.merge(Date_count,Date_Arrest_count, on=['Date'])
All_Arrest_df['Percent']=(All_Arrest_df['count_y']/All_Arrest_df['count_x'])*100
fig3 = plt.figure()
plt.plot(np.arange(len(All_Arrest_df['Date'])),All_Arrest_df['Percent'], 'r-', label='Percent')
plt.ylabel('% of Arrests Made')
plt.xlabel('Year')
plt.xticks([0,0+365,365+366,365+366+365,365+366+365+365,365+366+365+365+365,365+366+365+365+365+366,365+366+365+365+365+366+365],['2010','2011','2012','2013','2014','2015','2016','2017'])
plt.title('% of Arrests made in Chicago from 2010-2017 Time Line')
fig3.savefig('../graph/Line_Arrest.png')


#Heat Map of each district crime

Year_District_count=df.groupby( [ "Years","District"] ).size().unstack(level=1)
Year_District_count=Year_District_count.div(Year_District_count.sum(axis=1), axis=0)
fig4 = plt.figure()
plt.pcolor(Year_District_count,cmap='binary')
plt.yticks(np.arange(len(Year_District_count.index)), np.abs(Year_District_count.index))
plt.xticks(np.arange(0.5,len(Year_District_count.columns)),np.array(Year_District_count.columns).astype(int),ha='center')
plt.colorbar()
plt.ylabel('Year')
plt.xlabel('District')
plt.title('Heat Map of crimes in Chicago By Districts')
fig4.set_size_inches(18.5, 10.5)
fig4.savefig('../graph/Heatmap_District.png', dpi=100)


#Box Plot

Year_District_count=df.groupby( [ "Years","District"] ).size().unstack(level=1)
Year_District_Arrest_count=df_arrest.groupby( [ "Years","District"] ).size().unstack(level=1)
fig5 = plt.figure()
ax = fig5.add_subplot(111)
bp=ax.boxplot(Year_District_count.as_matrix(),patch_artist=True)
for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
	plt.setp(bp[element], color='blue')
for patch in bp['boxes']:
        patch.set(facecolor='cyan')
bp=ax.boxplot(Year_District_Arrest_count.as_matrix(),patch_artist=True)
for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
	plt.setp(bp[element], color='red')
for patch in bp['boxes']:
        patch.set(facecolor='tan')

plt.xticks(np.arange(1,len(Year_District_count.columns)+1),np.array(Year_District_count.columns).astype(int),ha='center')
plt.ylabel('No. of Crimes commited')
plt.xlabel('District')
plt.title('Box Plots of Crime commited and Arrests made')
fig5.savefig('../graph/BoxPlot_District.png')


#Pie Plot of most frequent crime month

Month_count=pd.DataFrame({'count' : df.groupby( [ "Months"] ).size()}).reset_index()
col=['red','blue','green','orange','violet','indigo','grey','yellow','white','brown','pink','purple']
fig6 = plt.figure()
plt.pie(Month_count['count'], labels=Month_count['Months'],colors=col,autopct='%1.1f%%',shadow=True, startangle=140)
plt.title('Pie Chart Of crimes commited by Months')
fig6.savefig('../graph/Pie_month.png')

#Pie Plot of most frequent crime time
TOD_count=pd.DataFrame({'count' : df.groupby( [ "Time Of Day"] ).size()}).reset_index()
fig7 = plt.figure()
col=['red','blue','green','orange']
plt.pie(TOD_count['count'], labels=TOD_count['Time Of Day'],autopct='%1.1f%%',shadow=True,colors=col, startangle=140)
plt.title('Pie Chart Of crimes commited by Time of Day')
fig7.savefig('../graph/Pie_TOD.png')

