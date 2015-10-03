# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:28:09 2015

@author: 570360
"""
import numpy as np
import pylab
import matplotlib.pyplot as plt
import matplotlib.dates
from mpl_toolkits.axes_grid1 import make_axes_locatable
import datetime as DT
from matplotlib.dates import date2num
from pandas import DataFrame, read_csv
import pandas as pd
import sys # only to determine Python version number
import csv
filename="C:/Users/570360/Documents/Exxon_Datascience_Team/Anomaly Detection/meas/A-1__1002_0_25.txt"
# http://cs.smith.edu/dftwiki/index.php/MatPlotLib_Tutorial_1
#TODO more items need to be finished here
df=pd.read_csv(filename)
df1=df.drop(df.index[[0,1,2,3,4]])
df=None # free up unused space





lDFAmp=[]
lDFA_small=[]
x=[]
y=[]
j=0
i=0
avg_amp=0.0
count=0;
#with open(filename, 'rb') as csvfile:
f=open(filename,'rb')
    #row_reader = csv.reader(csvfile, delimiter=' ')

i1=0
#while i1<20:
##    f.readline()
#    i1+=1

    
line=f.readline()
line=line.strip("\r\n")
c=line.split(" ")
b_prior=filter(None,c)
if (i>18):
    x1=b_prior[0].split(".")
    cx=x1[1]+"/"+x1[0]+"/"+x1[2]
    b_prior[0]=cx
    b_prior[3]=b_prior[3].strip('\r\n')

while line:

    line=f.readline()
    c=line.split(" ")
    b=filter(None,c)

   
    if (j>150):
        break
   
    if (i<20):

        lDFAmp.append(b)
        b_prior=b


    if (i>=20):

        if b:           #b cannot be null i.e. b has to be logical True

            x1=b[0].split(".")
            cx=x1[1]+"/"+x1[0]+"/"+x1[2]
            b[0]=cx
            b[3]=b[3].strip('\r\n')
            lDFAmp.append(b)
            
            avg_amp=avg_amp+float(b_prior[3])
            if b[0]!=b_prior[0]: # this should check item 0 not 3         
                j+=1 #new day
                
                if (j==1): #first day will otherwise be repeated
                    x1=b_prior[0].split(".")
                    cx=x1[1]+"/"+x1[0]+"/"+x1[2]
                    b_prior[0]=cx
                    b_prior[3]=b_prior[3].strip('\r\n')
                if (j>1):
                    x.append(b_prior[0])
                    y.append(avg_amp)
                    avg_amp=0.0
                    count=0;                
                    print "here",j, i,lDFAmp[i-1],b,len(lDFAmp)
#                x.append(lDFAmp[i-1][2])
#                y.append(lDFAmp[i-1][3])
    b_prior=b
    i=i+1
    
    
plt.title("Amplitude vs. Frequency")
plt.xlabel("Frequency (Hz) ... transducer 5")
plt.ylabel("| FFT amplitude | ")

   
# Plotting stuff here ...

fig = plt.figure()
ax = fig.gca()
ax=plt.axes()

from matplotlib.dates import YearLocator, MonthLocator, DateFormatter,WeekdayLocator
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

years = YearLocator()   # every year
months = MonthLocator()  # every month
days=WeekdayLocator()
yearsFmt = DateFormatter('%M/%Y')
dFmt=DateFormatter("%m %d %y")

loc = WeekdayLocator(byweekday=WE, interval=3)

#major_locator=months
ax.xaxis.set_major_locator(loc)
ax.xaxis.set_minor_locator(loc)
ax.xaxis.set_major_formatter(dFmt)

ax.xaxis_date()
ax.xaxis.grid(True,which="major")
ax.autoscale_view()

plt.plot_date(x,y,'-')
ax.xaxis.set_major_locator(loc)

plt.xticks(rotation=45) 
plt.plot(x,y,c='k')

plt.show()
 
plt.figure()
columns=['frequency','amplitude']

# http://nbviewer.ipython.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/04%20-%20Lesson.ipynb
df2=pd.DataFrame(x)
df2.columns=['Date']
df2['Freq']=y
#http://pandas.pydata.org/pandas-docs/stable/visualization.html#visualization-scatter
df2.plot(x='Date',y='Freq')
plt.xticks(rotation=25)
ax.xaxis.set_major_locator(loc)
df3=pd.DataFrame(lDFAmp)
df4=df3[7:]  # remove the first seven rows
df3=None
df4.columns=['Date','Time','Freq','Amp',"Junk","Junk2"]
del df4["Junk"]
del df4["Junk2"]
df4['Amp']=df4['Amp'].map(lambda x: x.rstrip('\r\n'))
df4['Amp']=df4[['Amp','Freq']].astype(float)
g1=df4.groupby(["Date","Time"]).count()
g1.head()
g1=df4.groupby(["Date","Time"]).mean()
#  http://pandas.pydata.org/pandas-docs/stable/groupby.html
#TODO finish out binning
#TODO establish on github and change a few things for the better mmm
df5=df4
binsize=50 #bin frequency width in Hz
One_bin=1.0/binsize
df5['Bin']=(df4['Freq'].astype(float))*float(One_bin)
df5['Bin']=df5['Bin'].astype(int)
df5['Bin']=((df4['Freq'].astype(float))*float(One_bin)).astype(int)
g2=df5.groupby(["Date","Time","Bin"]).mean()
g2.head(1000).plot()
#TODO  now work on binned data
#TODO remove this
