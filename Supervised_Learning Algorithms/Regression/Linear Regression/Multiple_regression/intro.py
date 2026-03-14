import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

data_frame = pd.read_csv("Supervised_Learning Algorithms\Regression\Linear Regression\Multiple_regression\sample_regression_data.csv")
(data_frame.describe())
# print((data_frame.Location_Type))
# plt.hist(data_frame.Location_Type , bins = 3)

x = (data_frame.Study_Hours.info())

x1 = data_frame.Study_Hours
x2 = data_frame.Sleep_Hours
y = data_frame.Performance_Score.to_numpy()

l1 = np.array([1,3,3])
l2 = np.array([3,5,6])
l3 = np.array([5,7,8])
ones = np.array(np.ones(len(x1))) 
# X = np.vstack([(ones) , (x1) ,(x2)])
X = np.array([ones ,x1 , x2 ]).T
# print(X.shape)
# print(y.shape)
t1 = 0 
t2 = 0 
t3 = 0 
theta = np.array([t1,t2,t3])

product_transpose = np.dot(X,theta)
# cost  = np.dot(product_transpose - y , product_transpose - y )

multipy_tv = np.dot(X.T , X)
mulitply_inverse = np.linalg.inv(multipy_tv)
product = np.dot(mulitply_inverse , X.T)
theta = np.dot(product , y)

print(theta)

# cost  = np.dot(product_transpose - y , product_transpose - y )

# print(cost)

x1_X2_rel = np.cov(x1,x2)
print(x1_X2_rel)
colors = y
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111 , projection = '3d')

ax.scatter(x1 , x2 , y , c = colors  ,cmap= "viridis")
ax.set_xlabel("Study Hours")
ax.set_ylabel("Sleep Hours")
ax.set_zlabel("Performane Score")
ax.set_title("Multiple Linear Regression Model")
x1_values = np.linspace(min(x1) , max(x1) , 100)
x2_values = np.linspace(min(x2) , max(x2) , 100)
x1_plot_val , x2_plot_val = np.meshgrid(x1_values , x2_values)
z = theta[0] +  theta[1] *  x1_plot_val + theta[2] * x2_plot_val

ax.plot_surface(x1_plot_val , x2_plot_val , z , alpha = 0.4)

# ax.plot(x1 , )
plt.show()