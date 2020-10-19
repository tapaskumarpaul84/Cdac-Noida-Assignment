# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:38:53 2020

@author: TAPAS KUMAR PAUL
"""


import pandas as pd
import numpy as np


##1. Write a Pandas program to create and display a one-dimensional array-like object containing an
#array of data.

arr=np.array(['sun','mon','tue','wed','thu'])
print("Array of data is:",arr)
ser=pd.Series(arr)
print("The Pandas series is:")
print(ser)
print("Dimension of array:",ser.ndim)



##2. Write a Pandas program to convert a Panda module Series to Python list. Display the list and it’s
#type.

data=(6,5,2,4,3,8)
ser=pd.Series(data)
print("Series of data:")
print(ser)
lis=ser.values.tolist()
print("List of data:",lis)


##3. Write a Python program to add, subtract, multiple and divide two Pandas Series.


ser1=pd.Series([2,4,5,3])
ser2=pd.Series([3,2,1,6])
print("First Series:\n",ser1)
print("Second Series:\n",ser2)
print("Addition of two series:\n",ser1+ser2)
print("First Series - second series:\n",ser1-ser2)
print("Multiplication of two series:\n",ser1*ser2)
print("First series divide by second series:\n",round(ser1/ser2,2))


##4. Write a Python program to get the largest integer smaller or equal to the 
#division of the inputs.


ser=pd.Series([5,3,6,7,4])
print("Series of data:\n",ser)
n=int(input("Enter the Divisor:"))
ser1=ser.floordiv(n)
print("the largest integer smaller or equal to the division")
print(ser1)


##5. Write a Python program to convert a dictionary to a Pandas series.

dic={'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
print("Dictionary is:\n",dic)
ser=pd.Series(dic)
print("Converted series is:\n",ser)


##6. Write a Pandas program to convert a NumPy array to a Pandas series.

arr=np.array([3,5,4,8,2])
print("Numpy array is:\n",arr)
ser=pd.Series(arr)
print("Pandas Series is:\n",ser)



##7. Write a Pandas program to change the data type of given a column or a Series.

ser=pd.Series([5,4,5.78,3.32,'tapas',6])
print("Data Series is:",ser)
print("Series convert to numeric data:\n")
ser1=pd.to_numeric(ser,errors='coerce')
print("converted Series:")
print(ser1)


##8. Write a Pandas program to convert a given Series to an array.

ser=pd.Series([6,7,5,8,4])
print("Pandas series:\n",ser)
arr=np.array(ser.values.tolist())
print("Numpy array is:\n")
print(arr)


##9. Write a Pandas program to sort a given Series.

ser=pd.Series([6,7,5,8,4])
print("Pandas series:\n",ser)
ser2=ser.sort_values(ascending=True)
print("Sorted series of given series:\n",ser2)



##10. Write a Pandas program to add some data to an existing Series.

ser=pd.Series([6,7,5,8,4])
print("Pandas series:\n",ser)
ser2=ser.append(pd.Series([9,10]),ignore_index=True)
print("New series is:\n",ser2)



##11. Write a Pandas program to create the mean and standard deviation of the data 
#of a given Series.

ser=pd.Series([6,7,5,8,4,9,10])
print("Pandas Series is:\n",ser)
print("Mean of the Series=",ser.mean())
print("Standard Deviation of the Series=",round(ser.std(),2))