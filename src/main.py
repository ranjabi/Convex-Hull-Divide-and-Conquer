import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from convexHull import *
from sklearn import datasets

def run(data_name):
    if (data_name == "iris sepal"):
        data = datasets.load_iris()
        #create a DataFrame
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df['Target'] = pd.DataFrame(data.target)
        print(df.shape)
        print(df.head())

        bucketInput = []

        #visualisasi hasil ConvexHull
        plt.figure(figsize = (10, 6))
        colors = ['b','r','g']
        
        plt.title('Sepal Width vs Sepal Length')
        plt.xlabel(data.feature_names[0])
        plt.ylabel(data.feature_names[1])
        for i in range(len(data.target_names)):
            bucket = df[df['Target'] == i]
            bucket = bucket.iloc[:,[0,1]].values
            bucketInput.append(bucket)
            # print("bucket: ", i, "\n", bucket)
            
            # ConvexHull Divide & Conquer
            hull = findConvex(bucketInput[i]) # Implementasi Convex Hull

            plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
                
            for elmt in hull:
                plt.plot([x for x,_ in hull], [y for _,y in hull], colors[i])       
    elif (data_name == "iris petal"):
        data = datasets.load_iris()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df['Target'] = pd.DataFrame(data.target)
        print(df.shape)
        print(df.head())

        bucketInput = []

        plt.figure(figsize = (10, 6))
        colors = ['b','r','g']
        
        plt.title('Petal Width vs Petal Length')
        plt.xlabel(data.feature_names[2])
        plt.ylabel(data.feature_names[3])
        for i in range(len(data.target_names)):
            bucket = df[df['Target'] == i]
            bucket = bucket.iloc[:,[2,3]].values
            bucketInput.append(bucket)
            # print("bucket: ", i, "\n", bucket)
            
            hull = findConvex(bucketInput[i])

            plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
                
            for elmt in hull:
                plt.plot([x for x,_ in hull], [y for _,y in hull], colors[i])
    elif (data_name == "breast cancer"):
        data = datasets.load_breast_cancer()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df['Target'] = pd.DataFrame(data.target)
        print(df.shape)
        print(df.head())

        bucketInput = []

        plt.figure(figsize = (10, 6))
        colors = ['b','r','g']
        plt.title('Mean Radius vs Mean Symmetry')
        plt.xlabel(data.feature_names[0])
        plt.ylabel(data.feature_names[8])
        for i in range(len(data.target_names)):
            bucket = df[df['Target'] == i]
            bucket = bucket.iloc[:,[0,8]].values
            bucketInput.append(bucket)
            # print("bucket: ", i, "\n", bucket)
            
            hull = findConvex(bucketInput[i])

            plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
                
            for elmt in hull:
                plt.plot([x for x,_ in hull], [y for _,y in hull], colors[i])

    elif (data_name == "wine"):
        data = datasets.load_wine()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df['Target'] = pd.DataFrame(data.target)
        print(df.shape)
        print(df.head())

        bucketInput = []

        plt.figure(figsize = (10, 6))
        colors = ['b','r','g']
        plt.title('Alcohol vs Malic Acid')
        plt.xlabel(data.feature_names[0])
        plt.ylabel(data.feature_names[1])
        for i in range(len(data.target_names)):
            bucket = df[df['Target'] == i]
            bucket = bucket.iloc[:,[0,1]].values
            bucketInput.append(bucket)
            # print("bucket: ", i, "\n", bucket)
            
            hull = findConvex(bucketInput[i])

            plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
                
            for elmt in hull:
                plt.plot([x for x,_ in hull], [y for _,y in hull], colors[i]) 
    plt.legend()
    plt.show()
    
# Pilih sesuai data yang diinginkan
run("iris sepal")
# run("iris petal")
# run("breast cancer")
# run("wine")