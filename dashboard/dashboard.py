import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
 
def sumOrder (df):
    output = df.groupby("hours").count_cr.sum().sort_values(ascending=False).reset_index()
    return output

dayDf = pd.read_csv("day_clean.csv")
hourDf = pd.read_csv("hour_clean.csv")


datetimeColumns = ["dteday"]
dayDf.sort_values(by="dteday", inplace=True)
dayDf.reset_index(inplace=True)   

hourDf.sort_values(by="dteday", inplace=True)
hourDf.reset_index(inplace=True)

for column in datetimeColumns:
    dayDf[column] = pd.to_datetime(dayDf[column])
    hourDf[column] = pd.to_datetime(hourDf[column])

minDateDays = dayDf["dteday"].min()
maxDateDays = dayDf["dteday"].max()

minDateHour = hourDf["dteday"].min()
maxDateHour = hourDf["dteday"].max()

st.subheader("pada jam berapa yang paling banyak dan paling sedikit disewa?")
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))

sns.barplot(x="hours", y="count_cr", data=sumOrder(hourDf).head(5), palette=["grey", "grey", "green", "grey", "grey"], ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Hours (PM)", fontsize=30)
ax[0].set_title("Jam dengan banyak penyewa sepeda", loc="center", fontsize=30)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)

sns.barplot(x="hours", y="count_cr", data=sumOrder(hourDf).sort_values(by="hours", ascending=True).head(5), palette=["grey", "grey", "grey", "grey","red"], ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Hours (AM)",  fontsize=30)
ax[1].set_title("Jam dengan sedikit penyewa sepeda", loc="center", fontsize=30)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)

st.pyplot(fig)

st.subheader("pada musim apa yang paling banyak dan paling sedikit disewa?")
fig, ax = plt.subplots(figsize=(20, 10))

sns.barplot(y="count_cr", x="season", data=dayDf.sort_values(by="season", ascending=False), palette=["grey", "grey", "red", "green"],ax=ax)
ax.set_title("Grafik Antar Musim", loc="center", fontsize=50)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=35)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)