import dataPlotter
import matplotlib.pyplot as plt

baffle, pMirror, sMirror = dataPlotter.createDataFiles()

def withinTwoPercent(a,b):
    return abs(1 - a/b) < 0.02

def getTotalDeltaT(array):
    return array[-1] - array[0]




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


def main():
    baffle = dataPlotter.dataFile("Baffle.csv")
    maxima = baffle.getDiscreteMaximaVals() #list of maxima in format: [[[timelist],[valuelist]],[[timelist],[valuelist]]...

    totalTemperatureChange = []
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

    for orbit in partialDeltaT:
        plotOrbitTemperatureChange(orbit)

    #plt.show() 
    #calculation here pls

    halfOrbitTime = 365*24*3600/2
    maxDeltaT = sum(partialDeltaT[3])
    totalTime = timeArray[-1]
    

if __name__ == "__main__":
    main()