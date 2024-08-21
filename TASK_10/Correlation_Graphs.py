import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the COVID-19 dataset
coviddata = pd.read_csv("country_wise_latest.csv")
coviddata1 = pd.read_csv("full_grouped.csv")

mask = ["China", "India", "Pakistan", "Bangladesh"]
filtered = coviddata1[coviddata1["Country/Region"].isin(mask)]
data  = filtered.groupby("Country/Region")[["Confirmed","Deaths","Recovered"]].sum()
def calculate_correlation_conf_deaths(group):
    return group[['Confirmed', 'Deaths']].corr().iloc[0, 1]
data['corr_death'] = filtered.groupby('Country/Region').apply(calculate_correlation_conf_deaths)
data['corr_death'] = data['corr_death'].round(2)
def calculate_correlation_conf_rec(group):
    return group[['Confirmed', 'Recovered']].corr().iloc[0, 1]
data['corr_rec'] = filtered.groupby('Country/Region').apply(calculate_correlation_conf_rec)
data['corr_rec'] = data['corr_rec'].round(2)
print(data)
fig, ax = plt.subplots(ncols=2, nrows=1, figsize=(14, 6))

sns.scatterplot(data=data, x="Confirmed", y="Deaths", hue="Country/Region", ax=ax[0], palette="viridis")
ax[0].set_title('Confirmed Cases vs Deaths | Annotation : Correlation Coefficient')
ax[0].set_xlabel('Confirmed Cases')
ax[0].set_ylabel('Deaths')
ax[0].grid(True)

for i in range(data.shape[0]):
    ax[0].text(data["Confirmed"].values[i],data["Deaths"].values[i], data["corr_death"].values[i],fontdict={'fontsize': 10, 'color': 'black'},
        ha='left',
        va='bottom') 


sns.scatterplot(data=data, x="Confirmed", y="Recovered", hue="Country/Region", ax=ax[1], palette="viridis")
ax[1].set_title('Confirmed Cases vs Recovered | Annotation : Correlation Coefficient')
ax[1].set_xlabel('Confirmed Cases')
ax[1].set_ylabel('Recovered')
ax[1].grid(True)

for i in range(data.shape[0]):
    ax[1].text(data["Confirmed"].values[i],data["Recovered"].values[i], data["corr_rec"].values[i],fontdict={'fontsize': 10, 'color': 'black'},
        ha='left',
        va='bottom')

plt.tight_layout()
plt.show()

