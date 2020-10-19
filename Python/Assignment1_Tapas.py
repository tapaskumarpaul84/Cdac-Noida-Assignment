# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 09:35:05 2020

@author: TAPAS KUMAR PAUL
"""

# QS1) Write a Python program which accept the radius of a circle from the user and compute the area.
from math import pi
r=float(input("Enter the radius of the circle: "))
area=pi*r*r
print("Area of the circle is %0.2f" %area)

#QS2) Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a program to convert this temperature into Centigrade degrees.

temp=input("Enter the temperature:")
temp_type=temp[-1]   #to get the type of temperature last letter of the string
t=float(temp[:-1])   # temperature without last letter
if temp_type=='c' or temp_type=='C':
    print("Entered temperature is in Celcius")
    f=((9*t)/5)+32   #conversion of celcius to fahrenheit
    print("Converted temperature is %0.2f F"%f)
elif temp_type=='f' or temp_type=='F':
    print("Entered temperature is in Fahrenheit")
    c=((t-32)/9)*5  #conversion of fahrenheit to celcius
    print("Converted temperature is %0.2f C"%c)
else:
    print("Entered temperature is wrong")
    
    
#QS3) Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of basic
#salary, and house rent allowance is 20% of basic salary. Write a program to calculate his gross
#salary.

sal=float(input("Enter the basic salary of ramesh:"))
da=sal*0.4
hra= sal*0.2
total=sal+da+hra
print("gross salary of ramesh is %0.2f",total)

#QS4) Write a Python program which accept the user's first and last name and print them in reverse
#order with a space between them.

first_name=input("Enter First name:")
last_name=input("Enter last name:")
#reverse the name position
print("reversed name\n")
print(last_name, first_name)
#reverse the each name and order
n1=first_name[::-1]
n2=last_name[::-1]
print("reversed name and order\n")
print(n2, n1)

#QS5) Write a Python program to get the the volume of a sphere with radius 6.

from math import pi
r=float(input("Enter the radius of the sphere: "))
vol=(4/3*pi)*r**3
print("Volume of the sphere is %0.2f"%vol)

#QS6) If a five-digit number is input through the keyboard, write a program to calculate the sum of
#its digits.

num=int(input("Enter a 5 digit number:"))
sum=0
while num>0:
    rem=num%10  #every remender is the digit of number
    num=num//10 #qutient  is the new number for every iteration
    sum=sum+rem
print("sum of digit is: %d"%sum)

#QS7) Write a Python program to accept a filename from the user and print the extension of that.

file_name=input("Enter the file name ")

F=list(file_name.split("."))
print("Extension is %s"%F[-1])

#QS8) Write a Python program to display the first and last colors from the following list.


color_list=list(input("Enter the color list: ").split(" "))
print("Color list is:",color_list)
print("First color is",color_list[0])
print("Last color is",color_list[-1])

#QS9) Write a Python program to calculate number of days between two dates.

from datetime import datetime
#First date
d1=input("Enter the first date(yyyy-mm-dd):").split("-")
date1=[]
for i in d1[0:]:
    date1.append(int(i))
strt_date=datetime(date1[0],date1[1],date1[2])
print("First date:",strt_date)

#last date
d2=input("Enter the last date(yyyy-mm-dd):").split("-")
date2=[]
for j in d2[0:]:
    date2.append(int(j))
end_date=datetime(date2[0],date2[1],date2[2])
print("Last date:",end_date)

#gap calculation
if strt_date>end_date:
    gap=(strt_date-end_date).days
else:
    gap=(end_date-strt_date).days

print("Gap of entered days: ",gap)

#QS10) Write a Python program to get a new string from a given string where "Is" has been added
#to the front. If the given string already begins with "Is" then return the string unchanged.

str1=input("Enter a string:")
if len(str1)>=2:
    if (str1[0:2]=='Is' or str1[0:2]=='is' or str1[0:2]=='IS'):
        print(str1)
    else:
        print("Is %s"%str1)
else:
    print("Wrong input, length should be greater than 2")
    


#QS11) Write a Python program to test whether a passed letter is a vowel or not.
    
vowel=['A','E','I','O','U','a','e','i','o','u']
letter=input("Enter the letter: ")
if letter in vowel:
    print("The letter is vowel")
else:
    print("The letter is not vowel")