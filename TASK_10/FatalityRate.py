import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("full_grouped.csv")
mask = ["China", "India", "Pakistan", "Bangladesh"]
filtered = dataset[dataset["Country/Region"].isin(mask)]

groupeddata = filtered.groupby("Country/Region")

def find_Fatality(group):
    group["Fatality Rate"] = (group["New deaths"]/group["New cases"])*100
    return group

updateddata = groupeddata.apply(find_Fatality)
updateddata = updateddata.reset_index(level="Country/Region", drop=True)
updateddata.set_index("Date", inplace=True)
updateddata = updateddata.dropna()
print(updateddata)

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 8), sharex=True)
# Plot on the first subplot (top-left)
BanTab = updateddata[updateddata["Country/Region"] == "Bangladesh"]
BanTab.index = pd.to_datetime(BanTab.index)
print(BanTab)
ax[0, 0].plot(BanTab.index, BanTab["Fatality Rate"], color='blue')
ax[0, 0].set_title('Fatality Rate of Bangladesh')
ax[0, 0].set_xlabel('Date')
ax[0, 0].set_ylabel('Fatality Rate')
ax[0, 0].grid(True)

PakTab = updateddata[updateddata["Country/Region"] == "Pakistan"]
PakTab.index = pd.to_datetime(PakTab.index)
print(PakTab)
ax[0, 1].plot(PakTab.index, PakTab["Fatality Rate"], color='blue')
ax[0, 1].set_title('Fatality Rate of Pakistan')
ax[0, 1].set_xlabel('Date')
ax[0, 1].set_ylabel('Fatality Rate')
ax[0, 1].grid(True)
IndTab = updateddata[updateddata["Country/Region"] == "India"]
IndTab.index = pd.to_datetime(IndTab.index)
print(IndTab)
ax[1, 0].plot(IndTab.index, IndTab["Fatality Rate"], color='blue')
ax[1, 0].set_title('Fatality Rate of India')
ax[1, 0].set_xlabel('Date')
ax[1, 0].set_ylabel('Fatality Rate')
ax[1, 0].grid(True)
ChiTab = updateddata[updateddata["Country/Region"] == "China"]
ChiTab.index = pd.to_datetime(ChiTab.index)
print(ChiTab)
ax[1, 1].plot(BanTab.index, BanTab["Fatality Rate"], color='blue')
ax[1, 1].set_title('Fatality Rate of Bangladesh')
ax[1, 1].set_xlabel('Date')
ax[1, 1].set_ylabel('Fatality Rate')
ax[1, 1].grid(True)
plt.show()