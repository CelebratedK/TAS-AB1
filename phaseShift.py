"""Feel free to try wacky stuff with the data here.
You can also have a look at dataplotter.py if you wanna try and understand my code, but it's quite messy.

My programming is object-oriented, which a bit different from what you might be used to in python.
Feel free to ask if you have any questions! it's always harder to read someone else's code without context
"""

import dataPlotter
import matplotlib.pyplot as plt
import numpy as np

baffle, pMirror, sMirror = dataPlotter.createDataFiles()

bafflemaxima = baffle.getDiscreteMaximaVals() #list of maxima in format: [[[timelist],[valuelist]],[[timelist],[valuelist]]... for each component in the baffle
pmirrormaxima = pMirror.getDiscreteMaximaVals() #same as above


#example: if you want to get a list of time indices for the maximum temperatures for the 3rd element of the baffle,
#it would be = bafflemaxima[3][0][0]
#the list of temperature values for those times would be = bafflemaxima[3][1][0]


#For the phase shift, what you want to compute is the difference in time between the maxima in the mirrors and the baffle

#let's plot the baffle and primary mirror to see this:

x = baffle.dataArray[0][0] #time array
y1 = baffle.dataArray[5][1] #value array for the fifth element (the brown curve on the baffle graphs)
y2 = pMirror.dataArray[0][1] #value array for an element on the primary mirror

plt.plot(x,y1)
plt.plot(x,y2)

plt.vlines(pmirrormaxima[0][0][0],200,400)#add vertical lines on the maximum temperatures of the pMirror

plt.show()