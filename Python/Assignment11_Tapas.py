# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:02:39 2020

@author: TAPAS KUMAR PAUL
"""

##Q.1. Write a program that asks the user how many days are in a particular month, and what day of the
#week the month begins on (0 for Monday, 1 for Tuesday, etc), and then prints a calendar for that month.
#For example, here is the output for a 30-day month that begins on day 4 (Thursday):

#(0-Monday,1-Tuesday,2-Wednesday,3-Thursday,4-Friday,5-Saturday,6-Sunday)
days=int(input("Enter the number of days of the month:"))
start=int(input("Enter starting day:"))
print("Mn\tTu\tWe\tTh\tFr\tSa\tSu")
k=1
for i in range(1):
    for j in range(7):
        if(j<start):
            print("\t",end="")
        else:
            print(k,end="\t")
            k=k+1
        
    break
print()
for i in range(4):
    for j in range(7):
        if(k<=days):
            print(k,end="\t")
            k=k+1
        else:
            break
    print()
    

##Q. 2. Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
#For example, histogram([4, 9, 7]) should print the following:
#****
#*********
#*******

def histogram(li):
    for i in li:
        for j in range(i):
            print("*",end="")
        print()
list1=list(map(int,input("Enter the values of list element:").split(",")))
histogram(list1)


##Q. 3. Write a version of a palindrome recognizer that also accepts phrase palindromes such as 
#"Go hang asalami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", 
#"Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
#"Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and
#spacing are usually ignored
        
import re
def palindrome(text):  
    text1=re.sub(r"\W","",text)
    new=text1[::-1]
    if(new.casefold()==text1.casefold()):
        print("The sentence is palindeome.")
    else:
        print("The sentence is not a palindrome.")
sentence=input("Enter your sentence:")
palindrome(sentence)


##Q. 4. A pangram is a sentence that contains all the letters of the English alphabet at least once, for
#example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a
#sentence to see if it is a pangram or not.

def contain(sen,let):
    common=[]
    for c in sen:
        if c in common:
            pass
        elif(c in let):
            common.append(c)
    a=len(common)
    b=len(let)
    if(a==b):
        print("It is a panagram.")
    else:
        print("It is not a panagram.")

letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
sentence=input("Enter the sentence:")
contain(sentence,letter)


##Q.5. In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter in the
#plain text is replaced by a letter some fixed number of positions down the alphabet. For example, with a
#shift of 3, A would be replaced by D, B would become E, and so on. The method is named after Julius
#Caesar, who used it to communicate with his generals. ROT-13 ("rotate by 13 places") is a widely used
#example of a Caesar cipher where the shift is 13.   


def cryptography(sen):
    text=""
    
    for eachletter in sen:
        
        index=ord(eachletter)
        if(65<=index<=77):
            crypting=chr(index+13)
            text=text+str(crypting)
        elif(78<=index<=90):
            crypting=chr(index-13)
            text=text+str(crypting)
        
        elif(97<=index<=109):
            crypting=chr(index+13)
            text=text+str(crypting)
        elif(110<=index<=122):
            crypting=chr(index-13)
            text=text+str(crypting)
        else:
            text=text+str(eachletter)
    print(text)
sentence=("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!")
cryptography(sentence)



##Q.6. Q. 1. Given a dictionary of students and their favourite colours:
#people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
#1. Find out how many students are in the list
#2. Change Lisa’s favourite colour
#3. Remove 'Jenny' and her favourite colour
#4. Sort and print students and their favourite colours alphabetically by name


people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
name_of_student=people.keys()
print("Number of student:",len(name_of_student))
people['Lisa']="Green"
print(people)
del people['Jenny']
print(people)
print(sorted(people))
for i in sorted (people) :
    print (i,":",people[i],end=", ")
        
#Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's
#language").That is, double every consonant and place an occurrence of "o" in between. For example, translate("this
#is fun") should return the string "tothohisos isos fofunon". 
       
import re
def translate(sen):
    res=''
    reg1=r'[^aeiou\s]'
    for i in range(len(sen)):
        if re.match(reg1,sen[i]):
            res=sen[i]+'o'+sen[i]
        else:
            res=sen[i]
        print(res,end="")
translate('this is fun')      

##Q. 7. Write a program that contains a function that has one parameter, n, representing an integer
#greater than 0. The function should return n! (n factorial). Then write a main function that calls this function
#with the values 1 through 20,     

import math
def factorial(f,l):
    for i in range(f,l):
        print("{} {}".format(i,math.factorial(i)))
def main():
    factorial(1,21)
if __name__=='__main__':
    main()
    
##Q. 8.We can define sum from 1 to x (i.e. 1 + 2 + ... + x) recursively as follows for integer x ≥ 1:
#1, if x = 1 x + sum from 1 to x-1 if x > 1

def sum(x):
    if(x==1):
        return 1
    else:
        return (x+sum(x-1))
num=int(input("Enter the number:"))
print("Sum of natural numbers upto %d is:%d"%(num,sum(num))) 


##Q. 9. Define a function overlapping() that takes two lists and returns True if they have at least one
#member in common, False otherwise.


def overlapping(list1,list2):
    s1= set(list1)
    s2= set(list2)
    if len(set.intersection(s1,s2))!=0:
        print("True")
    else:
        print("False")
list1=list(input("Enter list1 value:").split(","))
list2=list(input("Enter list2 value:").split(","))
overlapping(list1,list2)

#Q.10.Write a function find_longest_word() that takes a list of words and returns the length of the longest
#one. 

def find_longest_word(list1):

    l=sorted(list1,key=len,reverse=True)
    print("%s is the longest word with length %d"%(l[0],len(l[0])))
list1=list(map(str,input("Enter words in the list: ").split()))
find_longest_word(list1)


##Write a function filter_long_words() that takes a list of words and an integer n and returns the list
#of words that are longer than n


def filter_long_word(list1,n):
    list2=[]
    for i in list1:
        if (len(i)>n):
            list2.append(i)
        else:
            pass
    print(list2)
n=int(input("Enter the value of n:"))
list1=list(map(str,input("Enter words in the list: ").split()))
filter_long_word(list1,n)
            


#Q. 11.Define a simple "spelling correction" function correct() that takes a string and sees to it that
#1)two or more occurrences of the space character is compressed into one, and
#2)inserts an extra space after a period if the period is directly followed by a letter.
#e.g. correct("This is very funny and cool.Indeed!") should return "This is very funny and cool.
#Indeed!"


def correct(str1):
    stin=re.sub(r'[\s]+'," ",str1)
    stin=re.sub(r'(\w)([\.,!]+)(\w)',r'\1\2 \3',str1)
    print(stin)
str1="This is very funny and cool. Indeed!"
correct(str1)

##Q. 12.In English, present participle is formed by adding suffix -ing to infinite form: go -> going. A simple
#set of heuristic rules can be given as follows:
#● If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
#● If the verb ends in ie, change ie to y and add ing
#● For words consisting of consonant-vowel-consonant, double the final letter before adding ing
#● By default just add ing
#Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form
#returns its present participle form. Test your function with words such as lie, see, move and hug.
#However, you must not expect such simple rules to work for all cases.


expt=['be','see','is','flee','knee',]
def make_ing_form(str1):
    reg=r'([bcdfghjklmnpqrstvwxyz][aeiou][bcdfghjklmnpqrstvwxyz])\b'
    if str1 in expt:
        str1=str1
    elif str1[-2:]=='ie':
        str1=re.sub(r'(\w)(ie)\b',r'\1ying',str1)
    elif str1[-1]=='e':
        str1=re.sub(r'(\w)(e)\b',r'\1ing',str1)
    elif(re.match(reg,str1)):
        str1=re.sub(reg,r'\1\2\3\3ing',str1)
    else:
        str1=re.sub(r'\b(\w+)\b',r'\1ing',str1)
    print(str1)
str1=input("Enter string : ")
make_ing_form(str1)