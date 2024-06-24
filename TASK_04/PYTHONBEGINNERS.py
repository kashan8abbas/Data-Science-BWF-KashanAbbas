from math import *
import os

# Now you can use functions and classes from the os module
print(os.getcwd())  # Prints the current working directory

# WORKING WITH STRINGS

myName = "Kashan Abbas"
print(myName)
print("My Name is: %s" % myName)  
print(f"My Name is: {myName}")   
print("My Name is: " + myName)    
print(myName.lower())             
print(myName.upper())             
print(myName.isupper())           
print(myName.upper().isupper())   
print(len(myName))                
print(myName[0] + ' ' + myName[1] + ' ' + myName[2])
print(f"{myName.index('a')} {myName.index('sh')}")    
print(myName.replace("Kashan", "Syed Kashan"))        

# WORKING WITH NUMBERS

print(2)              
print(2.5)          
print(-2 + 3)    
print(-3.5 + 3)      
print(3 * 4 + 2) 
print(3 * (4 + 2))  
print(10 % 3)     
print(10 / 3)   
print(10 // 3)    
myNumber = -5
print(myNumber)
print(str(myNumber).isupper()) 
print(str(myNumber) + " is my Age") 
print(abs(myNumber))      
print(pow(myNumber, 3))
print(max(2, 4))         
print(min(2, 4))         
print(round(3.3))         
print(ceil(4.2))         
print(floor(4.2))         
print(sqrt(81))

# GETTING USER INPUT

Qualification = input("What is your qualification?")
print("So! you have done " + Qualification )

# BASIC CALCULATOR USING ARITHEMATIC OPERATION (IF ELSE Conditions AND Function Defination)

def BasicCalculation() :
    print("1) ADDITION\n2) SUBTRACTION\n3) MULTIPLICATION\n4) DIVISION\n5) REMINDER\n6) EXPONENT\n")
    operation = input("Select the operation: ")
    if operation in {"1","2","3","4","5","6"} :
        if operation == "1":
             num1 = int(input("Enter the first number: "))
             num2 = int(input("Enter the second number: "))
             result = num1 + num2
             
        elif operation == "2":
             num1 = int(input("Enter the first number: "))
             num2 = int(input("Enter the second number: "))
             result = num1 - num2
             
        elif operation == "3":
             num1 = int(input("Enter the first number: "))
             num2 = int(input("Enter the second number: "))
             result = num1 * num2
             
        elif operation == "4":
             num1 = int(input("Enter the first number: "))
             num2 = int(input("Enter the second number: "))
             if num2 != 0:
                result = num1 / num2
             else:
                return ("Invalid Divider")
        elif operation == "5":
             num1 = int(input("Enter the first number: "))
             num2 = int(input("Enter the second number: "))
             if num2 != 0:
                result = num1 % num2
                
             else:
                return ("Invalid Divider")
        elif operation == "6":
             num1 = int(input("Enter the first number: "))
             num2 = int(input("Enter the second number: "))
             result = pow(num1, num2)
        return result        
    else : 
        return("Invalid Input")
        

print(BasicCalculation())


# WORKING WITH LISTS

Friends = ["John", "Messum"]
print(Friends)
MixData = ["Laila", "Saba", 2]
print(MixData)
print(MixData[-1]) #output: 2                           |\
print(MixData[2]) #output: 2                            | \
print(MixData[1:]) #output: saba  , ... , end of list   |  \
print(MixData[0:2]) #output: Laila , Saba               |   Slicing methods for list and tuple
print(MixData[::2]) #output: skipping 2 indexes         |  /
print(MixData[::-1]) #output: reverse list              | /
print(MixData[1:2:2]) # [Start : Stop : Step]           |/

# Another way of Slicing (Slice object)
#when you want to use slicing dynamically and for repeation of same slice object
lst = [0, 1, 2, 3, 4, 5]
s = slice(0, 6, 2)
sublist = lst[s]
print(sublist)  # Output: [0, 2, 4]

#List Functions
print(len(MixData))
Friends.append("Adil") #if passed a single value then it will be added at last in list, if another list is appended then that whole list be added as a single sublist at the end. unlike extend function
print(Friends)
Friends.insert(1,"Hunain")
print(Friends)
Friends.extend(MixData) #if passed a list in extend then the whole elements in the list will be added individually at the end of main list.
print(Friends)
Friends.remove(2)
print(Friends)
print(Friends.pop())
print(Friends.index("Hunain"))
print(Friends.append("John")) #output: None because it is operation and does not return
print(Friends)
print(Friends.count("John"))
print(Friends.sort()) #output: None because it is operation and does not return
print(Friends)
print(Friends.reverse()) #output: None because it is operation and does not return 
print(Friends)
coleagues = Friends.copy()
print(coleagues)
# Operations for lists as well as tuples
lst3 = Friends + MixData # Concatination
lst4 = Friends * 3 # Repeatation (Friends + Friends + Friends) 
print("Hunain" in lst4) # Membership Testing

print(lst3)
print(lst3)
# WORKING WITH TUPLES

coordinates = (4,5)
print(coordinates[0])
# coordinates[1] = 2 # this is basically not allowed for tuples and it gives error
# you cannot change, modify, update the element inside the tuple unlike lists in python
MyHomeLocations = [(2,4),(3,5)] # this is basically the tuples inside a list of addresses, 
# you can add another location of yours 
#but you cannot change the single coordinate of any location you have in the list because 
#it is in the tuple but if you want to chane the whole tuple then it doable 
#because tuple is basically in a list and that can he modified.

# WORKING WITH 'and' & 'in' & 'not' KEYWORDS

is_male = True
is_tall = True
age = 19

if is_male and is_tall and age in (15,16,17,18,19):
    print("You are a tall teen male ")
elif is_male and not is_tall:
    print("You are a short male")


#WORKING WITH COMMPARISONS (USING IF ELSE)

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num1 and num3 >= num2:
        return num3
    
print(max_num(3,4,5))

#WORKING WITH COMPARISONS (USING TERNARY)
 
def with_ternary(num1,num2,num3):
    return (num1 if num1>=num2 and num1>=num3 else (num2 if num2>=num1 and num2>=num3 else num3))

print(with_ternary(14,0,15))

#WORKING WITH DICTIONARIES

student = {
    "name" : "Kashan",
    "age" : 19,
    "courses" : ["Math", "Science", "English"],
    "is_online" : True
}

print(student.get("name"))
print(student["age"])
print(student.get("course","key Not Finded"))
print(student["courses"][1])

#WORKING WITH WHILE LOOP

i = 1
while i <= 10:
    print(i)
    i += 1
print("done")

#GUESSING GAME

secret_word = "practice"
guess = ""
i=1
AttemptsLow = 0
while guess != secret_word and not AttemptsLow:
    if i <= 5:
        guess = input("Guess the secret word: ")
        i += 1
    else:
        AttemptsLow = True
if not AttemptsLow:     
    print("You Win!")
else:
    print("You Lose!")

#WORKING WITH FOR LOOP
count = 0
for letter in "Kashan":
    print(letter)

for letter in "Kashan":
    if letter == "a":
        count+=1
print(count)

for friendname in Friends:
    print(friendname)

Courses = student.get("courses",[])
for i in range(len(Courses)):
    print(Courses[i])

for i in range(10):
    print(i)

for i in range(2,10):
    print(i)

for i in range(2,10,4):
    print(i)

#EXPONENT FUNCTION USING RECURSION FUNCTION

def Exponent(a,b):
    if b == 1:
        return a
    else:
        return a * Exponent(a,b-1)

print("power")
print(Exponent(3,3))

#EXPONENT FUNCTION USING FOR LOOP

def ExponentForLoop(a,b):
    result = 1
    for i in range(b):
        result *= a
    return result
    
print(ExponentForLoop(2,4))


#WORKING WITH NESTED FOR LOOP

number_matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in number_matrix:
    for col in row:
        print(col)

#BUILDING A TRANSLATOR

def translate(word):
    updated = ""
    for letter in word:
        if letter in "AEIOUaeiou":
            updated += "g"
        else:
            updated += letter
    return updated
print(translate("kashan"))


#EXCEPTIONAL HANDLING

try:
    val = 5/0
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError as valErr:
    print(valErr)
except ZeroDivisionError as ZeroDevErr:
    print(ZeroDevErr)


#FILE READING

#1 way of reading
with open("Kashan.txt","r") as file:
    content = file.read()
    print(content)

#2 way of reading
filename = open("kashan.txt", "r")
print(filename.readable()) # return boolean if file is readable or not
print(filename.readline()) # return firstline of file (it behaves like a cursor position)
print(filename.readline()) # return secondline of file
print(filename.readlines()) # return the all lines of file (it behaves like a cursor position)
filename.close()

#Through For Loop
filename = open("kashan.txt", "r")
for singleline in filename.readlines():
    print(singleline)
filename.close()


#FILE APPENDING (This will add the data at the end of the file  data that is already added)
count = 0
filename = open("kashan.txt", "a")
while count < 10:
    filename.write(f"syedkashanabbas{count}@gmail.com\n")
    count += 1
filename.close()

#FILE WRITING (This will erase the existed data and replace with the newer ones)
count = 0
filename = open("kashan.txt", "w") # We use file writing to create a file 
while count < 10:
    filename.write(f"syedkashanabbas{count}@gmail.com\n")
    count += 1
filename.close()

#OBJECT ORIENTED PROGRAMMING CONCEPTS

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def location(self):
        if self.x > 0 and self.y >= 0:
            print("You are located at North-East")
        elif self.x > 0 and self.y < 0:
            print("You are located at South-East")
        elif self.x < 0 and self.y >= 0:
            print("You are located at North-West")
        elif self.x < 0 and self.y < 0:
            print("You are located at South-West") 

class Question:
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer