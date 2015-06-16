import json
import zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import math


# reading training data
# #####  zf = zipfile.ZipFile('../input/train.csv.zip')
df = pd.read_csv('/Users/zahidpanjwani/Desktop/Code/Kaggle/Taxi-Trajectory/datasets/small_df.csv',converters={'POLYLINE': lambda x:json.loads(x)})


#{n[0] : str(n[1]) for n in l}
df_train = df[0:10000]
df_test = df[30001:34999]
df_train.insert(len(df_train.columns),'hour',0)
df_train.insert(len(df_train.columns),'lngSt',0)
df_train.insert(len(df_train.columns),'latSt',0)
df_train.insert(len(df_train.columns),'lngNxt',0)
df_train.insert(len(df_train.columns),'latNxt',0)
df_train.insert(len(df_train.columns),'angle',0)
arr = df_train.as_matrix()

# sort data by timestamp
# add hour to dataframe
# this takes a long time only do it once
# very inefficient! fix it
for index, row in df_train[0:500].iterrows():
    a = datetime.datetime.fromtimestamp(row.TIMESTAMP).strftime('%d:%H:%M')
    (d, h, m) = a.split(':')
    result = int(h) + int(m)/60
    # get initial position
    if (len(row.POLYLINE) > 0):
        lng = row.POLYLINE[0][0]
        lat = row.POLYLINE[0][1]
        # get next position
        if (len(row.POLYLINE) > 3):
            lngNxt = row.POLYLINE[3][0]
            latNxt = row.POLYLINE[3][1]
            df_train.ix[index,'lngNxt'] = lngNxt
            df_train.ix[index,'latNxt'] = latNxt
            if (lng and lat and lngNxt and latNxt):
                # get angle function
                opp = latNxt*68 - lat*68
                adj = lngNxt*68 - lng*68
                angle = 0
                if (adj > 0.00001):
                    angle = math.atan(opp/adj)
                df_train.ix[index,'angle'] = angle
        df_train.ix[index,'lngSt'] = lng
        df_train.ix[index,'latSt'] = lat
        # get angle between initial and next

    df_train.ix[index,'hour'] = result





df_train.to_csv("/Users/zahidpanjwani/Desktop/Code/Kaggle/Taxi-Trajectory/datasets/df_train_2.csv",sep=",")
