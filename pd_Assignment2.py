import pandas as pd
df1=pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user")
print(df1.head())

#Assign it to a variable called users and use the 'user_id' as index
print("\t**Assign it to a variable called users and use the 'user_id' as index**")
users = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user", sep="|", index_col="user_id")

#See the first 10
print("\t**Seeing the first 10**") 
print(users.head(10))

#See the last 10
print("\t**Seeing the last 10**")
print(users.tail(10))

#Number of Obeservation in dataset
print("Total Numbers of observations",users.shape[0])

#What is the number of columns in the dataset?
print("\nThe number of columns in the dataset",users.shape[1])

#Print the name of all the columns.
print(users.columns)

# How is the dataset indexed?
print("\n",users.index)

#What is the data type of each column?
print("\n",users.dtypes)

#Print only the occupation column
a=users["occupation"]
print(a)

#How many different occupations are in this dataset?
print("\n",a.value_counts().count())

#What is the most frequent occupation?
print("\n",a.value_counts().sort_values(ascending=False).head())

#DataFrame Info.
print("\n",)
#Describe all the columns
print("\n",users.describe(include="all"))
#Summarize only the occupation column
print("\n",users.occupation.describe())
#What is the mean age of users?
print("\n",users.age.mean())
#What is the age with least occurrence?
print("\n",users.age.value_counts().tail())
