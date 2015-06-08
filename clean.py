import json
import zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# reading training data
zf = zipfile.ZipFile('../input/train.csv.zip')
df = pd.read_csv(zf.open('train.csv'), converters={'POLYLINE': lambda x: json.loads(x)[-1:]})
latlong = np.array([[p[0][1], p[0][0]] for p in df['POLYLINE'] if len(p)>0])

# cut off long distance trips
lat_low, lat_hgh = np.percentile(latlong[:,0], [2, 98])
lon_low, lon_hgh = np.percentile(latlong[:,1], [2, 98])

# find NAs
nans = df.count(0)



# sort data to see individual taxi trips
df[0:10000].sort(['TAXI_ID'])

df[df.TAXI_ID==20000001]
