# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 21:16:32 2020

@author: TAPAS KUMAR PAUL
"""

import numpy as np

##1. Write a NumPy program to reverse an array (first element becomes last).

arr=np.array(list(map(int,input("Enter the element of array:").split())))
print("The array is:\n",arr)
arr1=arr[::-1]
print("The reversed array is:\n",arr1)


##2. Write a NumPy program to extract all odd numbers from an array.

arr=np.array(list(map(int,input("Enter element of array:").split())))
print("Enter array is:\n",arr)
condition=arr%2!=0
arr1=np.extract(condition,arr)
print("Extracted array is:\n",arr1)


##3. Write a NumPy program to create a 2d array with 1 on the border and 0 inside.

r=int(input("Enter the number of rows:"))
c=int(input("Enter the number of column:"))
array=np.full((r,c),1)
array[1:-1,1:-1]=0
print("The new array is:\n",array)


##4. Write a NumPy program to append values to the end of an array.

arr=np.array(list(map(int,input("Enter the array:").split())))
print("The primary array is:\n",arr)
arr1=list(map(int,input("Append value:").split()))
arr2=np.append(arr,arr1)
print("Appened array is:\n",arr2)


##5. Write a NumPy program to compute the median of flattened given array.

arr=np.array([[3,5,2,4],
              [5,4,8,6],
              [6,4,8,2]])
arr1=arr.flatten()
print("Flattened array is:\n",arr1)
median=np.median(arr1)
print("Median of the flattened array is:",median)


##6. Write a NumPy program to find the most frequent value in an array.

arr=np.array([[3,5,2,4],
              [5,4,8,6],
              [6,4,8,2]])
arr1=arr.flatten()
print("Flattened array is:\n",arr1)
mode=np.bincount(arr1).argmax()
print("Most frequent value is:\n",mode)


##7. Write a NumPy program to check two random arrays are equal or not

a=np.random.randint(0,5,5)
b=np.random.randint(0,5,5)
print("First random array is:\n",a)
print("Second random array is:\n",b)
equal=np.allclose(a,b)
print("Two array are equal or not:",equal)

##user input of a array
a=np.array(list(map(int,input("a=").split())))
b=np.array(list(map(int,input("b=").split())))
print("First random array is:\n",a)
print("Second random array is:\n",b)
equal=np.allclose(a,b)
print("Two array are equal or not:",equal)


##8. Write a NumPy program to get the powers of an array values element-wise.

arr=np.array([[5,1,2,4],
              [3,6,2,5],
              [7,3,5,6]])
power=int(input("Enter the power value:"))
arr1=np.power(arr,power)
print("New array is:\n",arr1)


##9. Write a NumPy program to add, subtract, multiply, divide arguments element-wise.

arr=np.random.randint(1,9,size=(3,3))
print("The 3x3 array is:\n",arr)
add=int(input("Enter add number:"))
print("After Adding each element:\n",np.add(arr,add))

sub=int(input("Enter subtract number:"))
print("After subtracting each element:\n",np.subtract(arr,sub))

mul=int(input("Enter multiply number:"))
print("After multipling each element:\n",np.multiply(arr,mul))

div=int(input("Enter dividend number:"))
print("After dividinging each element:\n",np.around(np.divide(arr,div),decimals=2))


##10. Write a NumPy program to compute the multiplication of two given matrixes.

a=np.array([[3,4,5],
            [4,5,2],
            [3,1,2]])
b=np.array([[2,4,5],
            [4,2,7],
            [3,6,2]])
c=np.multiply(a,b)
print("Element wise multiplication of given matrix:\n",c)
d=np.dot(a,b)
print("Multiplication of two given matrix:\n",d)


##11. Write a NumPy program to Replace all odd numbers in arr with -1


arr=np.random.randint(1,9,size=(3,3))
print("Primary array:\n",arr)
arr1=np.where(arr%2!=0,arr-1,arr)
print("After replacing all odd from the array with -1:\n",arr1)
arr2=np.where(arr%2!=0,-1,arr)
print("After replcing all the odd from the array by -1:\n",arr2)


##12. Replace all odd numbers in arr with -1 without changing arr


arr=np.random.randint(1,9,size=(3,3))
print("Primary array:\n",arr)
print("After replacing all odd from the array with -1:\
      \n",np.where(arr%2!=0,arr-1,arr))
print("After replcing all the odd from the array by -1:\
      \n",np.where(arr%2!=0,-1,arr))


##13. Convert a 1D array to a 2D array with 2 rows

arr_1d=np.arange(8)
print("The dimension of array is:",arr_1d.ndim)
print("Array is:\n",arr_1d)
arr_2d=arr_1d.reshape(2,4)
print("The converted array is:\n",arr_2d)
print("The dimensions of the converted array:",arr_2d.ndim)


##14. Write a numpy program to swap two columns in a 2d numpy array?


arr=np.arange(9).reshape(3,3)
print("primary array is:\n",arr)
arr[:,[0,1]]=arr[:,[1,0]]
print("Swap two column in array:\n",arr)


##15. Write a numpy program to swap two rows in a 2d numpy array?



arr=np.arange(9).reshape(3,3)
print("primary array is:\n",arr)
arr[[0,1],:]=arr[[1,0],:]
print("Swap two row in array:\n",arr)



##16. Write a numpy program to reverse the rows of a 2D array?

arr_2d=np.arange(1,13).reshape(4,3)
print("Primary array is:\n",arr_2d)
arr_row_rev=np.flip(arr_2d,axis=0)
print("Rverse the rows of array:\n",arr_row_rev)


##17. Write a numpy program to reverse the columns of a 2D array?

arr_2d=np.arange(1,13).reshape(4,3)
print("Primary array is:\n",arr_2d)
arr_col_rev=np.flip(arr_2d,axis=1)
print("Rverse the columns of array:\n",arr_col_rev)


