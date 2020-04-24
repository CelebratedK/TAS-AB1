import dataPlotter
import matplotlib.pyplot as plt
import numpy as np

def withinTwoPercent(a,b):
    return abs(1 - a/b) < 0.005

def getTotalDeltaT(array):
    return array[-1] - array[0]

def getFinalTemperature(array):
    return array[-1]

def getMean(array):
    mean = np.mean(array)
    sigma = np.std(array)
    return mean,sigma

def getOrbitDeltaT(list):
    deltaTList = []

    for i in range(len(list)-1):
        dT = list[i+1] - list[i]
        deltaTList.append(dT)

    return deltaTList

def plotOrbitTemperatureChange(DeltaT): #Expects a 1d list
    x = range(len(DeltaT))
    plt.plot(x,DeltaT)
    plt.xlabel("Orbit number")
    plt.ylabel("Temperature change (K)")


def main(dataFile):
    maxima = dataFile.getDiscreteMaximaVals() #list of maxima in format: [[[timelist],[valuelist]],[[timelist],[valuelist]]...

    TotalTemperatureDelta = []
    partialDeltaT = []

    for i in range(len(maxima)):
        deltaT = []

        timeArray = maxima[i][0][0]
        valueArray = maxima[i][1][0]
        for i in valueArray:
            m = max(valueArray)
            if withinTwoPercent(i, m):
                deltaT.append(i)
        
        partialDeltaT.append(getOrbitDeltaT(deltaT))
    
    finaldeltaTlist = []

    for orbit in partialDeltaT:
        plotOrbitTemperatureChange(orbit)
        TotalTemperatureDelta.append(sum(orbit))
        lastdeltaT = orbit[-1]
        finaldeltaTlist.append(lastdeltaT)
    
    print(TotalTemperatureDelta)
    print(f"Average temperature change over all components is {np.mean(TotalTemperatureDelta)} K")

    for i in finaldeltaTlist:
        print(f"The last change in temperature was {i} Kelvins \n")

    plt.show()


if __name__ == "__main__":
    for df in dataPlotter.createDataFiles():
        main(df)