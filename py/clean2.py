import json
import zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import math
import geo_metrics as gmt


# reading training data
# #####  zf = zipfile.ZipFile('../input/train.csv.zip')
df = pd.read_csv('/Users/zahidpanjwani/Desktop/Code/Kaggle/Taxi-Trajectory/datasets/small_df.csv',converters={'POLYLINE': lambda x:json.loads(x)})


#{n[0] : str(n[1]) for n in l}
df_train = df[0:5000]
df_test = df[30001:34999]
df_train.insert(len(df_train.columns),'hour',0)
df_train.insert(len(df_train.columns),'lngSt',0)
df_train.insert(len(df_train.columns),'latSt',0)
df_train.insert(len(df_train.columns),'lngNxt',0)
df_train.insert(len(df_train.columns),'latNxt',0)
df_train.insert(len(df_train.columns),'angle',0)
df_train.insert(len(df_train.columns),'lngFin',0)
df_train.insert(len(df_train.columns),'latFin',0)



arr = df_train.as_matrix()

# sort data by timestamp
# add hour to dataframe
# this takes a long time only do it once
# very inefficient! fix it
for index, row in df_train[0:500].iterrows():
    a = datetime.datetime.fromtimestamp(row.TIMESTAMP).strftime('%d:%H:%M')
    (d, h, m) = a.split(':')
    # get hour
    result = int(h) + int(m)/60
    if (result < 6):
        hr = 1
    elif (result >= 6 and result < 9.5):
        hr = 2
    elif (result >= 9.5 and result < 13):
        hr = 3
    elif (result >= 13 and result < 16):
        hr = 4
    elif (result >= 16 and result < 19):
        hr = 5
    else:
        hr = 6
    df_train.ix[index,'hour'] = hr
    # get initial and final position
    if (len(row.POLYLINE) > 0):
        lng = row.POLYLINE[0][0]
        lat = row.POLYLINE[0][1]
        lngFin = row.POLYLINE[len(row.POLYLINE)-1][0]
        latFin = row.POLYLINE[len(row.POLYLINE)-1][1]
        df_train.ix[index,'lngSt'] = lng
        df_train.ix[index,'latSt'] = lat
        zoneSt = gmt.zoning(row.POLYLINE[0][1],row.POLYLINE[0][0])
        df_train.ix[index,'lngStZn'] = zoneSt[1]
        df_train.ix[index,'latStZn'] = zoneSt[0]
        df_train.ix[index,'stZn'] = str(zoneSt[1]) + str(zoneSt[0])
        df_train.ix[index,'lngFin'] = lngFin
        df_train.ix[index,'latFin'] = latFin
        zoneFin = gmt.zoning(latFin,lngFin)
        df_train.ix[index,'lngFinZn'] = zoneFin[1]
        df_train.ix[index,'latFinZn'] = zoneFin[0]
        df_train.ix[index,'finZn'] = str(zoneFin[1]) + str(zoneFin[0])
        # get middle position
        if (len(row.POLYLINE) > 3):
            lngNxt = row.POLYLINE[3][0]
            latNxt = row.POLYLINE[3][1]
            df_train.ix[index,'lngNxt'] = lngNxt
            df_train.ix[index,'latNxt'] = latNxt
            zoneNxt = gmt.zoning(row.POLYLINE[3][1],row.POLYLINE[3][0])
            df_train.ix[index,'nxtZn'] = str(zoneNxt[1]) + str(zoneNxt[0])
            if (lng and lat and lngNxt and latNxt):
                # get angle function
                opp = latNxt*68 - lat*68
                adj = lngNxt*68 - lng*68
                angle = 0
                if (adj > 0.00001):
                    angle = math.atan(opp/adj)
                df_train.ix[index,'angle'] = angle

print(df_train[0:10])
df_train.to_csv("/Users/zahidpanjwani/Desktop/Code/Kaggle/Taxi-Trajectory/datasets/df_train_2.csv",sep=",")
