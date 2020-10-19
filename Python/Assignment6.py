# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 09:12:32 2020

@author: TAPAS KUMAR PAUL
"""

##Q1. write a Python program to check if the input year is a leap year or not.

def leap_year(year):
    if (year%4==0):
        if (year%100==0):
            if(year%400==0):
                print("%d is a leap year"%year)
            else:
                print("%d is not a leap year"%year)
        else:
            print("%d is a leap year"%year)
    else:
        print("%d is not a leap year"%year)

year=int(input("Enter a year:"))
leap_year(year)
            

##Q2. write a Program to display the Fibonacci sequence up to n-th term where n is provided by the user

def fibo(n):
    a=0
    b=1
    print("Fibonacci Series upto %d th term is:"%n)
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
        
x=int(input("Enter the number of terms of the series:"))       
fibo(x)
        

##Q3. write a Program to check if a string is palindrome or not

def palindrome(string):
    if (string[::-1]==string):
        print("Entered string '%s' is a palindrome"%string)
    else:
        print("Entered string '%s' is not a palindrome"%string)
str1=input("Enter a string to check palindrome or not:")
palindrome(str1)


##Q4. write a Program to sort alphabetically the words form a string provided by the
##user. [You can use split() method to split string into a list of words. ]


str1=input("Enter the strings:").split(" ")
li=list(map(lambda x:x,str1))
li.sort()
print("Sorted list is:",li)

##Q5. write a Program to Remove Punctuations from a String provided by the user

punc= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
str1=input("Enter a string:")
no_punc=""
for char in str1:
    if char not in punc:
        no_punc=no_punc+char
print(no_punc)
    


##Q6. Write a Python program to find sequences of lowercase letters joined with a underscore.

import re
str1=input("Enter the string:")
str2=re.findall(r'[a-z]+_[a-z]+',str1)
print(str2)



##Q7. Write a Python program to find the sequences of one upper case letter followed by lower case letters.

str1=input("Enter a string:")
str2=re.findall(r'[A-Z]{1}[a-z]+',str1)
print(str2)

##Q8. Write a Python program that matches a string that has an 'a' followed by
##anything, ending in 'b'.

import re
p=re.compile('.*a.*b$', flags=re.IGNORECASE)
str1=input("Enter your string: ")
result_str=p.findall(str1)
print(result_str)

    
##Q9. Write a Python program that matches a word containing 'z', not at the start or
##end of the word.

import re
p=re.compile(r'\b[a-y]+z+[a-y]+\b')
str1=input("Enter your string: ")
result_str=p.findall(str1)
print("The strings containing z: ",result_str)



##Q10. Write a Python program to match a string that contains only upper and
##lowercase letters, numbers, and underscores.

import re
p=re.compile('\w+', flags=re.IGNORECASE)
str1=input("Enter your string: ")
result_str=p.findall(str1)
print("The strings with alphanumeric letters: ",result_str)



        
##Q11. Write a Python program where a string will start with a specific number.    

import re
str1=input("Enter your string: ")
str2=re.findall(r'\b[0-9]+\w+\b',str1,flags=re.IGNORECASE)
print("The strings starting with number: ",list(str2))



##Q12. Write a Python program to remove leading zeros from an IP address.

import re
str1=input("Enter your IP address: ")
p=re.sub(r'\b0+(\d+)',r'\1',str1)
print("Removing leading zeroes in IP address: ", p)



##Q13. Write a Python program to check for a number at the end of a string.

import re
str1=input("Enter your string: ")
result_str=re.findall(r'\b\w+[0-9]+\b',str1,flags=re.IGNORECASE)
print("The strings ending with number: ",list(result_str))



##Q14. Write a Python program to search the numbers (0-9) of length between 1 to 3
##in a given string.

import re
str1=input("Enter your string: ")
result_str=re.findall('\d{1,3}',str1)
print("The strings with digits of length 1 to 3: ",result_str)





##Q15. Write a Python program to search a literals string in a string and also find the
##location within the original string where the pattern occurs.

import re
pattern = 'string'
text =input("Enter the string:")
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' % \
    (match.re.pattern, match.string, s, e))



##Q16. Write a Python program to find the substrings within a string.

import re
p=re.compile(r' \w+$')
str1=input("Enter your string: ")
result_str=re.findall(p,str1)
print(result_str)



##Q18. Write a Python program to extract year, month and date from an url.

def findMonth(string):
    reg=r"(\d{4,4})-([A-Za-z]+)-(\d{1,2})"
    match=re.match(reg,string)
    if match==None:
        print("Not a valid date:")
        return
    print("Given data is:%s"%(match.group()))
    print("Year:",match.group(1))
    print("Month:",match.group(2))
    print("Date:",match.group(3))

str1=input("Enter the url date:")
findMonth(str1)

##Q19. Write a Python program to find all words starting with 'a' or 'e' in a given
##string.

import re
str1=input("Enter your string: ")
result_str=re.findall(r'[a|e]+\w+',str1)
print("The strings starting with a or e",result_str)




##Q20. Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.

import re
str1=input("Enter your string: ")
p=re.sub(r'\B[a-z]+\B',"",str1)
print(p+".")


