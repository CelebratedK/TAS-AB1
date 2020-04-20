"""Feel free to try wacky stuff with the data here.
You can also have a look at dataplotter.py if you wanna try and understand my code, but it's quite messy.

My programming is object-oriented, which a bit different from what you might be used to in python.
Feel free to ask if you have any questions! it's always harder to read someone else's code without context
"""

import dataPlotter
import matplotlib.pyplot as plt

baffle, pMirror, sMirror = dataPlotter.createDataFiles()

baffle.dataArray #This array has shape: [[timelist,temperaturelist],[timelist,temperaturelist]....]

#Example below: plot temperature against time for the first sensor on the baffle

x = baffle.dataArray[0][0]
y = baffle.dataArray[0][1]

plt.plot(x,y)
plt.show()
