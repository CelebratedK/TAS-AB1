import dataPlotter
import numpy as np
import matplotlib.pyplot as plt

baffle, pMirror, sMirror = dataPlotter.createDataFiles()

def formatGraphs(dataFile): #put all the formatting stuff here
    plt.legend(dataFile.getArrayNames(),loc='upper left')
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (K)")
    plt.show()

def main(): #Just doodle code here to test is my functions work xd. Just ignore this

    splines = baffle.giveMeASpline() #this array has shape [[splineFunction],[splineFunction]]
    newDataPoints = baffle.newTimeArray(5)

    for function in splines:
        plt.plot(newDataPoints, function(newDataPoints,1))

    plt.legend(baffle.getArrayNames(),loc='upper left')
    plt.xlabel("Time (s)")
    plt.ylabel("Rate of change of temperature (K/s)")

    plt.show()

if __name__ == "__main__": #This will only run if you run this scirpt directly; won't run if you import it in another program
    main()