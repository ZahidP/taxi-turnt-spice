import json
import zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import math
import geo_metrics as gmt

df = pd.read_csv('/Users/zahidpanjwani/Desktop/Code/Kaggle/Taxi-Trajectory/results/pred1.csv')

df.insert(0,'LONGITUDE',0)
df.insert(0,'LATITUDE',0)
df.insert(0,'TRIP',0)
t = 1

for index, row in df.iterrows():
    lat = 0.001
    lng = 0.001
    trip = 'T' + str(t)
    [lat,lng] = gmt.dezoning(str(row.x))
    #row.LATITUDE = lat
    #row.LONGITUDE = lng
    df.ix[index,'LATITUDE'] = lat
    df.ix[index,'LONGITUDE'] = lng
    df.ix[index,'TRIP'] = lat = trip
    t = t + 1



print(df[0:5])

df.to_csv("/Users/zahidpanjwani/Desktop/Code/Kaggle/Taxi-Trajectory/results/results1.csv",sep=",")
