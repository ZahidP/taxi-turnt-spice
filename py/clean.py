import json
import zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime


# reading training data
# #####  zf = zipfile.ZipFile('../input/train.csv.zip')
df = pd.read_csv('/Users/zahidpanjwani/Desktop/Code/Kaggle/Taxi-Trajectory/datasets/small_df.csv')


{n[0] : str(n[1]) for n in l}
df_train = df[0:10000]
df_test = df[40001:49999]
df_train.insert(len(df_train.columns),'hour',0)
arr = df_train.as_matrix()

# sort data by timestamp
# add hour to dataframe
# this takes a long time only do it once
# very inefficient! fix it
for index, row in df_train.iterrows():
    a = datetime.datetime.fromtimestamp(row.TIMESTAMP).strftime('%d:%H:%M')
    (d, h, m) = a.split(':')
    result = int(h) + int(m)/60
    df_train.ix[index,'hour'] = result



df_train.to_csv("/Users/zahidpanjwani/Desktop/Code/Kaggle/Taxi-Trajectory/datasets/df_train.csv",sep=",")
