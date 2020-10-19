# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:23:20 2020

@author: TAPAS KUMAR PAUL
"""


import pandas as pd
import numpy as np


##1. Write a Pandas program to get the columns of the DataFrame using iris.csv file.


iris=pd.read_csv("C:\\Users\\TAPAS KUMAR PAUL\\Documents\\iris set.csv")
col=iris.columns
print("The columns of the dataframe is:\n",col)



##2. Write a Pandas program to get the information of the DataFrame (iris.csv file) including data
#types and memory usage.


print("The Information of the iris.csv file or dataframe:\n")
iris.info()



##3. Write a Pandas program to get the details of the third iris flower of the DataFrame (iris.csv file).

print("Details of third iris flower:")
print(iris.loc[2])


##4. Write a Pandas program to count the number of rows and columns of the DataFrame (iris.csv
#file).


print("Number of rows of the datframe:",len(iris.index))
print("Number of columns of the datframe:",len(iris.columns))


##5. Write a Pandas program to get the details of the columns sepal length and sepal width of the
#DataFrame.


print("Details of the columns sepal length and sepal width")
iris[['sepal lenth in cm','sepal width in cm']].describe()