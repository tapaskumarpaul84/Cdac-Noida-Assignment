# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:25:10 2020

@author: TAPAS KUMAR PAUL
"""

###1. Write a NumPy program to get the numpy version and show numpy build configuration.

import numpy as np
print("Version of the numpy is:",np.__version__)
print("Configuration of numpy:")
print(np.show_config())


##2. Write a NumPy program to get help on the add function.

print("Information or get help of add function")
print(help(np.add))

##3. Write a NumPy program to test whether none of the elements of a given array is zero.

mat=np.array(list(map(int,input("Enter element of array:").split())))
print("Entered array is:\n",mat)
print("None of the element is zero:")
print(np.all(mat))

##4. Write a NumPy program to test if any of the elements of a given array is non-zero.

mat1=np.array(list(map(int,input("Enter element of array:").split())))
print("Entered array is:\n",mat1)
print("Any element of the array is nonzero:")
print(np.any(mat1))
print("Position of non zero element in the array:\n",np.nonzero(mat1))

##5. Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a
#Number).
##6. Write a NumPy program to test element-wise for positive or negative infinity.
##7. Write a NumPy program to test element-wise for NaN of a given array.

arr=np.array([1,2,0,np.nan,np.inf])
print("Element wise finiteness:\n",np.isfinite(arr))
print("Element wise check infinite or not:\n",np.isinf(arr))
print("Element wise check not a number:\n",np.isnan(arr))


##8. Write a NumPy program to test element-wise for complex number, real number of a given array.
#Also test if a given number is a scalar type or not.

arr1=np.array([2,3,4+2j,6,2-3j,0j])
print("Element wise real number:\n",np.isreal(arr1))
print("Element wise complex number:\n",np.iscomplex(arr1))
num=3.5
num1=[3.5]
print("Scalar or not:\n",np.isscalar(num))
print("Scalar or not:\n",np.isscalar(num1))


##9. Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and
#less_equal) of two given arrays.

a=np.array(list(map(int,input("Array1 elements:").split())))
b=np.array(list(map(int,input("Array2 elements:").split())))
print("array1",a)
print("array2",b)
print("Greater than:\n",np.greater(a,b))
print("Greater than equal:\n",np.greater_equal(a,b))
print("Less than:\n",np.less(a,b))
print("Less than equal:\n",np.less_equal(a,b))


##10. Write a NumPy program to create an array of 10 zeros, an array of 10 ones, and an array of 10
#fives.

zero=np.zeros([1,10],dtype=np.int)
one=np.full((1,10),1)
five=np.full((1,10),5)
print("Array of 10 zeros:\n",zero)
print("Array of 10 ones:\n",one)
print("Array of 10 fives:\n",five)

##11. Write a NumPy program to create an array of the integers from 30 to70.

arr2=np.arange(30,71)
print("Array from 30 to 70:\n",arr2)

##12. Write a NumPy program to create an array of all the even integers from 30 to 70.

arr2=np.arange(30,71)
cond=arr2%2==0
even=arr2[cond]
print("Array of even integer from 30 to 70:\n",even)

##13. Write a NumPy program to create a 3x3 identity matrix.

identity=np.identity(3,dtype=int)
print("3x3 identity matrix:\n",identity)

##14. Write a NumPy program to generate a random number between 0 and 1.

ran=np.random.uniform(0,1)
print("A Random number from 0 to 1:",ran)

##15. Write a NumPy program to generate an array of 15 random numbers from a standard normal
#distribution.

ran=np.random.normal(0,1,15)#mean=0,std=1,size=15
print("Array of 15 random number of a standard normal distribution:\n",ran)

##16. Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values
#except the first and last.

vec=np.arange(15,55)
print("The vector is:\n",vec)
vec1=vec[1:]
print("New vector is:\n",vec1)

##17. Write a NumPy program to create a vector of length 10 with values evenly distributed between
#5 and 50.

vec=np.linspace(5,50,10)
print("Vector between 5 to 50:\n",vec)
vec1=vec[1::2]
print("Evenly distributed vector between 5 to 50:\n",vec1)

##18. Write a NumPy program to multiply the values of two given vectors.

a=np.array(list(map(int,input("element of first array:").split())))
b=np.array(list(map(int,input("element of second array:").split())))
print("First array:\n",a)
print("second array:\n",b)
c=a*b
print("Multiply of two array:\n",c)

##19. Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.

arr=np.arange(10,22).reshape(3,4)
print("3x4 matrix filled with 10 to 21:\n",arr)

##20. Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal
#to 1, 2, 3, 4, 5.

dig=np.diag([1,2,3,4,5])
print("5x5 Zero matrix with diagonal value of [1,2,3,4,5]:\n",dig)

##21. Write a NumPy program to compute sum of all elements, sum of each column and sum of each
#row of an given array.

arr=np.arange(10,22).reshape(3,4)
print("Array is:\n",arr)
print("Sum of all element of array:",np.sum(arr))
print("Column sum of the array:",np.sum(arr,axis=1))
print("Sum of each column of the array:\n",np.cumsum(arr,axis=1))
print("Row sum of the array:",np.sum(arr,axis=0))
print("Sum of each row of the array:\n",np.cumsum(arr,axis=0))
