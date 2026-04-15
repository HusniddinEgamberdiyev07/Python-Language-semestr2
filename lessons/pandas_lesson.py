# data analyze and data manipulation

# sql -> Structure query language. Database language.

# data stored in rows and columns. They together will create a table.

# rows == tuples
# column names == attributes

# sql data is multi-demintional

# We can work with sql using pandas

import pandas as pd
import matplotlib.pyplot as plt

# s1 = pd.Series([[1,2,3,4], [12,34,90,0]])
# s1 = pd.Series([1,2,3,4])

# s1 = pd.Series([1,2,3,4], index=["a", "b", "c", "d"])
s1 = pd.Series({"id":1, "name":"husniddin", "age":18})
print(s1)
print(type(s1))


d1 = pd.DataFrame({"course":["Mcs2", "Discrete", "App"], "studens":["Husniddin", "Sardor", "Husan"]})
print(d1)

# dataframe inbuilt function

# 1. shape

# 2. describe()

# 3. head()

# 4. tail()

# data is in excel or in csv. CSV comma separeted values is faster than excel.
dataset = pd.read_csv('./csv/country_wise_latest.csv')
print(dataset, "\n")

print("head\n")

print(dataset.head(), "\n")

print("tail\n")

print(dataset.tail(), "\n")

print("shape\n")

print(dataset.shape, "\n")

print("top 60 records\n")

print(dataset.head(60), "\n")

print("records from 100 to 150 rows and from 0 to 11 columns")

print(dataset.iloc[100:150, 0:11], "\n")

# print(dataset.iloc[0:3, [0,2,4]], "\n")

print(dataset.loc[0:3, ["Country/Region","Deaths"]], "\n")

# iloc with indexes
# loc with names

# dataset.plot()
# plt.show()

print("condition\n")

countries = dataset.loc[dataset["Deaths"]>1000, ["Country/Region", "Deaths"]]
# print(countries.head(60), "\n")
print(countries, "\n")

asia = dataset.loc[(dataset["WHO Region"]=="Europe") & (dataset["Deaths"]>5000), ["Country/Region", "Deaths"]]
print(asia)
# countries.plot()
# plt.show()
