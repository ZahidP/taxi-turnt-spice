import json
import zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

df = pd.read_csv('/Users/zahidpanjwani/Desktop/Code/Kaggle/Taxi-Trajectory/datasets/df_train.csv',converters={'POLYLINE': lambda x:json.loads(x)})

df = df.drop('Unnamed: 0',1)

def countPoly(polyList):
    len(polyList)


df['POLYCOUNT'] = df.apply(func, axis=1)

#for index, row in df_train.iterrows():




#(d, h, m) = a.split(':')
df.POLY_AVG = df.POLYLINE.split('],')
