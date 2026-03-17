import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Feature_Engineering\laptopData.csv") 
# print(df.columns)
# sns.countplot(data = df , x = df['Company']  )
sns.scatterplot(data = df , x = df.Price , y = pd.to_numeric(df.Inches , errors = 'coerce') )
plt.show()
sns.countplot(data = df , x = df['Company']  )
plt.show()