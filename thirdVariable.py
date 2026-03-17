import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('student_data')

# print(df.sex)

# sns.scatterplot(data = df , x = df.total_bill  , y = df.tip  , hue= df.sex ,hue_order = ['Female' , 'Male'] )

# plt.show()

print(df.head())


