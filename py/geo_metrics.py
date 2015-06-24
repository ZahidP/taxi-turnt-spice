import json
import zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import math as math

#df = pd.read_csv('/Users/zahidpanjwani/Desktop/Code/Kaggle/Taxi-Trajectory/datasets/df_train.csv',converters={'POLYLINE': lambda x:json.loads(x)[-1:]})

#df = df.drop('Unnamed: 0',1)

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


# break start points into regions
def zoning(lat,lng):
    #lat = df.latSt
    #lng = df.lngSt
    zoneLng = 1
    zoneLat = 1
    lngMin = -8.64
    lngMax = -8.58
    lngStep = (lngMax-lngMin)/5
    latMin = 41.14
    latMax = 41.18
    latStep = (latMax-latMin)/4
    if (lng <= lngMin):
        zoneLng = 1
    elif (lng > lngMin and lng <= lngMin+lngStep):
        zoneLng = 2
    elif (lng > lngMin+lngStep and lng <= lngMin+lngStep*2):
        zoneLng = 3
    elif (lng > lngMin+lngStep*2 and lng <= lngMin+lngStep*3):
        zoneLng = 4
    elif (lng > lngMin+lngStep*4):
        zoneLng = 5

    if (lat <= latMin):
        zoneLat = 1
    elif (lat > latMin and lat <= latMin+latStep):
        zoneLat = 2
    elif (lat > latMin+latStep and lat <= latMin+latStep*2):
        zoneLat = 3
    elif (lat > (latMin+latStep*3)):
        zoneLat = 4

    return [zoneLat,zoneLng]


def dezoning(zone):
    [zoneLat,zoneLng] = list(zone)
    lat = 0
    lng = 0
    lngMin = -8.64
    lngMax = -8.58
    lngStep = (lngMax-lngMin)/5
    latMin = 41.14
    latMax = 41.18
    latStep = (latMax-latMin)/4
    if (zoneLng == '1'):
        lng = lngMin   #1
    elif (zoneLng == '2'):
        lng = lngMin + lngStep*.5  #1
    elif (zoneLng == '3'):
        lng = lngMin + lngStep*1.5  #2
    elif (zoneLng == '4'):
        lng = lngMin + lngStep*2.5  #3
    elif (zoneLng == '5'):
        lng = lngMin + lngStep*3.5

    
    if (zoneLat == '1'):
        lat = latMin
    elif (zoneLat == '2'):
        lat = latMin + latStep*.5
    elif (zoneLat == '3'):
        lat = latMin + latStep*1.5
    elif (zoneLat == '4'):
        lat = latMin + latStep*2.5

    return [lat,lng]



# count the length of the polyline list
def countPoly(polyList):
    polylength = len(polyList)
    return polylength


# get the initial direction
def initDir(polyList,polylength):
    firstThird = Math.ceil(polylength/3)


def main():
    a = haversDist(40.123,40.123,41.12,41.23)
    print(a)

if __name__ == "__main__":
    main()


#df.insert(len(df_train.columns),'zoneLat',0)
#df.insert(len(df_train.columns),'zoneLng',0)
#df.apply(zoning)

#df['POLYCOUNT'] = df.apply(countPoly, axis=1)

#for index, row in df_train.iterrows():
