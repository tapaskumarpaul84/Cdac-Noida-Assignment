# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:03:52 2020

@author: TAPAS KUMAR PAUL
"""

#Q1: Write a Python Program to make a simple calculator that can add, subtract, multiply and divide

num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
choice=input("Enter the operation +,-,*,/: ")
if choice=='+':
    print("%0.1f + %0.1f= %0.1f"%(num1,num2,num1+num2))
elif choice=='-':
    print("%0.1f - %0.1f= %0.1f"%(num1,num2,num1-num2))
elif choice=='*':
    print("%0.1f * %0.1f= %0.1f"%(num1,num2,num1*num2))
elif choice=='/':
    print("%0.1f / %0.1f= %0.1f"%(num1,num2,num1/num2))
else:
    print("wrong operation")
    
#Q2: Write a Python Program to calculate the square root
    
import math
num=float(input("Enter the number: "))
sqrt_of_num=math.sqrt(num)
print("Squre root of a number=%0.2f"%sqrt_of_num)

# Q3: Write a Python Program to Solve the quadratic equation ax**2 + bx + c = 0

import cmath
a=float(input("Enter value of a: "))
b=float(input("Enter value of b: "))
c=float(input("Enter value of c: "))
#discriminate solve
if a==0:
    print("value of a should be greater than zero")
else:
    d=(b**2)-(4*a*c)
    d1=cmath.sqrt(d)
    #find the solutions
    sol1=(-b+d1)/(2*a)
    sol2=(-b-d1)/(2*a)
    Sol1=round(sol1.real,2)+round(sol1.imag,2)*1j
    Sol2=round(sol2.real,2)+round(sol2.imag,2)*1j
    print("solutions are",Sol1 , Sol2)

#Q4: Write a Python Program to find the area of triangle

a=float(input("Enter the base of triangle:"))
b=float(input("Enter the height of triangle:"))
c=float(input("Enter the hypotenuse of triangle:"))
#checking triangle or not
if (a+b)>c:
    print("It is a triangle")
    area=0.5*a*c
    print("Area of the triangle is: %0.2f"%area)
else:
    print("It is not a triangle")
    
#Q5: Write a Python program to convert decimal number into binary, octal and hexadecimal number system

dec=int(input("Enter the decimal number:"))
choose=input("choose the conversion name: (2-Binary/8-Octal/16-Hexa-decimal): ")
x=dec
a=[]
str1=""
#from decimal to binary
if choose=='Binary' or choose=='2':
    while dec>0:
        rem=dec%2
        dec=dec//2
        a.append(rem)
    for i in a[::-1]:
        str1=str1+str(i)
    print("Binary number of %d is %s"%(x,str1))
    
# from decimal to octal
    
elif choose=='Octal' or choose=='8':
    
     while dec>0:
        rem=dec%8
        dec=dec//8
        a.append(rem)
     for i in a[::-1]:
        str1=str1+str(i)
     print("Octal number of %d is %s"%(x,str1))
     
# from decimal to Hexa-decimal
     
elif choose=='Hexa-decimal' or choose=='16':
    
     while dec>0:
        rem=dec%16
        dec=dec//16
        if rem<10:
            rem=rem
        elif rem==10:
            rem='A'
        elif rem==11:
            rem='B'
        elif rem==12:
            rem='C'
        elif rem==13:
            rem='D'
        elif rem==14:
            rem='E'
        else:
            rem='F'
        a.append(rem)
     for i in a[::-1]:
        str1=str1+str(i)
     print("Hexa-decimal number of %d is %s"%(x,str1))
    
    
#Q6: Write a python Program to convert kilometers into miles
     
dis=input("Enter the distance: ")
dis_type=dis[-2:]    #last two character as unit of distance

dist=float(dis[:-2]) #take distance from dis variable except last 2 character(unit)
if dis_type=='km':
    print("Entered distance is in kilometer")
    mile=round(dist/1.609,2)  #convert from km to mile
    print("The distance in mile: %0.2f mile"%mile)

elif dis_type=='ml':
    print("Entered distance is in mile")
    km=round(dist*1.609,2) #convert mile to km
    print("The distance in kilometer: %0.2f km"%km)
    
#Q7: Write a Python program to check whether a specified value is contained in a group of values.

data=input("Enter the group: ").split()
group=[]  # blank list
for i in data[0:]:   #convert the list of string to list of integer
    group.append(int(i))
print("Data group is:",group)
val=int(input("Enter the specified value: "))
print(val in group)

#Q8: Write a Python program to concatenate all elements in a list into a string and return it.

list_data=list(input("Enter the list of data: ").split())
print("List of data is :",list_data)
str1=""
for i in list_data[0:]:
    str1=str1+str(i)

print("Concatinated string is: ",str1)

#Q9: Write a Python program to get the least common multiple (LCM) of two positive integers.

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if a>b:
    max=a
    min=b
else:
    max=b
    min=a

while(1):
    if (max%a==0 and max%b==0):
        print("LCM of two number is: ",max)
        break
    max=max+1

# GCD of two numbers
while(1):
    if(a%min==0 and b%min==0):
        print("GCM of given numbers is: ",min)
        break
    min=min-1
    
#Q10: Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

import math
x1=float(input("Enter the value of x1: "))
y1=float(input("Enter the value of y1: "))
print("The first point is:",(x1,y1))  #first point

x2=float(input("Enter the value of x2: "))
y2=float(input("Enter the value of y2: "))
print("The second point is:",(x2,y2))  #second point

distance=round(math.sqrt((x1-x2)**2 + (y1-y2)**2),2)
print("Distance of the given points is: ",distance)





