# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 16:45:02 2022

@author: Zhonghao Jiang, Yang Zhao

Only for PhD Python Workshop, Univeristy of Glasgow.
"""

#%% Practice 1
# Import matplotlib with the usual abbreviation mpl.
import matplotlib as mpl # The version of matplotlib used.
# Import the main plotting sub package with the usual abbreviation plt.
import matplotlib.pyplot as plt 
# Import the data package
import numpy as np

# Draws the random numbers (xy values).
y = np.random.standard_normal(20)
x = np.random.standard_normal(20)
# Calls the plt.plot() function with the x and y objects.
# plot() function plots continuous lines by default
plt.plot(x, y)

#plot figures with labels and titles
plt.plot(x,y)
plt.figure(figsize=(16, 6)) # Increases the size of the figure.
plt.plot(x,y, 'b', lw=1.5) # Plots the data as a line in blue with line width of 1.5 points.
plt.plot(x,y, 'ro') # Plots the data as red (thick) dots.
plt.xlabel('index') # Places a label on the x-axis.
plt.ylabel('value') # Places a label on the y-axis.
plt.title('A Simple Plot')  # Places a title.


#%% Static 3D Plotting

# Case of a European call option
# Strike values between 50 and 150
strike = np.linspace(50, 150, 24)
# Times-to-maturity between 0.5 and 2.5 years
ttm = np.linspace(0.5, 2.5, 24)
# The two two-dimensional ndarray objects (grids) created.
strike, ttm = np.meshgrid(strike, ttm)
strike[:2].round(1)
iv = (strike - 100) ** 2 / (100 * strike) / ttm
iv[:5, :3]

# Imports the relevant 3D plotting features, which is required 
# although Axes3D is not directly used.
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(10, 6))
ax = fig.gca(projection='3d') # Sets up a canvas for 3D plotting.
surf = ax.plot_surface(strike, ttm, iv, rstride=2, cstride=2,
                       cmap=plt.cm.coolwarm, linewidth=0.5,antialiased=True)
ax.set_xlabel('strike')
ax.set_ylabel('time-to-maturity')
ax.set_zlabel('implied volatility')
fig.colorbar(surf, shrink=0.5, aspect=5);














