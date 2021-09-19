#Assignment 1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [0,2,4,6,8]

#Resize the graph
plt.figure(figsize=(7,6), dpi=100)

#Plot a line graph
plt.plot(x,y,label='2x', color='gray', marker='v', linestyle='dashed', markersize=15, markeredgecolor='k', linewidth=4)

# Add a title, labels, legend to your graph
plt.title('line chart')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()

#Save the graph
plt.savefig('mygraph.png', dpi=300)
plt.show()