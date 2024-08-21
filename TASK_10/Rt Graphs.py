
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Loading the COVID Dataset
coviddata = pd.read_csv("country_wise_latest.csv")
#print(coviddata.head())

coviddata1 = pd.read_csv("full_grouped.csv")

# Filter the data for specific countries
mask = ["China", "India", "Pakistan", "Bangladesh"]
filtered = coviddata1[coviddata1["Country/Region"].isin(mask)]

# Convert Date to datetime and set it as the index
filtered["Date"] = pd.to_datetime(filtered["Date"])
filtered.set_index('Date', inplace=True)

print(filtered)

# Group the data by Country/Region
grouped = filtered.groupby("Country/Region")

# Function to calculate the 7-Day Moving Average of New cases and Rt
def CalculateMovingAverage(eachgroupofcountries):
    eachgroupofcountries["New Cases Moving Average"] = eachgroupofcountries["New cases"].rolling(window=3).mean()
    eachgroupofcountries['New Cases MA Shifted'] = eachgroupofcountries['New Cases Moving Average'].shift(3)
    eachgroupofcountries["Reproductive Number"] = eachgroupofcountries['New cases'] / eachgroupofcountries['New Cases MA Shifted']
    return eachgroupofcountries

# Apply the function to each group
result = grouped.apply(CalculateMovingAverage)
result.replace([np.inf, -np.inf], np.nan, inplace=True)
# Drop rows with NaN in Reproductive Number
result.dropna(subset=["Reproductive Number"], inplace=True)
result = result.drop_duplicates()
# Reset index to flatten the DataFrame
result = result.reset_index(level="Country/Region", drop=True)
print(result)
print(max(result["Reproductive Number"]))
print(result.sort_values(by="Reproductive Number"))

index_value = '2020-03-15'
single_row = result.loc[index_value]
print(single_row)


fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 8), sharex=True)
# Plot on the first subplot (top-left)
BanTab = result[result["Country/Region"] == "Bangladesh"]
print(BanTab)
ax[0, 0].scatter(BanTab.index, BanTab["Reproductive Number"], color='blue')
ax[0, 0].set_title('COVID-19 Effective Reproductive Number for Bangladesh')
ax[0, 0].set_xlabel('Date')
ax[0, 0].set_ylabel('Reproductive Number (Rt)')
ax[0, 0].grid(True)
PakTab = result[result["Country/Region"] == "Pakistan"]
print(PakTab)
ax[0, 1].scatter(PakTab.index, PakTab["Reproductive Number"], color='red')
ax[0, 1].set_title('COVID-19 Effective Reproductive Number for Pakistan')
ax[0, 1].set_xlabel('Date')
ax[0, 1].set_ylabel('Reproductive Number (Rt)')
ax[0, 1].grid(True)
IndTab = result[result["Country/Region"] == "India"]
print(IndTab)
ax[1, 0].scatter(IndTab.index, IndTab["Reproductive Number"], color='green')
ax[1, 0].set_title('COVID-19 Effective Reproductive Number for India')
ax[1, 0].set_xlabel('Date')
ax[1, 0].set_ylabel('Reproductive Number (Rt)')
ax[1, 0].grid(True)
ChiTab = result[result["Country/Region"] == "China"]
print(ChiTab)
ax[1, 1].scatter(ChiTab.index, ChiTab["Reproductive Number"], color='purple')
ax[1, 1].set_title('COVID-19 Effective Reproductive Number for China')
ax[1, 1].set_xlabel('Date')
ax[1, 1].set_ylabel('Reproductive Number (Rt)')
ax[1, 1].grid(True)
plt.show()

