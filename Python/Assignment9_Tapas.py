# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 16:20:51 2020

@author: TAPAS KUMAR PAUL
"""

##Q1: Write a Python Program To Display Powers of 2 Using Anonymous Function. Take
#number of terms from user

power=lambda x:x**2
n=int(input("Enter the number:"))
print(power(n))


##Q2: Write a Python Program to find numbers divisible by thirteen from a list using
#anonymous function

list1=list(map(int,input("Enter the list of numbers:").split(",")))
list2=list(filter(lambda x:(x%13==0),list1))
print(list2)


#Q3: Write a Python program to find the H.C.F of two input number

def hcf(a,b):
    if(a>b):
        min=b
    else:
        min=a
    while(1):
        if(a%min==0 and b%min==0):
            break
        else:
            min=min-1
    print("H.C.F is:",min)

x,y=[int(x) for x in input("Enter two numbers:").split()]
hcf(x,y)

##Q4: Write a Python Program to find the factors of a number

def factors(x):
    min=x
    count=0
    factors=[]
    while(min>=1):
        if(x%min==0):
            factors.append(min)
            min=min-1
            count=count+1
        else:
            min=min-1
    print("Number of factors:",count)
    print("List of factors:",factors[::-1])
factors(int(input("Enter the number:")))


##Q5: Write a Program to make a simple calculator that can add, subtract, multiply and
#divide using functions

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

a=float(input("Enter the first number:"))
ops=input("Enter the operation(+ or - or * or /):")
b=float(input("Enter the second number:"))

print("Result")
if(ops=="+"):
    print("%0.2f + %0.2f=%0.2f"%(a,b,add(a,b)))
elif(ops=="-"):
    print("%0.2f - %0.2f=%0.2f"%(a,b,sub(a,b)))
elif(ops=="*"):
    print("%0.2f * %0.2f=%0.2f"%(a,b,mul(a,b)))
elif(ops=="/"):
    print("%0.2f / %0.2f=%0.2f"%(a,b,div(a,b)))
    
else:
    print("Invalid operation")
    

##Q6: Write a Python program to display the Fibonacci sequence up to n-th term using
#recursive functions
    
def fibo(n):
    if (n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return (fibo(n-1)+fibo(n-2))
n=int(input("Enter the number of terms:"))
print("Fibonacci series upto %d th number:"%n)
for i in range(n):
    print(fibo(i),end=" ")

##Q7: Write a Python program to find the sum of natural numbers up to n using recursive
#function
    
def sum(n):
    if(n==1):
        return 1
    else:
        return (n+sum(n-1))
num=int(input("Enter the number:"))
print("Sum of natural numbers upto %d is:%d"%(num,sum(num)))


##Q8: Write a Python program to convert decimal number into binary number using
#recursive function

def binary(n):
   if n > 1:
       binary(n//2)
   
   print(n % 2,end =" ")
 

dec = int(input("Enter an integer: "))
print("Binary number is:",end=" ")
binary(dec)

    

    
    


            
            