import json
import zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import math as math

df = pd.read_csv('/Users/zahidpanjwani/Desktop/Code/Kaggle/Taxi-Trajectory/datasets/df_train.csv',converters={'POLYLINE': lambda x:json.loads(x)})

df = df.drop('Unnamed: 0',1)

# calculate haversine distance
def haversDist(lat1,lon1,lat2,lon2):
    REarth = 6371
    pi = math.pi
    lat = math.fabs(lat1-lat2)*pi/180
    lon = math.fabs(lon1-lon2)*pi/180
    lat1 = lat1*pi/180
    lat2 = lat2*pi/180
    a = math.sin(lat/2)*math.sin(lat/2)+math.cos(lat1)*math.cos(lat2)*math.sin(lon/2)*math.sin(lon/2)
    d = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
    d = REarth*d
    return d

# count the length of the polyline list
def countPoly(polyList):
    polylength = len(polyList)
    return polylength

# get the initial direction
def initDir(polyList,polylength):
    firstThird = Math.ceil(polylength/3)



#df['POLYCOUNT'] = df.apply(countPoly, axis=1)

#for index, row in df_train.iterrows():
a = haversDist(40.123,40.123,41.12,41.23)
print(a)
