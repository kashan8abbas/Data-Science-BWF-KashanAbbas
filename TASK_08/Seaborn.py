import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#1) Relational plots : to see the statistical relation btw 2 or more variables, bivariate analysis
#plots: Scatter plot, lineplot
#Scatter Plot -> axis level function
tips = sns.load_dataset('tips')
sns.scatterplot(data=tips, x="total_bill", y="tip",hue="sex",style="time", size="size")
plt.show()
#Relplot -> figure level function -> square shaped
sns.relplot(data=tips, x="total_bill", y="tip", kind="scatter",hue="sex",style="time",size="size")
plt.show()

#Line Plot
#Task: lineplot of india's life expectancy varying with time till date.
gap = px.data.gapminder()
temp = gap[gap["country"] == "India"]
#axis level function
sns.lineplot(data=temp, x="year", y="lifeExp")
plt.show()
#figure level function 
sns.relplot(data=temp, x="year", y="lifeExp", kind="line")
plt.show()
#task: three lineplots on single axis (india, pakistan, china)
temp2 = gap[gap["country"].isin(["India","Brazil","Germany"])]
sns.relplot(data=temp2, x="year", y="lifeExp", kind="line", hue="country", style="continent",size="continent")
plt.show()


#Facet Plot: Multiple plots in context to differentiate the different categories of a column
# Facet Plot -> figure level function -> work with relplot function
# it will not work with the scatterplot and lineplot
sns.relplot(data=tips, x="total_bill", y="tip", kind="scatter", col="sex", row="smoker")
plt.show()
#Column Wrap 
sns.relplot(data=gap, x="lifeExp", y="gdpPercap", kind="scatter", col="year", col_wrap=4)
plt.show()

#2) Distribution plots : univariate analysis, find out the distribution, range of observation, central tendency, data outliers
#plots: histplot, kdeplot (kernal distribution estimation), rugplot
#axis level functions -> histplot, kdeplot, rugplot
#figure level function -> displot 

#Histogram Plot
sns.histplot(data=tips, x="total_bill") # axis level function
plt.show()
sns.displot(data=tips, x="total_bill", kind="hist") # figure level function
plt.show()
#Bins Attribute
sns.displot(data=tips, x="total_bill", kind="hist",bins=20) # figure level function
plt.show()

#Its also possible to visualize the distribution of a categorical variable using the logic of a histogram
#discrete bins are automatically set for categorical variables -> it is basically a countplot but somehow works here
sns.displot(data=tips, x="day", kind="hist") # x will be categorical column eg: day
plt.show()
#Hue parameter and element attribute
sns.displot(data=tips, x="tip", kind="hist", hue="sex", element="step") 
plt.show()
#Faceting -> not work on histplot because it is not figure level but an axis level function
sns.displot(data=tips, x="tip", kind="hist", col="sex", element="step") 
plt.show()
#Bivariate histogram -> a bivariate histogram bins the data within rectangles that tile the plot and then shows the count of observations within each rectangle with the fill color
sns.histplot(data=tips, x="total_bill", y="tip")
plt.show()
sns.displot(data=tips, x="total_bill", y="tip", kind="hist")
plt.show()

#KDE Plot -> kernal Distribution Estimation Plot: It works like a histplot but tells density instead of count and it is continuous graph and works on the probability to estimate the density of value which is not in x axis 
sns.kdeplot(data=tips, x="total_bill") # axis level function
plt.show()
sns.displot(data=tips, x="total_bill", kind="kde") # figure level function
plt.show()
#Hue parameter and fill attribute
sns.displot(data=tips, x="tip", kind="kde", hue="sex", fill=True) 
plt.show()
#Faceting -> not work on kdeplot because it is not figure level but an axis level function
sns.displot(data=tips, x="tip", kind="kde", col="sex") 
plt.show()
#Bivariate KDE Plot -> bivariate KDE plot smoothes the (x,y) observations with a 2D Guassian 
sns.kdeplot(data=tips, x="total_bill", y="tip")
plt.show()
sns.displot(data=tips, x="total_bill", y="tip", kind="kde")
plt.show()

#Rugplot: Plot Marginal distributions by drawing ticks along the x and y axes.
# This function is intended to conplement other plots by showing the location of individual observations in an unobstrusive way.
sns.kdeplot(data=tips, x="tip") 
sns.rugplot(data=tips, x="tip") 
plt.show()


#3) Matrix plots : bivariate analysis, grid form, Color Encoded
#plots: Heatmap, clustermap 
# No figure level function in this.

#Heatmap : Plot a rectengular data as a color-encoded matrix, it is an axis level function
data = gap.pivot(index="country", columns="year", values="lifeExp")
#Annotation, linewidth, color theme
sns.heatmap(data, annot=True, linewidths=0.5, cmap="summer")
plt.show()
#TASK: plot a heatmap of europian countries with life expectations values
data1 = gap[gap["continent"]=="Europe"].pivot(index="country", columns="year", values="lifeExp")
plt.figure(figsize=(15,15))
sns.heatmap(data, annot=True, linewidths=0.5, cmap="viridis")
plt.show()

#Clustermap : Plot a matrix dataset as a hierarchically-clustered heatmap works on ML algo: Agglomerative Hierarchical Clustering
iris = px.data.iris()
sns.clustermap(iris.iloc[:,[0,1,2,3]])
plt.show()


#4) Categorical Plots -> A) Categorical Scatter Plots B) Categorical Distribution Plots 3) Categorical Estimation Plots
#Figure Level Function -> Catplot
#Axis Level Functions -> Given Below
#A) Categorical Scatter Plots -> i) Stripplot ii) Swarmplot
#B) Categorical Distribution Plots -> i) Boxplot ii) Violinplot
#C) Categorical Estimation Plots -> i) Barplot ii) Pointplot iii) Countplot

#A) Categorical Scatter Plots -> Bivariate Analysis
#i) Stripplot -> Numerical Column VS Categorical Column
sns.stripplot(data=tips, x="day", y="total_bill") #Seaborn internally add some noise to distribute the single dots.
plt.show()
sns.catplot(data=tips, x="day", y="total_bill", kind="strip") 
plt.show()
#jitter attribute, Hue attribute -> arranges value to single line you can make jitter false to arrange and give values to spread btw dots, Hue differentiate the cols with colors
sns.catplot(data=tips, x="day", y="total_bill", kind="strip", jitter=0.2, hue="sex") 
plt.show()

#ii) Swarmplot -> Numerical Column VS Categorical Column, It is similar to stripplot but it has internal algorithm running and gives better distributions
sns.swarmplot(data=tips, x="day", y="total_bill") #Seaborn internally add some noise to distribute the single dots.
plt.show()
sns.catplot(data=tips, x="day", y="total_bill", kind="swarm") 
plt.show()
#Hue attribute -> Hue differentiate the cols with colors
sns.catplot(data=tips, x="day", y="total_bill", kind="swarm", hue="sex") 
plt.show()

#B) Categorical Distribution Plots -> Univariate Analysis
#i) Boxplot -> A boxplot is a standardized way of displaying the distribution of data based on a five number summary
# (minimum, first quartile(25%), second quartile(median), third quartile(75%), maximum). it can tell about your outliers and what thier values are.
# Boxplots can also tell you if your data is symmetrical, how tightly your data is grouped and if and how your data is skewed.

#For Categorical Column on x axis
sns.boxplot(data=tips, x="sex", y="total_bill")
plt.show()
sns.catplot(data=tips, x="sex", y="total_bill", kind="box")
plt.show()
#Hue parameter
sns.catplot(data=tips, x="sex", y="total_bill", kind="box", hue="day")
plt.show()
#For just single information in Y axis
sns.boxplot(data=tips,y="total_bill")
plt.show()

#ii) Violinplot -> Boxplot + KDEplot
#For Categorical Column on x axis
sns.violinplot(data=tips, x="sex", y="total_bill")
plt.show()
sns.catplot(data=tips, x="sex", y="total_bill", kind="violin")
plt.show()
#Hue parameter
sns.catplot(data=tips, x="sex", y="total_bill", kind="violin", hue="day")
plt.show()
#Hue parameter + split parameter
sns.catplot(data=tips, x="sex", y="total_bill", kind="violin", hue="day", split=True)
plt.show()
#For just single information in Y axis
sns.violinplot(data=tips,y="total_bill")
plt.show()


#C) Categorical Estimate Plots -> Bivariate Analysis, for measuring the aggregate value of a data
#i) Barplot ii) Pointplot iii) Countplot

#i) Barplot -> Categorical Column VS Numerical Column
sns.barplot(data=tips, x="sex", y="total_bill", hue="smoker") #categorizes the bar with smoker and non smoker, by default it calculates the average.
plt.show() #the black bar (error bar) on the graph shows the confidence interval
sns.barplot(data=tips, x="sex", y="total_bill", estimator=np.std) #by adding estimator parameter you can give the aggregate function you want.
plt.show()
sns.catplot(kind="bar", data=tips, x="sex", y="total_bill", hue="smoker") #categorizes the bar with smoker and non smoker, by default it calculates the average.
plt.show()

#ii) Pointplot -> Categorical Column VS Numerical Column, but it plots the points and draw the line of difference
sns.pointplot(data=tips, x="sex", y="total_bill", hue="smoker") #categorizes the bar with smoker and non smoker, by default it calculates the average and connects the points.
plt.show() 
sns.pointplot(data=tips, x="sex", y="total_bill", estimator=np.std) #by adding estimator parameter you can give the aggregate function you want.
plt.show()
sns.catplot(kind="point", data=tips, x="sex", y="total_bill", hue="smoker") #categorizes the bar with smoker and non smoker, by default it calculates the average and connects the points.
plt.show()

#iii) Countplot -> the special type of barplot that takes  a categorical column on x axis, then count the observations on that not including other statistics functions than count.
sns.countplot(data=tips, x="sex", hue="day") # you can add hue parameter to categorize the bars.
plt.show()
sns.catplot(kind="count", data=tips, x="sex", hue="day") # you can add hue parameter to categorize the bars.
plt.show() # there is a feceting option here as well, you just have to add col and give the value.


#5) Regression Plots -> Just like the Relational Scatter Plot but it creates the regression line according to the given points on the graph and plot the pridiction error aswell.
#) i) regplot ii) residplot -> axis level function
#  lmplot -> figure level function
# Regplot -> creates the regression line on scatter plot
sns.regplot(data=tips, x="total_bill", y="tip")
plt.show()
sns.lmplot(data=tips, x="total_bill", y="tip", hue="sex") #This is the figure level function.
plt.show()
#residplot -> relates the scatter points on -2,-1,0,1,2 scale to measure the error in predictions
sns.residplot(data=tips, x="total_bill", y="tip")
plt.show()


#MultiPlots 
#1) facetGrid
g = sns.FacetGrid(data=tips, col="day", hue="smoker")
g.map(sns.violinplot, "sex", "total_bill")
plt.show()
g.add_legend()
#2) Plotting Pairwise Relationship (PairGrid Vs Pairplot)
#3) Plotting JointGrid and JontPlot