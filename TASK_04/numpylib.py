import numpy as np

# numpy - Nnumeric Array
# ndArray - n-dimentional array
np1 = np.array([1, 2, 3, 4]) # creating an array of numpy
print(np1)

print(np1.shape) # returns the length of the array of numpy

np2 = np.arange(12) # creating an array of numpy using arange method of numpy
print(np2)

np3 = np.arange(0,10,2) # arange with [start,stop,step]
print(np3)

np4 = np.zeros(10) # creating an zero array of numpy
print(np4)

# creating multidimentional numpy array of zeroes
np5 = np.zeros((2,5))
print(np5) 

# creating 1-D full numpy array
np6 = np.full((10),5) # full((size), value)
print(np6)

# creating multidimentional full numpy array
np7 = np.full((2,5),4)
print(np7)

# converting the normal python list into a numpy array
my_list = [2,4,5]
np8 = np.array(my_list)
print(np8)

# Accessing any element from numpy array is same as of python list

# Slicing Numpy Arrays
np9 = np.array([1,2,3,4,5])

print(np9[1:2]) # excluding 2nd index term

# Slicing with multidimensional numpy arrays
n10 = np.array([[1,2,4],[3,4,6],[5,6,8],[7,8,10]])
print(n10[1,2])
print(n10[1:2])

print(n10[1:3,1:2])

# Extract every second element from each row
print(n10[:2, ::2])

# Integer array indexing
arr = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 3]
print(arr[indices])  # Output: [10 30 40]

# Boolean Masking
arr = np.array([0, 1, 2, 3, 4, 5])
mask = arr > 2
print(arr[mask])  # Output: [3 4 5]
#practice: Slice the Even Number array from the given general array
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
evenMask = arr % 2 == 0
EvenArray = arr[evenMask]
print(EvenArray)
#practice: Slice the Fruits with the letter 'a'
arr1 = np.array(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape'])
mask = np.char.find(arr1,"a")
fruitWithAletter = arr1[mask]
print(fruitWithAletter)


# Functions of NumPy Arrays
arr2 = np.array([2,3,4,5,6,7])
# Square Root Function
sroot = np.sqrt(arr2)
print(sroot)
# Absolute Value Function
absolute = np.abs(arr2)
print(absolute)
# Exponential Value Function
exponential = np.exp(arr2)
print(exponential)
# Aggregate Functions
minimum = np.min(exponential)
print(minimum)
maximum = np.max(exponential)
print(maximum)
# Sign of elements in Numpy array
arr3 = np.array([-2,0,4,25,-6,7])
signArray = np.sign(arr3)
print(signArray) # returns array with entries (1,0,-1) 1 shows +, 0 shows neither, -1 shows negation
# Trignometric Functions
arr4 = np.array([0, 30, 45, 60, 90])
sinArray = np.sin(arr4)
print(sinArray)
cosArray = np.cos(arr4)
print(cosArray)
# Same for tan(arr4),arcsin(arr4),arccos(arr4),arctan(arr4)
# Logarithmic Function
arr5 = np.array([1, 2, 3, 4, 5])
logArray = np.log(arr5)
print(logArray)
# visit Numpy.org website for all universal functions for Numpy



