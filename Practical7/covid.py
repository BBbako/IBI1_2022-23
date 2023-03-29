import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/Asus/Downloads")
covid_data = pd.read_csv("full_data.csv")
#the code to show the second column from every 100th row from the first 1000 rows
print(covid_data.iloc[0:1001:100,1])
#the code to use a Boolean to show “total cases” for all rows correspondingto Afghanistan.
my_column=[False,True,False,False,False,False]
data=covid_data.iloc[:,my_column]
#find the number of rows
print(data)
print(covid_data.head(5))
i=0
b=True  #the Boolean to show whether the data is from Afghanistan or not
row1=[] #the list to show the row of Afghanistan
for i in range(7996):
  if data.iloc[i,0]=="Afghanistan":
    b=True
  else:
    b=False
  c=[b] #change the Boolean b to a list
  row1=row1+c
print(covid_data.iloc[row1,4])
#5.Examining the situation on 31 March
i=0
b=True
row2=[]
for i in range(7996):
  if covid_data.iloc[i,0]=="2020-03-31":
    b=True
  else:
    b=False
  c=[b]
  row2=row2+c
new_data=covid_data.iloc[row2,1:4]
newcases=new_data.iloc[:,1]
newdeaths=new_data.iloc[:,2]
print(new_data)
#the mean number of new cases
print(newcases.mean())
#the mean number of new deaths
print(newdeaths.mean())
newcases.plot.box(title="new cases")
plt.show()
newdeaths.plot.box(title="new deaths")
plt.show()
# plot both new cases and new deaths worldwide over time
covid_dates=covid_data.iloc[:,0]
covid_new_cases=covid_data.iloc[:,2]
covid_new_deaths=covid_data.iloc[:,3]
plt.plot(covid_dates, covid_new_cases, 'b+')
plt.show()
plt.plot(covid_dates,covid_new_deaths,'r+')
plt.show()
#the code to solve the question in question.txt.
i=0
d=True
row3=[]
for i in range(7996):
  if data.iloc[i,0]=="Germany":
    d=True
  else:
    d=False
  e=[d] 
  row3=row3+e
Germany_total_cases=covid_data.iloc[row3,4]
i=0
d=True
row3=[]
for i in range(7996):
  if data.iloc[i,0]=="China":
    d=True
  else:
    d=False
  e=[d] 
  row3=row3+e
China_total_cases=covid_data.iloc[row3,4]
Germany_total_cases.plot.box(title="Germany")
plt.show()
China_total_cases.plot.box(title="China")
plt.show()
