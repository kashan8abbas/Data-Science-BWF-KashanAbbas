import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Creating the Series of Pandas 
obj1 = pd.Series([1,2,-3])
obj2 = pd.Series(np.arange(len(obj1)), index=['a', 'b', 'c'])
print(obj2)

#Array representation of a series
print(obj2.array)

#Index representation of a series
print(obj2.index)

#Selecting single value from the series 
print(obj2["b"])

#Selecting multiple values from the series
print(obj2[["b", "c"]])

#Filtering with the boolean array
print(obj2[obj2 > obj2["b"]])

#Using Numpy Functions on a Series
print(np.exp(obj2))

#isna() notna() are boolean returning functions that checks if the value is missing or not in series
print(pd.isna(obj2))
print(pd.notna(obj2))

#Series automatically aligns by index label  in arithmatic operations.
obj3 = pd.Series(np.arange(len(obj1)), index=['b', 'c', 'd'])
print(obj2+obj3)

#Name attribute of Series object and Index object of Series object
obj3.name = "Marks"
obj3.index.name = "Grade"







#Creating dataframe from dictionary data structure in python
dict_data = {"Name": ["kashan","hasnain","Meesum"], "Age": [21, 22, 23]}
dict_dataframe = pd.DataFrame(dict_data)
dict_dataframe_Update = pd.DataFrame(dict_data, columns= ['Name'])
print(dict_dataframe)
print(dict_dataframe_Update)

# Reading the CSV File using pandas method
dataframe = pd.read_csv('weather_data.csv')


#print the head (first five values of dataframe) of a dataframe
print(dataframe.head())

#print the tail (last five values of dataframe) of a dataframe
print(dataframe.tail())

#print the information about the dataframe
print(dataframe.info())

#print the description of a dataframe 
print(dataframe.describe())

#parts of a dataframe or attributes. 1) Values 2) Columns 3) Index

#print the all values of a dataframe
print(dataframe.values)

#print the columns of dataframe
print(dataframe.columns)

#print the row indexes of a dataframe
print(dataframe.index)

#Sorting of a dataframe

print(dataframe.sort_values("Temperature_C")) # by default it will sort it in ascending order
print(dataframe.sort_values("Temperature_C", ascending= False)) # now ascending is false, it will sort it in descending order

#Sorting with multiple columns
print(dataframe.sort_values(["Temperature_C", "Humidity_pct"])) 
print(dataframe.sort_values(["Temperature_C", "Humidity_pct"], ascending=[True,False])) 


#Subsetting of a Dataframe

#Subsetting a column
print(dataframe["Location"])


#Subsetting multiple columns
print(dataframe[["Temperature_C", "Humidity_pct"]])

#Subsetting with a logical condition returning true or false
print(dataframe["Temperature_C"] > 25)

#Subsetting some rows with logical condition
subset = dataframe[dataframe["Temperature_C"] > 25]
print(subset)

#print the indexed row
print(dataframe.loc[1])
print(dataframe.iloc[1])

#adding a column to a dataframe and assigning a value to that column
dataframe["example"] = np.arange(0, len(dataframe))
print(dataframe)

#indexes in series does not match the indexes in dataframe therefore gthe values will be missing
val1 = pd.Series([-1.2,-1.3,-1.4], index=["a","b","c"])
dataframe["example"] = val1
print(dataframe)

#The length of the dataframe and series become equal now example column will be assigned the values of series
val2 = pd.Series(np.arange(len(dataframe)))
dataframe["example"] = val2
print(dataframe)

#deleting a column
#del dataframe["example"]
#print(dataframe.columns)

#Adding the new column and assigning with the boolean values using boolean calculations 
dataframe["example2"] = dataframe["example"] > 50


#The outer dictionary keys as a columns and inner keys are row indices.
populations =  {'a': {1:{1.1:"z",1.2:"y"},2:{1.3:"x",1.4:"w"}}, 'b': {3:{1.5:"q",1.6:"e"},4:{1.7:"i",1.8:"o"}}}
create = pd.DataFrame(populations)
print(create)

#Index objects are basically the labels of dataframes and Series
obj4 = pd.Series(np.arange(3), index=['a','b','c'])
print(obj4.index[1:])

#They are immutable 
#obj4.index[2] = "v" #you cannot do that 

#Essential Functionality 

#Reindexing of Series
obj5 = pd.Series([1.2,1.3,1.4], index=['b','a','c'])
obj5.reindex(['a','b','c'])
#Method attribute of reindexing
obj6 = pd.Series([2.1,3.1,4.1], index=[0,2,4])
obj7 = obj6.reindex(np.arange(6), method="bfill")
print(obj7)
#Reindexing of Dataframe 
frame = pd.DataFrame(np.zeros(9).reshape((3, 3)), index=["a", "c", "d"], columns=["Ohio", "Texas", "California"])
#reindexing the row atttribute 
frame2 = frame.reindex(index=["a" , "b" , "d"])
#reindexing the column atttribute 
frame3 = frame.reindex(columns=["a" , "b" , "d"])

#Dropping Entries from Axis

#Drop from series
obj8 = pd.Series(np.arange(5.), index=['a', 'b' ,'c', 'd', 'e'])
obj9 = obj8.drop("a")

#Drop from Dataframe
obj10 = pd.DataFrame(np.arange(16).reshape((4,4)), index=['a', 'b' ,'c', 'd'], columns=[1,2,3,4])
obj11 = obj8.drop(index=["a"])
obj12 = obj8.drop(columns=["1"])

#Arithematic and Data Alignment
#1)Arithemaric methods with fill values 2)Operation btw dataframe and Series

#Function Application and Mapping
frame4 = pd.DataFrame(np.random.standard_normal((4,3)),columns=list("bde"),index=[1,2,3,4])
def f1(x):
    return x.max() - x.min()
frame4.apply(f1, axis="columns") #apply wrt columns
frame4.apply(f1) #apply wrt to rows

#function returning the series
def  f2(x):
    return pd.Series([x.min(),x.max()], index=["min","max"])
frame5 = frame4.apply(f2)

dataframe["Location"].value_counts().head().plot(kind='barh')

plt.show()