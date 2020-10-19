# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:16:44 2020

@author: TAPAS KUMAR PAUL
"""

import pandas as pd
import numpy as np


##1. Write a Pandas program to create and display a DataFrame from a specified
#dictionary data which has the index labels.


exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
                      'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
            'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
            'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
data=pd.DataFrame(exam_data,index=labels)
print("Given Data Frame is:\n",data)


##2. Write a Pandas program to display a summary of the basic information
#about a specified DataFrame and its data.

print("Summary of the basic information of the data frame:")
print(data.info())


##3. Write a Pandas program to get the first 3 rows of a given DataFrame.


print("the first 3 rows of a given DataFrame:")
print(data.head(3))


##4. Write a Pandas program to select the 'name' and 'score' columns from the DataFrame given in Q1.


print("Print the 'name' and 'Score' columns from dataframe:")
print(data[["name","score"]])


##5. Write a Pandas program to select the specified columns and rows from a given data frame.

rows=['b','d','g','i']
columns=['name','attempts']
data1=data.loc[rows,columns]
print("Specified rows and columns")
print(data1)


##6. Write a Pandas program to count the number of rows and columns of a DataFrame.

rows,columns=data.shape
print("Number of rows of the dataframe:",rows)
print("Number of columns of the dataframe:",columns)
print("rows=",len(data.axes[0]))
print("columns=",len(data.axes[1]))


##7. Write a Pandas program to select the rows where the score is missing, i.e. is NaN.

print(" the rows where the score is missing:")
print(data[data['score'].isnull()])


##8. Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).

print("the rows the score is between 15 and 20")
print(data[data['score'].between(15,20)])


##9. Write a Pandas program to select the rows where number of attempts in the examination is less
#than 2 and score greater than 15.


print("the rows where number of attempts in the examination is less \
than 2 and score greater than 15")
print(data[(data['attempts']<2) & (data['score']>15)])

##10. Write a Pandas program to change the score in row 'd' to 11.5.

data.loc['d','score']=11.5
print("The modified dataframe is:\n",data)


##11. Write a Pandas program to calculate the sum of the examination attempts by the students.

print("Sum of the examination attempts:",end=" ")
print(data.attempts.sum())

##12. Write a Pandas program to calculate the mean score for the students in DataFrame.

print("Mean of score for the students:",end=" ")
print(round(data.score.mean(),2))


##13. Write a Pandas program to append a new row 'k' to DataFrame with given values for each
#column. Now delete the new row and return the original data frame.


data.loc['k']=[2,'Jhones','yes',18]
print("Add a new row to the DataFrame:")
print(data)
print("Delete the new row and return the original:")
data=data.drop('k',axis=0)
print(data)


##14. Write a Pandas program to sort the data frame first by 'name' in descending order, then by
#'score' in ascending order.


print("Data frame after sorting by name in descending order ")
print(data.sort_values(['name'],ascending=False))
print("Data frame after sorting by score in ascending order ")
print(data.sort_values(['score'],ascending=True))


##15. Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with
#True and False.


data['qualify']=data['qualify'].map({'yes':True,'no':False})
print("Replacing the 'qualify' column:")
print("New dataframe is:\n",data)


##16. Write a Pandas program to change the name 'James' to 'Suresh' in name column of the data
#frame.

data['name']=data['name'].replace('James','Suresh')
print("After replacing the name 'James' to 'Suresh', the dataframe is:")
print(data)


##17. Write a Pandas program to delete the 'attempts' column from the DataFrame.

data1=data.drop(['attempts'],axis=1)
print("After deleted the 'attempts' column")
print(data1)

##18. Write a Pandas program to insert a new column in existing DataFrame.

data['sub']=['math','phys','hist','math','chem','phys','chem','geog','math','phys']
print("Insert new column in existing dataframe:")
print(data)


##19. Write a Pandas program to iterate over rows in a DataFrame.

print(data)
print("Rows Iteration")
for i,j in data.iterrows():
    print(i,j)
    print()


##20. Write a Pandas program to get list from DataFrame column headers.
    
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
                      'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
            'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
            'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
data=pd.DataFrame(exam_data,index=labels)
print("Given Data Frame is:\n",data)
print("List of column headers:")
lis=list(data.columns.values)
print(lis)

