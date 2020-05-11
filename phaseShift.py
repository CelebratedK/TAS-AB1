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
smirrormaxima = sMirror.getDiscreteMaximaVals() #same as above

#print(smirrormaxima)

print(bafflemaxima[0][0][0])
print(pmirrormaxima[0][0][1])
#Find time dealy between baffle and primary mirror
delaylist_pmirror = []
delaylist_pmirroraverage = []

lstj = []
lstl = []
for i in range(len(bafflemaxima)):
    for j in range(len(bafflemaxima[i][0])):
        lstj.append(j)
        
        for k in range(len(pmirrormaxima)):
            for l in range(len(pmirrormaxima[k][0])):
                lstl.append(l)
                
                if j == l:
                    timedelay_pmirror = abs(bafflemaxima[i][0][j] - pmirrormaxima[k][0][l])
                    delaylist_pmirror.append(timedelay_pmirror)
#print(lstj)
#print(lstl)
#print(bafflemaxima[0][0])
z = 0
averagetimedelay = 0
averagelist = []
for i in range(len(delaylist_pmirror)):
    averagetimedelay = averagetimedelay + delaylist_pmirror[i]
    z = z + 1
    if z == 9:
        average = averagetimedelay/10
        averagelist.append(average)
        averagetimedelay = 0
        z = 0
    
#print(averagelist)
        
#print(max(delaylist_pmirror))
print(len(bafflemaxima[6][0]))               
                
            
      

#print("This is the primary", delaylist_pmirror)
            

delaylist_smirror = []
for i in range(len(bafflemaxima)):
    for j in range(len(bafflemaxima[i][0])):
        for k in range(len(smirrormaxima)):
            for l in range(len(smirrormaxima[k][0])):
                if j == l:
                    timedelay_smirror = abs(bafflemaxima[i][0][j] - smirrormaxima[k][0][l])
                    delaylist_smirror.append(timedelay_smirror)
                
            
        

#print("This is the secondary", delaylist_pmirror) 
    
#example: if you want to get a list of time indices for the maximum temperatures for the 3rd element of the baffle,
#it would be = bafflemaxima[3][0]
#the list of temperature values for those times would be = bafflemaxima[3][1]


#For the phase shift, what you want to compute is the difference in time between the maxima in the mirrors and the baffle

#let's plot the baffle and primary mirror to see this:

x = baffle.dataArray[0][0] #time array
y1 = baffle.dataArray[5][1] #value array for the fifth element (the brown curve on the baffle graphs)
y2 = pMirror.dataArray[0][1] #value array for an element on the primary mirror

#Let's plot all the time delays over time





plt.plot(x,y1)
plt.plot(x,y2)

plt.vlines(pmirrormaxima[0][0],200,400)#add vertical lines on the maximum temperatures of the pMirror

plt.show()
