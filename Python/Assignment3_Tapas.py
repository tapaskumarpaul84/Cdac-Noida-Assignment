# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:24:26 2020

@author: TAPAS KUMAR PAUL
"""

#Q1: Write a Python program to sum all the items in a list.
#Q2: Write a Python program to get the largest number from a list.
#Q3: Write a Python program to get the smallest number from a list.

list1=input("Enter a list of data: ").split(" ")
list2=[]
total=0
for i in list1[0:]:
    list2.append(int(i))
    total=total+int(i)
print("List of number: ",list2)
print("Sum of all data in a list: ",total)
#check the largest number
max=list2[0]
for j in range(1,len(list2)):
    if max<list2[j]:
        max=list2[j]
    
print("Largest number of the list is ",max)

#check the smallest number
min=list2[0]
for j in range(1,len(list2)):
    if min>list2[j]:
        min=list2[j]
    
print("smallest number of the list is ",min)



#Q4: Write a Python program which accepts a sequence of commaseparated
#numbers from user and generate a list and a tuple with those numbers.

string=input("Enter a list of data: ").split(",")
list1=[]
for i in string[0:]:
    list1.append(int(i))
    
print("List of number: ",list1)

tup=tuple(list1)
print("Tuple of number: ",tup)

#Q5: Write a Python program to print out a set containing all the colors
#from a list which are not present in another list

color_list_1=list(input("Enter 1st color list: ").split(" "))
color_list_2=list(input("Enter 1st color list: ").split(" "))
print("First color list is: ",color_list_1)
print("Second color list is: ",color_list_2)
color_list_3=set(set(color_list_1)-set(color_list_2))
print("New set is:",color_list_3)

#Q6: Write a Python program to get a string made of the first 2 and the
#last 2 chars from a given a string.

string=input("Enter a string: ")
if len(string)>4:
    new_string=string[0:2]+string[-2:]
    print("New string: ",new_string)
else:
    print("Wrong input")
    
#Q7: Write a Python program to get a string from a given string where all
#occurrences of its first char have been changed to '$', except the first char itself.

string=input("Enter the string: ")
first_letter=string[0]
letter=first_letter.lower()
new_string=first_letter
for i in string[1:]:
    if i==first_letter or i==letter:
        i='$'
    new_string=new_string+str(i)

print("New string is: ",new_string)

#Q8: Write a Python program to get a single string from two given strings,
#separated by a space and swap the first two characters of each string.

str1,str2=input("Enter two string: ").split(" ")
a=str1[0:2]
b=str2[0:2]
new_str1=b+str1[2:]
new_str2=a+str2[2:]
new_str=new_str1+str(" ")+new_str2
print("New String is: ",new_str)

#Q9: Write a Python program to add 'ing' at the end of a given string
#(length should be at least 3). If the given string is already ends with 'ing' then add 'ly' instead.

word=input("Enter the string: ")
a=word[-3:]
if a=='ing':
    new_word=word+str('ly')
    
else:
    new_word=word+str('ing')
print("New String is: ",new_word)

#Q10: Write a Python program to change a given string to a new string
#where the first and last chars have been exchanged.

word=input("Enter a string: ")
a=word[0]
b=word[1:-1]
c=word[-1]
new_word=c+b+a
print("New string: ",new_word)


#Q11: Write a Python program to get a string made of 4 copies of the last
#two characters of a specified string (length must be at least 2).

str1=input("Enter a string: ")
print("String is: ",str1)
a=str1[-2:]
str2=a*4
print("%s >> %s"%(str1,str2))

#Q12: Write a Python program to add key to a dictionary.

dict1={0:10,1:20}
dict1[2]=30
print("New dictionary is :",dict1)


#Q13: Write a Python program to concatenate following dictionaries to create a new one.

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dict4={**dic1,**dic2,**dic3}

print(dict4)






