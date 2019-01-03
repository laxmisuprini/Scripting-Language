import pandas as pd
from pandas import Series,DataFrame
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


student_df=pd.read_csv("StudentsPerformance.csv")

print("---------header rows----------")
print(student_df.head())
print("--------description---------")
student_df.info()
student_df.describe()
student_df1=student_df.drop(["lunch","test preparation course"],axis=1)
print(student_df1.head())
student_df1["parental level of education"]=student_df1["parental level of education"].fillna("high school")
print(student_df1["parental level of education"])
student_df1["race/ethnicity"]=student_df1["race/ethnicity"].map({
                               "group A":"Asian Students",
                               "group B":"African Students",
                               "group C":"Afo-Asian Students",
                               "group D":"American Students",
                               "group E":"European Students"
                              })
print(student_df1["race/ethnicity"])

ax=sns.countplot(x="test preparation course",hue="gender",palette="Set1",data=student_df)
ax.set(title="tally",xlabel="courses",ylabel="total")
plt.show()

ax=sns.countplot(x="race/ethnicity",hue="gender",palette="Set1",data=student_df)
ax.set(title="tally",xlabel="groups",ylabel="total")
plt.show()
interval=[0,40,50,60,75]
category=["failed","second class","first class","distinction"]


student_df1["maths_category"]=pd.cut(student_df1.mathscore,interval,labels=category)
ax=sns.countplot(x="maths_category",hue="gender",palette="Set1",data=student_df1)
ax.set(title="tally",xlabel="maths",ylabel="total")
plt.show()



student_df1["read_category"]=pd.cut(student_df1.readingscore,interval,labels=category)
ax=sns.countplot(x="read_category",hue="gender",palette="Set1",data=student_df1)
ax.set(title="tally",xlabel="read",ylabel="total")
plt.show()


student_df1["write_category"]=pd.cut(student_df1.writingscore,interval,labels=category)
ax=sns.countplot(x="write_category",hue="gender",palette="Set1",data=student_df1)
ax.set(title="tally",xlabel="write",ylabel="total")
plt.show()


