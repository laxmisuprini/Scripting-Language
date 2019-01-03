import pandas as pd
from pandas import Series,DataFrame
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("BlackFriday.csv");

print("------header------");
print("df.head()");
print("------description-------");
df.info();
df.describe();
df=df.drop(["User_ID","Product_ID","Stay_In_Current_City_Years"],axis=1);
print(df.head());
df["City_Category"]=df["City_Category"].fillna("B");
print(df["City_Category"]);
df["City_Category"]=df["City_Category"].map({
                      "A":"Metro Cities",
                      "B":"Small Towns",
                      "C":"Villages"});
print(df.head());
df=df.rename(columns={"Product_Category_1":"Baseball Caps","Product_Category_2":"Wine Tumblers","Product_Category_3":"Pet Raincoats"});
print(df.head());

df["Marital_Status"]=df["Marital_Status"].map({
                         1:"Married",
                         0:"Un-Married"});
print(df.head());
df["Baseball Caps"]=df["Baseball Caps"].fillna(8);
df["City_Category"]=df["Wine Tumblers"].fillna(10);

ax=sns.countplot(x="Baseball Caps",hue="Gender",palette="Set1",data=df);
ax.set(title="tally",xlabel="product_1",ylabel="total");
plt.show();

ax=sns.countplot(x="Wine Tumblers",hue="Gender",palette="Set1",data=df);
ax.set(title="tally",xlabel="product_2",ylabel="total");
plt.show();
ax=sns.countplot(x="City_Category",hue="Gender",palette="Set1",data=df);
ax.set(title="tally",xlabel="cities",ylabel="total");
plt.show();


