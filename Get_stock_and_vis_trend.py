#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 02:06:36 2020

@author: meshal
"""
import numpy as np

import re
import time

import investpy
import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn.preprocessing import MinMaxScaler

#For history data for Stock

df = investpy.get_stock_historical_data(stock='PFE',
                                        country='United States',
                                        from_date='01/01/2005',
                                        to_date='01/12/2020')
print(df.head())


#Get The Profile 
fizer_profile = investpy.get_stock_company_profile(stock='PFE' , country='United States')

#Featch the trend
df['Close'].plot(figsize=(20,10), linewidth=5, fontsize=20)

close = df[['Close']]
close.rolling(12).mean().plot(figsize=(20,10), linewidth=5, fontsize=20)


open_price = df[['Open']]
open_price.rolling(12).mean().plot(figsize=(20,10), linewidth=5, fontsize=20)

df_rm = pd.concat([close.rolling(12).mean(), open_price.rolling(12).mean()], axis=1)
df_rm.plot(figsize=(20,10), linewidth=5, fontsize=20)



#Take The Trend from data
import statsmodels.api as sm
df['Close'].plot()
fizer_open , fizer_close  = sm.tsa.filters.hpfilter(df['Close'])

df['trend'] = fizer_close
df[['Close' , 'trend']].plot()


#setting index as date
df['Date'] = pd.to_datetime(df['Date'])

#Visulalize the closing and trend 
#Data
plt.figure(figsize=(16,8))
plt.title('Fizer Price History')
plt.plot(df)
plt.xlabel('Date' , fontsize=18)
plt.ylabel('Fizer Price USD ($)' ,fontsize=18)
plt.show()

#Close
plt.figure(figsize=(16,8))
plt.title('Close Price History')
plt.plot(df['Close'])
plt.xlabel('Date' , fontsize=18)
plt.ylabel('Close Price USD ($)' ,fontsize=18)
plt.show()

#Trend
plt.figure(figsize=(16,8))
plt.title('trend Price History')
plt.plot(df['trend'])
plt.xlabel('Date' , fontsize=18)
plt.ylabel('trend Price USD ($)' ,fontsize=18)
plt.show()

#Volume Price
plt.figure(figsize=(16,8))
plt.title('Volume Price History')
plt.plot(df['Volume'])
plt.xlabel('Date' , fontsize=18)
plt.ylabel('Volume Price USD ($)' ,fontsize=18)
plt.show()
