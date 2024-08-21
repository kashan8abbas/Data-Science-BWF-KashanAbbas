import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("full_grouped.csv")
mask = ["China", "India", "Pakistan", "Bangladesh"]
filtered = dataset[dataset["Country/Region"].isin(mask)]

groupeddata = filtered.groupby("Country/Region")

def find_Rates(group):
    group["Infection Rate"] = group["New cases"].rolling(window=3).mean()
    group["Death Rate"] = group["New deaths"].rolling(window=3).mean()
    return group


updateddata = groupeddata.apply(find_Rates)
updateddata = updateddata.reset_index(level="Country/Region", drop=True)
updateddata.set_index("Date", inplace=True)
print(updateddata)

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 8), sharex=True)
# Plot on the first subplot (top-left)
BanTab = updateddata[updateddata["Country/Region"] == "Bangladesh"]
BanTab.index = pd.to_datetime(BanTab.index)
infectionpeak = BanTab["Infection Rate"].idxmax()
deathpeak = BanTab["Death Rate"].idxmax()
lag = np.abs(deathpeak - infectionpeak)
print(BanTab)
ax[0, 0].plot(BanTab.index, BanTab["Infection Rate"], color='blue', label='Infection Rate')
ax[0, 0].plot(BanTab.index, BanTab["Death Rate"], color='red', label='Death Rate')
ax[0, 0].set_title('Rates of Bangladesh')
ax[0, 0].set_xlabel('Date')
ax[0, 0].set_ylabel('Rate')
ax[0, 0].grid(True)
ax[0, 0].legend()
PakTab = updateddata[updateddata["Country/Region"] == "Pakistan"]
PakTab.index = pd.to_datetime(PakTab.index)
infectionpeak1 = PakTab["Infection Rate"].idxmax()
deathpeak1 = PakTab["Death Rate"].idxmax()
lag1 = np.abs(deathpeak1 - infectionpeak1)
print(PakTab)
ax[0, 1].plot(PakTab.index, PakTab["Infection Rate"], color='blue', label='Infection Rate')
ax[0, 1].plot(PakTab.index, PakTab["Death Rate"], color='red', label='Death Rate')
ax[0, 1].set_title('Rates of Pakistan')
ax[0, 1].set_xlabel('Date')
ax[0, 1].set_ylabel('Rate')
ax[0, 1].grid(True)
ax[0, 1].legend()
IndTab = updateddata[updateddata["Country/Region"] == "India"]
IndTab.index = pd.to_datetime(IndTab.index)
infectionpeak2 = IndTab["Infection Rate"].idxmax()
deathpeak2 = IndTab["Death Rate"].idxmax()
lag2 = np.abs(deathpeak2 - infectionpeak2)
print(IndTab)
ax[1, 0].plot(IndTab.index, IndTab["Infection Rate"], color='blue', label='Infection Rate')
ax[1, 0].plot(IndTab.index, IndTab["Death Rate"], color='red', label='Death Rate')
ax[1, 0].set_title('Rates of India')
ax[1, 0].set_xlabel('Date')
ax[1, 0].set_ylabel('Rate')
ax[1, 0].grid(True)
ax[1, 0].legend()
ChiTab = updateddata[updateddata["Country/Region"] == "China"]
ChiTab.index = pd.to_datetime(ChiTab.index)
infectionpeak3 = ChiTab["Infection Rate"].idxmax()
deathpeak3 = ChiTab["Death Rate"].idxmax()
lag3 = np.abs(deathpeak3 - infectionpeak3)
print(ChiTab)
ax[1, 1].plot(ChiTab.index, ChiTab["Infection Rate"], color='blue', label='Infection Rate')
ax[1, 1].plot(ChiTab.index, ChiTab["Death Rate"], color='red', label='Death Rate')
ax[1, 1].set_title('Rates of Pakistan')
ax[1, 1].set_xlabel('Date')
ax[1, 1].set_ylabel('Rate')
ax[1, 1].grid(True)
ax[1, 1].legend()
plt.show()

print(lag)
print(lag1)
print(lag2)
print(lag3)