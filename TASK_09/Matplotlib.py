import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(15,7)) #figure size x = width, y = height
styles = plt.style.available
print(styles)
#plt.style.use("fivethirtyeight")
# Data : 1) Numerical data 2) Categorical data
# Univariate Analysis , Bivariate analysis , Multivariate analysis
# 2D line plot: Bivariate analysis, Time Series data

# Visualizing a simple 2D line plot graph
Price = [43000, 45000, 57000, 49000, 45000]
year = [2015, 2016, 2017, 2018, 2019]
plt.plot(year, Price)
plt.show()

# Reading csv file and visualizing the data
batsman = pd.read_csv("sharma-kohli.csv")
print(batsman)

#plot attributes
plt.plot(batsman['index'], batsman['RG Sharma'],color="blue",linestyle="dashed",marker='D', label="R Sharma")
plt.plot(batsman['index'], batsman['V Kohli'],linestyle='dotted',marker='D',label='V Kohli')
plt.title("Rohit Sharma VS Virat Kohli Career ")
plt.xlabel("Season")
plt.ylabel("Runs Scored")
plt.legend() #for the identification of lines on graph
plt.show()


# we use xlim and ylim when we want to visualize the minor change in a curve
Price2 = [43000, 45000, 57000, 49000, 45000, 4000000]
year2 = [2015, 2016, 2017, 2018, 2019, 2020]
plt.plot(year2, Price2)
plt.ylim(0,100000) #you use this in case if you have outliers in your data, so the middle variations vanishes
plt.xlim(2017,2019)
plt.grid()
plt.show()


#Scatter Plot : Bivariate Analysis , Numerical vs Numerical ,  Finding   correlation 
df = pd.read_csv("batter.csv")
df = df.head(50)
plt.scatter(df["avg"],df["strike_rate"])
plt.title("Average and Strike Rate Analysis of Top 50 Batsman")
plt.xlabel("Average")
plt.ylabel("Strike Rate")
plt.show()

#importing the csv from seaborn
Tips = sns.load_dataset('tips')
plt.scatter(Tips["total_bill"],Tips["tip"], s=Tips["size"]*20)
plt.show()
#Another way of drawing Scatter Graph you can use Plot Function
#plt.plot(x,y,'o')

#Colored Scattered Plot
iris = pd.read_csv("iris.csv")
iris['Species'] = iris['Species'].replace({'Iris-setosa':0,'Iris-versicolor':1,'Iris-virginica':2})
plt.scatter(iris["SepalLengthCm"],iris["PetalLengthCm"],c=iris['Species']) #cmap is attribute for different themes, alpha attribute for opacity
plt.colorbar()
plt.show()
#Annotation
batters = pd.read_csv("batter.csv")
sample = batters.head(100).sample(25,random_state=5)
plt.scatter(sample["avg"],sample["strike_rate"])
for i in range(sample.shape[0]):
    plt.text(sample["avg"].values[i],sample["strike_rate"].values[i], sample["batter"].values[i]) #you can add fontdict attribute to add details about labels
plt.show()
#Bar Chart: Bivariate Analysis , Numerical vs Categorical , Aggregate Analysis of groups
#Simple Bar Chart
children = [10, 20, 30, 20, 70]
colors = ["red" , "blue" , "green", "yellow", "pink"]
plt.bar(colors, children) #bar function also contains all that attributes like color etc
plt.show()

#drawing lines for specification of entities
#plt.axhline(value at x,color)
#plt.axvline(value at y,color)


#Horizontal Bar Chart
plt.barh(colors, children) #barh function also contains all that attributes like color etc
plt.show()

dataframe = pd.read_csv("batsman_season_record.csv")
print(dataframe.head())

#bar chart of batsman scored runs in 2015
plt.bar(dataframe["batsman"],dataframe["2015"])
plt.show()
 
#Multiple Bar Charts
plt.bar(np.arange(dataframe.shape[0]) - 0.3, dataframe["2015"], width=0.3, label="2015")
plt.bar(np.arange(dataframe.shape[0]), dataframe["2016"], width=0.3, label="2016")
plt.bar(np.arange(dataframe.shape[0]) + 0.3, dataframe["2017"], width=0.3, label="2017")
plt.xticks(np.arange(dataframe.shape[0]),dataframe["batsman"]) #converting numbers into batsman name.
plt.legend()
plt.xticks(rotation="vertical") #making vertical texts on x axis
plt.show()

#Stacked Bar Chart
plt.bar(dataframe["batsman"],dataframe["2017"],label="2017")
plt.bar(dataframe["batsman"],dataframe["2016"],bottom=dataframe["2017"],label="2016")
plt.bar(dataframe["batsman"],dataframe["2015"],bottom=dataframe["2016"] + dataframe["2017"],label="2015")
plt.legend()
plt.show()

#Histogram = Bivariate Analysis , Numerical Column , Frequency Count
vk = pd.read_csv("vk.csv")
plt.hist(vk["batsman_runs"], bins=[0,10,20,30,40,50,60,70,80,90,100,120])
plt.grid()
plt.show()
#Loading the large numpy array
load = np.load("big-array.npy")
plt.hist(load, bins=[10,20,30,40,50,60,70])
plt.show()
#We use logarithmic scale for y axis to handle the large difference between the frequency counts
plt.hist(load, bins=[10,20,30,40,50,60,70], log=True)
plt.show()


#Pie Chart: Univariate/Bivariate Analysis , Categorical vs Numerical , To find contribution on the standard scale
marks = [23,45,100,20,49]
subjects = ["Data Structures","Alogorithmic Techniques","Cloud Computing","Data Analysis","Machine Learning"]
plt.pie(marks,labels=subjects)
plt.show()

#Example from available dataset
matchdata = pd.read_csv("gayle-175.csv")
plt.pie(matchdata["batsman_runs"],labels=matchdata["batsman"], autopct='%0.1f%%') # you can add color attribute in the form of list as well eg: color=[----]
plt.show()
# If you are focusing or showing some data of particular/one or two batsman then you can explode it soehow outside you can add shadow attribute as well the chart will look somehow 3D
plt.pie(matchdata["batsman_runs"],labels=matchdata["batsman"], autopct='%0.1f%%', explode=[0.1,0,0,0,0,0], shadow=True) 
plt.show()
#plt.savefig("pie_chart1") #saving the figure to local device

#Subplots : multiple graphs on single figure
fig, ax = plt.subplots(nrows=2, ncols=1,sharex=True) #declaring the figure and the axis grid for multiple graphs in easy words, the subplots takes the rows and column number so that it can make 2d Array of graphs and store it in ax. if you want to customize any graph you have to access it like you are going to access the numpy array
ax[0].scatter(batters["avg"],batters["strike_rate"], color="red")
ax[0].set_title('Average VS Strike Rate')
ax[0].set_xlabel('Average')
ax[0].set_ylabel('Strike Rate')
ax[1].scatter(batters["avg"],batters["runs"])
ax[1].set_title('Average VS Runs')
ax[1].set_xlabel('Average')
ax[1].set_ylabel('Runs')
plt.show()

#3D Scatter Plot:
fig = plt.figure()
ax = plt.subplot(projection='3d')
ax.scatter3D(batters["runs"],batters["avg"],batters["strike_rate"])
ax.set_title("IPL batters Analysis")
ax.set_xlabel('Runs')
ax.set_ylabel('Average')
ax.set_zlabel('Strike Rate')
plt.show()

#3D Line Plot: The line connecting the points on the scatter3D plot
x = [0,1,5]
y = [0,10,13]
z = [0,13,20]
fig1 = plt.figure()
ax1 = plt.subplot(projection='3d')
ax1.scatter3D(x,y,z, s=[100,100,100]) #s is list of sizes of each marker
ax1.plot3D(x,y,z,color="red")
plt.show()


#3D Surface Plots: helpful for ML 
x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
X,Y = np.meshgrid(x,y)
Z = np.sin(X) + np.cos(Y)
#Z = X**2 + Y**2
fig2 = plt.figure()
ax2 = plt.subplot(projection="3d")
ax2.plot_surface(X,Y,Z) #cmap is coloring attribute
plt.show()


#Contour(colorless) and Contourf(colorfull) Plots: 2D Version of Surface Plots.
fig3 = plt.figure()
ax3 = plt.subplot()
ax3.contourf(X,Y,Z) #cmap is coloring attribute
plt.show()


#heatmap
ballbyball = pd.read_csv("IPL_Ball_by_Ball_2008_2022.csv")
print(ballbyball.head())
#Task: Make a dataframe with over numbers as indexs and ball numbers as columns and find the total number of sixes on each ball of each over.
#1) Make a table with ball number not exceeding 6 and runs on each ball == 6
temp = ballbyball[(ballbyball["ballnumber"].isin([1,2,3,4,5,6])) & (ballbyball["batsman_run"]==6)]
grid = temp.pivot_table(index=temp["overs"],columns=temp["ballnumber"],values=["batsman_run"],aggfunc="count")
print(grid)
fig = plt.figure(figsize=(20,10))
plt.imshow(grid)
plt.yticks(ballbyball["overs"].unique(),list(range(1,21)))
plt.xticks(np.arange(0,6), list(range(1,7)))
plt.colorbar()
plt.show()
