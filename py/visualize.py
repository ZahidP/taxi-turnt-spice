
import json
import zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# reading training data
zf = zipfile.ZipFile('/Users/zahidpanjwani/Desktop/Code/Kaggle/Taxi-Trajectory/train.csv.zip')
df = pd.read_csv(zf.open('train.csv'), converters={'POLYLINE': lambda x: json.loads(x)[-1:]})

df_sort = df[0:10000].sort('TIMESTAMP')

def plotFigure(image,season):
    plt.figure()
    ax = plt.subplot(1,1,1)
    plt.imshow(image)
    plt.axis('off')
    plt.title('Taxi trip end points')
    fName = "end_points_" + season + ".png"
    plt.savefig(fName)

def subsetData(df2,start,end):
    df1 = df2[start:end]
    df1.sort('TIMESTAMP')
    latlong = np.array([[p[0][1], p[0][0]] for p in df1['POLYLINE'] if len(p)>0])
    # cut off long distance trips
    lat_low, lat_hgh = np.percentile(latlong[:,0], [2, 98])
    lon_low, lon_hgh = np.percentile(latlong[:,1], [2, 98])
    # create image
    bins = 513
    lat_bins = np.linspace(lat_low, lat_hgh, bins)
    lon_bins = np.linspace(lon_low, lon_hgh, bins)
    H2, _, _ = np.histogram2d(latlong[:,0], latlong[:,1], bins=(lat_bins, lon_bins))
    img = np.log(H2[::-1, :] + 1)
    return img

img = subsetData(df,0,25000)
img2 = subsetData(df,25001,50000)
img3 = subsetData(df_sort,500,5050)

plotFigure(img,'summer')
plotFigure(img2,'fall')
plotFigure(img3,'day')
