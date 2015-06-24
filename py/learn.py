import json
import zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from sklearn import tree
from sklearn import preprocessing


df = pd.read_csv("/Users/zahidpanjwani/Desktop/Code/Kaggle/Taxi-Trajectory/datasets/df_train_2.csv")
testSet = df[0:500].as_matrix()
# subset the data
test_small = testSet[:,2:10]
test_small2 = testSet[:,19:25]
test_set = np.concatenate((test_small, test_small2), axis=1)
# create predictor and response arrays
predictors = test_set[:,0:13]
response = test_set[:,13]
predictors = np.delete(predictors,10,1)
# process the data
arrW = predictors.shape[1]
uniques = []
le = preprocessing.LabelEncoder()
for (i in range(0,arrW)):
    uni = np.unique(predictors[:,i])
    uniques.append(uni)
    


predictors = le.transform(predictors)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(predictors, response)

print(clf)
