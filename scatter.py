import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1, 4 , 9 , 16 , 25 ] 

plt.scatter(x_values, y_values , s= 100)

# set chart title and axes

plt.title("Square Numbers in Scatter Plot" , fontsize = 24 )
plt.xlabel("Value" , fontsize = 14 ) 
plt.ylabel("Square of Value", fontsize=14)

plt.show()

