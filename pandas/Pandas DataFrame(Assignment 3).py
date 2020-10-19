# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 10:29:34 2020

@author: TAPAS KUMAR PAUL
"""



import pandas as pd
import numpy as np

##1. Write a Pandas program to get list from DataFrame column headers.


d={'Name':['Yogesh','Debansh','Rishav','Tapas','Nayan'],
   'Age':[26,24,23,23,24],
   'City':['Mumbai','Bhopal','Lucknow','Kolkata','Mumbai']}
data=pd.DataFrame(d)
print("The DataFrame is:\n",data)
li=list(data['City'])
print("List of student's city name:\n",li)



##2. Write a Pandas program to rename columns of a given DataFrame.
#Sample data:
#Original DataFrame
#col1 col2 col3
#0 1 4 7
#1 2 5 8
#2 3 6 9
#New DataFrame after renaming columns:
#Column1 Column2 Column3
#0 1 4 7
#1 2 5 8
#2 3 6 9



data=pd.DataFrame({'col1':[1,2,3],
                   'col2':[4,5,6],
                   'col3':[7,8,9]})
print("Original DataFrame:\n",data)

data1=data.rename(columns={'col1':'Column1','col2':'Column2','col3':'Column3'})
print("New DataFrame after renaming columns:")
print(data1)

print("Rename the index:")
data1=data1.rename(index={0:'x',1:'y',2:'z'})
print(data1)


##3. Write a Pandas program to add one row in an existing DataFrame.


#Use the previous dataframe
print("The Existing DataFrame is:\n",data1)
#add a new row name 'a'
data1.loc['a']=[10,11,12]
print("After adding new row the dataframe is:\n",data1)


#add a new row in data1
data2=data1.append({'Column1':13,'Column2':14,'Column3':15},ignore_index=True)
print("New DataFrame after adding 'b' row:\n",data2)



##4. Write a Pandas program to write a DataFrame to CSV file using tab separator.


print("Existing dataframe is:\n",data1)
print("Dataframe to csv")
data1.to_csv("Data.csv",sep='\t',index=False)
newData=pd.read_csv("Data.csv")
print("New data frame is:\n")
print(newData)



##5. Write a Pandas program to count city wise number of people from a given of data set (city,
#name of the person).


data=pd.DataFrame({'Student_name':['Yogesh','Debansh','Rishav','Tapas','Nayan','Mangal','Rishi'],
                   'City':['Mumbai','Bhopal','Lucknow','Kolkata','Mumbai','Lucknow','Mumbai']},
                    columns=['Student_name','City'])
                    
print("The DataFrame is:\n",data)
group=data.groupby(data['City']).size().reset_index(name='Number of student')
print("city wise number of people:")
print(group)


##6. Write a Pandas program to replace all the NaN values with Zero's in a column of a dataframe.


data={'First score':[100,90,np.nan,95],'Second score':[30,np.nan,56,np.nan],'third score':[np.nan,40,80,98]}
df=pd.DataFrame(data)
print("The original DataFrame is:\n",df)
df1=df.fillna(0)
print("After fill all nan values with zero:")
print(df1)


##7. Write a Pandas program to count the NaN values in one or more columns in DataFrame.


data={'First score':[100,90,np.nan,95],'Second score':[30,np.nan,56,np.nan],'third score':[np.nan,40,80,98]}
df=pd.DataFrame(data)
print("The original DataFrame is:\n",df)
print("Number of NaN value for each column:")
print(df.isna().sum())



##8. Write a Pandas program to drop 2nd and 4th rows from a specified DataFrame.


data={'First score':[100,90,np.nan,95],'Second score':[30,np.nan,56,np.nan],'third score':[np.nan,40,80,98]}
df=pd.DataFrame(data)
print("The original DataFrame is:\n",df)
df1=df.drop([1,3],axis=0)
print("After droped the 2nd and 4th rows from the dataframe:")
print(df1)


##9. Write a Pandas program to combining two series into a DataFrame.


ser1=pd.Series(['Tapas','Yogesh','Rishabh','Debansh'])
ser2=pd.Series(['Kolkata','Mumbai','Lucknow','Bhopal'])
data={'Name':ser1,'city':ser2}
df=pd.DataFrame(data)
print("DataFrame is:")
print(df)


##10. Write a Pandas program to rename a specific column name in a given DataFrame.



data={'First score':[100,90,np.nan,95],'Second score':[30,np.nan,56,np.nan],'Third score':[np.nan,40,80,98]}
df=pd.DataFrame(data)
print("The original DataFrame is:\n",df)
df1=df.rename(columns={'First score':'1st score','Second score':'2nd score','Third score':'3rd score'})
print("Rename the columns name:\n",df1)



##11. Write a Pandas program to get a list of a specified column of a DataFrame.


data={'First score':[100,90,np.nan,95],'Second score':[30,np.nan,56,np.nan],'Third score':[np.nan,40,80,98]}
df=pd.DataFrame(data)
print("The original DataFrame is:\n",df)
lis=list(df['Second score'])
print("List of the Second column is:\n",lis)


##12. Write a Pandas program to get the datatypes of columns of a DataFrame.


d={'Name':['Yogesh','Debansh','Rishav','Tapas','Nayan'],
   'Age':[26,24,23,23,24],
   'City':['Mumbai','Bhopal','Lucknow','Kolkata','Mumbai']}
data=pd.DataFrame(d,columns=['Name','Age','City'])
print("The DataFrame is:\n",data)
print("Data types of each column:\n",data.dtypes)


##13. Write a Pandas program to remove infinite values from a given DataFrame.



data=pd.DataFrame({'col1':[1,2,np.inf,3,4],
                   'col2':[4,np.inf,5,6,3],
                   'col3':[7,8,9,-np.inf,1]})
print("Original DataFrame:\n",data)
data1=data.replace([np.inf,-np.inf],np.nan)
print("Remove infinite value from a dataframe by NaN value:\n",data1)


data2=data.replace([np.inf,-np.inf],0)
print("Remove infinite value from a dataframe by zero value:\n",data2)


##14. Write a Pandas program to insert a given column at a specific column index in a DataFrame.



d={'Name':['Yogesh','Debansh','Rishav','Tapas','Nayan'],
   'City':['Mumbai','Bhopal','Lucknow','Kolkata','Mumbai']}
data=pd.DataFrame(d)
print("Original DataFrame is:\n",data)
new_col=[26,24,23,23,24]
pos=1
data.insert(loc=pos,column='Age',value=new_col)
print("New Data Frame is:\n",data)


##15. Write a Pandas program to get first n records of a DataFrame.


d={'Name':['Yogesh','Debansh','Rishav','Tapas','Nayan'],
   'Age':[26,24,23,23,24],
   'City':['Mumbai','Bhopal','Lucknow','Kolkata','Mumbai']}
data=pd.DataFrame(d,columns=['Name','Age','City'])
print("The DataFrame is:\n",data)

n=int(input("Enter the value of number of rows less than 5:"))
print("Get the first %d value from the dataframe:"%n)
print(data.head(n))



##16. Write a Pandas program to get last n records of a DataFrame.


d={'Name':['Yogesh','Debansh','Rishav','Tapas','Nayan'],
   'Age':[26,24,23,23,24],
   'City':['Mumbai','Bhopal','Lucknow','Kolkata','Mumbai']}
data=pd.DataFrame(d,columns=['Name','Age','City'])
print("The DataFrame is:\n",data)

n=int(input("Enter the value of number of rows less than 5:"))
print("Get the last %d value from the dataframe:"%n)
print(data.tail(n))


##17.Write a Pandas program to remove first n rows of a given DataFrame.


d={'Name':['Yogesh','Debansh','Rishav','Tapas','Nayan'],
   'Age':[26,24,23,23,24],
   'City':['Mumbai','Bhopal','Lucknow','Kolkata','Mumbai']}
data=pd.DataFrame(d,columns=['Name','Age','City'])
print("The DataFrame is:\n",data)
n=int(input("Enter number of first rows to delete less than 5:"))
print("New dataframe is:\n",data.drop(data.index[0:n]))



##18. Write a Pandas program to remove last n rows of a given DataFrame.


d={'Name':['Yogesh','Debansh','Rishav','Tapas','Nayan'],
   'Age':[26,24,23,23,24],
   'City':['Mumbai','Bhopal','Lucknow','Kolkata','Mumbai']}
data=pd.DataFrame(d,columns=['Name','Age','City'])
print("The DataFrame is:\n",data)
n=int(input("Enter number of last rows to delete less than 5:"))
print("New DataFrame is:\n",data.drop(data.index[-n:]))