#Through this program, i am plotting the graph for comparison of year wise percentage of usage of bus.

import numpy as np 
import matplotlib.pyplot as plt  
  
   
# creating the dataset 
data = {'2015':71, '2016':81, '2017':84,  
        '2018':79, '2019':85} 
courses = list(data.keys()) 
values = list(data.values()) 
   
fig = plt.figure(figsize = (10, 5)) 
  
# creating the bar plot 
plt.bar(courses, values, color ='maroon',  
        width = 0.4) 
  
plt.xlabel("Year wise Comparison") 
plt.ylabel("Percentage Usage of Buses") 
plt.title("Buses Usage Survey of 4 Years") 
plt.show() 
