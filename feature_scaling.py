import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Feature_Engineering\laptopData.csv") 
# df.drop(df.Unnamed)
print((df.Inches.dtype))
# Convert the Inches from str to float64
df.Inches = pd.to_numeric(df.Inches , errors = 'coerce')
# Now task is to remove the null values and replace with the mean of the column 
df.Inches = df.Inches.fillna(df.Inches.mean())
# Now NaN values boil down to 0
print(df.Inches.isnull().sum())
print(df.Weight)
df.Weight = df['Weight'].replace('kg' , '',regex = True)
df.Weight = pd.to_numeric(df.Weight , errors = 'coerce')
# print(df.Weight)
print(df.Weight.values)

df.Inches_dash = (df.Inches.values - df.Inches.mean()) / df.Inches.std()

print(df.Inches_dash)

print(df.Weight)
# Now Convert the 

# plt.scatter(df.Weight , df.Inches_dash)
# plt.xlabel("Weights in kg")
# plt.ylabel("Pixels in inches")
# plt.title("Distribution Curve")
fig , (ax1 , ax2) = plt.subplots(nrows = 2)
sns.kdeplot(x = df.Inches_dash , ax = ax1 )
# ax1.xlabel('')
# plt.show()
sns.kdeplot(x = df.Inches  , ax = ax2)
# sns.countplot(x = df.)

plt.show()

