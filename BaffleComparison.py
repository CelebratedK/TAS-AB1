import dataPlotter
import matplotlib.pyplot as plt
import numpy as np
import scipy as scp

baffle, pMirror, sMirror = dataPlotter.createDataFiles()

baffle.dataArray #This array has shape: [[timelist,temperaturelist],[timelist,temperaturelist]....]

#Example below: plot temperature against time for the first sensor on the baffle




array = baffle.giveMeASpline()
spline1 = array[0]
spline2 = array[5]
dsdx1 = spline1.derivative(1)
dsdx2 = spline2.derivative(1)

#print(dsdx1.roots()) # Easy way to get all roots of a function

x = baffle.newTimeArray(10)
y1 = spline1(x)
y2 = spline2(x)
"""
plt.plot(x,dsdx1(x),x,dsdx2(x))
plt.xlim(4500.,5000.)
plt.show()
"""
substracted = y2-y1

spline3 = scp.interpolate.CubicSpline(x,substracted)
intersections = spline3.roots()



"""
plt.plot(baffle.dataArray[0][0],baffle.dataArray[0][1],baffle.dataArray[5][0],baffle.dataArray[5][1])
plt.ylim(58.,66)
plt.xlim(4000.,7500.)
plt.show()
"""


