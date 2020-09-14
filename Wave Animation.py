# -*- coding: utf-8 -*-
"""
Parampreet Singh | parampreet_singh@hotmail.com
Simple Python Animation Tutorial/Practice
Adapted from Jake Vanderplas (vanderplas@astro.washington.edu)
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation



#Set up a figure
fig=plt.figure()

#Set up some axes
axes=plt.axes(xlim=(0,2), ylim=(-2, 2))

#Plot the element which we want to animate
line, =axes.plot([], [], lw=2)

#Create the first function for the animation to happen, this function will be called to create the base frame
#for where the animation takes place
#use just a simple function which sets the line data to nothing 
#It is important that this function return the line object, because this tells the animator which objects on the plot to update after each frame
def init():
    line.set_data([], [])
    return line,

#Animation function which takes a single parameter, the frame number i, and draws a sine wave with a shift that depends on i
def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

#Call the animator
#blit=True means only re-draw the parts that have changed
A=animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=15, blit=True)

#Save the animation as an MP4 file
#You may need to install PillowWriter there are various online resources of how to do this
#If you are using anaconda simply go to the anaconda prompt and type: conda install -c anaconda pillow
A.save('Animation.gif', writer="PillowWriter")

#Give a title to the animation and the axes then show it
plt.title("Wave Animation!")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()