import json
import zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# reading training data
zf = zipfile.ZipFile('../input/train.csv.zip')
df = pd.read_csv(zf.open('train.csv'))  # subset the data due to speed restrictions

df_train = df[0:10000]
df_test = df[10001:15000]

# cut off long distance trips
lat_low, lat_hgh = np.percentile(latlong[:,0], [2, 98])
lon_low, lon_hgh = np.percentile(latlong[:,1], [2, 98])

# find NAs
nans = df.count(0)


# sort data to see individual taxi trips
df[0:10000].sort(['TAXI_ID'])
