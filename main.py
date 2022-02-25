import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from cgi import print_environ
from hashlib import sha224
from traceback import print_exception
from convexHull import *
from sklearn import datasets


data = datasets.load_iris()
#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
print(df.shape)
df.head()

bucketInput = []

#visualisasi hasil ConvexHull
plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('Petal Width vs Petal Length')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
# for i in range(len(data.target_names)):
for i in range(0,3):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    bucketInput.append(bucket)
    
    # ConvexHull Divide & Conquer
    hull = findConvex(bucketInput[i]) # Implementasi Convex Hull

    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
        
    for elmt in hull:
        plt.plot([x for x,_ in hull], [y for _,y in hull], colors[i])
        
plt.legend()
plt.show()