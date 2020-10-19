# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:15:32 2020

@author: TAPAS KUMAR PAUL
"""

##1:Write a program to prompt for a file name, and then read through the file
##line-by-line.


import os
def file(line):
    return os.path.join(os.getcwd(),line)
print("Your current directory is -",os.getcwd())

os.listdir(os.getcwd())
name=input("Enter the file name with extension : ")
dic=file(name)
print(dic)
try:
    fi2=open(dic,"r")
    print(fi2.readlines())
except:
    print("No such file exists.")
fi2.close()

##Exercise 2:Create a file called new_world.txt.First add a new line to the file:Welcome to
##robotics time.. And then print the content of new_world.txt.

file=input("Enter the file name with extension : ")
file_object = open(file,'a')

file_object.write("Welcome to robotics time.")
file_object.close()
file_object=open(file,"r")
print(file_object.read())
file_object.close()


##Exercise 3: Follow the steps:
#• Create a class, Triangle. Its __init__() method should take self, angle1, angle2,
#and angle3 as arguments. Make sure to set these appropriately in the body of the
#__init__()method.

#Create a variable named number_of_sides and set it equal to 3.
#• Create a method named check_angles. The sum of a triangle's three angles is It
#should return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180,
#and False otherwise.
#• Create a variable named my_triangle and set it equal to a new instance of your
#Triangle class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).
#• Print out my_triangle.number_of_sides and print out my_triangle.check_angles().

class triangle:
    number_of_sides=3
    def __init__(self,angle1,angle2,angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3
    def check_angles(self):
        if(self.angle1+self.angle2+self.angle3==180):
            return True
        else:
            return False

a,b,c=[int(a) for a in input("Enter all three angles:").split(" ")]
my_triangle=triangle(a,b,c)
print("Number of side of triangle:",my_triangle.number_of_sides)
print("Is it a triangle:",my_triangle.check_angles())


##Exercise 4: Define a class called Songs, it will show the lyrics of a song. Its __init__()
#method should have two arguments:self and lyrics.lyricsis a list. Inside your class create
#a method called sing_me_a_song that prints each element of lyricson his own line.

import time
class Song():
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for i in range(len(self.lyrics)):
            for j in self.lyrics[i]:
                print(j,end="")
                time.sleep(0.1)
            print("\n")
happy_bday = Song(["May god bless you",
"Have a sunshine on you","Happy Birthday to you!"])
Song.sing_me_a_song(happy_bday)


##Exercise 5: Define a class called Lunch.Its __init__() method should have two
#arguments:selfanf menu.Where menu is a string. Add a method called menu_price.It will
#involve a ifstatement:
#• if "menu 1" print "Your choice:", menu, "Price 12.00", if "menu 2" print "Your
#choice:", menu, "Price 13.40", else print "Error in menu".
#To check if it works define: Paul=Lunch("menu 1") and call Paul.menu_price().
 

class lunch:
    def __init__(self,menu):
        self.menu=menu
        
    def menu_price(self):
        if(self.menu=="menu 1" or self.menu=="menu1"):
            print("Your choice:"+self.menu+" Price 12.00")
        elif(self.menu=="menu 2" or self.menu=="menu2"):
            print("Your choice:"+self.menu+" Price 13.40")
        else:
            print("Error in menu")
menu=input("Enter your menu(menu 1/menu 2):")
paul=lunch(menu)
paul.menu_price()


##Exercise 6: Define a Point3D class that inherits from object Inside the Point3D class,
#define an __init__() function that accepts self, x, y, and z, and assigns these numbers to
#the member variables self.x,self.y,self.z. Define a __repr__() method that returns "(%d,
#%d, %d)" % (self.x, self.y, self.z). This tells Python to represent this object in the
#following format: (x, y, z). Outside the class definition, create a variable named my_point
#containing a new instance of Point3D with x=1, y=2, and z=3. Finally, print my_point.
 

class Point3D():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __repr__(self):
        return "(%d,%d,%d)"%(self.x,self.y,self.z)

a,b,c=[int(a) for a in input("Enter three value of point:").split(" ")]
my_point=Point3D(a,b,c)
print("The 3D point is:",my_point)      