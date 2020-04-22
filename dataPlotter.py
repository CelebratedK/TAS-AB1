import numpy as np
import math as m
import csv
import pandas as pd
import matplotlib.pyplot as plt
import scipy as scp
from scipy.signal import argrelextrema

class universe: #Write universal constants here. You can use them anywhere in the code with: universe.constant
    constant = 1
    kelvin = 273.15
    filenames = ["Baffle.csv","Primary_mirror.csv","Secondary_mirror.csv"]

class dataFile:
    def __init__(self, fileName, filePath="AB1"):
        self.filePath = f"{filePath}\{fileName}"
        self.dataArray = self.getDataArray()
        self.dataArrayKelvin = self.getdataArrayKelvin()
        self.timeStepHours = self.dataArray[0][0][1] / 3600 #Take first time index, convert it from seconds to hours
        self.timeStepSeconds = self.dataArray[0][0][1]      #I took these to try make a fourrier transform of the data, but didn't go well ;(
        self.localMaximaDiscrete = self.getDiscreteMaxima() #returns list of indices
        self.localMinimaDiscrete = self.getDiscreteMinima()

    def getDataArray(self):
        data = pd.read_csv(self.filePath,skiprows=5)
        data.drop(data.tail(1).index, inplace=True)
        dataArray = np.transpose(data.to_numpy())
        dataArray = np.split(dataArray,len(dataArray)/2)
        return dataArray #dataarray has format [[time,value],[time,value]....]

    def getdataArrayKelvin(self):
        KelvinArray = self.getDataArray()
        for element in KelvinArray:
            element[1]+=universe.kelvin
        return KelvinArray

    def plotAllGraphs(self, units='C'):
        if units == 'K':
            plotArray = self.dataArrayKelvin
        elif units == 'C':
            plotArray = self.dataArray

        for data in plotArray:
            x = data[0]
            y = data[1]
            plt.plot(x,y)
    
    def getArrayNames(self):    #generate a list of the element names from the CSV file
        data = pd.read_csv(self.filePath,skiprows=1)
        names = []
        dataArray = data.to_numpy()
        for i in range(int(len(data.columns)/2)):
            names.append(dataArray[0][2*i+1])
        return names

    def getDiscreteMaxima(self): #generate a list of indices of the local maximums for a given list of temperatures
        indicesList = []
        for array in self.dataArray:
            iterArray = array[1]
            indicesList.append(argrelextrema(iterArray,np.greater)) #argrelextrema is a wacky scipy function, returns the indices of all extrema in a signal
        return indicesList
    
    def getDiscreteMinima(self): #same function as above, but for local minima
        indicesList = []
        for array in self.dataArray:
            iterArray = array[1]
            indicesList.append(argrelextrema(iterArray,np.less))
        return indicesList

    def indicesToVals(self,indexArray):
        output=[]
        for i, lst in enumerate(indexArray):
            vals = []
            time = []
            for element in lst:
                vals.append(self.dataArray[i][1][element])
                time.append(self.dataArray[i][0][element])
            output.append([time,vals])
        return output

    def getDiscreteMaximaVals(self):
        return self.indicesToVals(self.localMaximaDiscrete)

    def getDiscreteMinimaVals(self):
        return self.indicesToVals(self.localMinimaDiscrete)

    def giveMeASpline(self): #returns an array of scipy spline functions
        tempArray = self.dataArray
        newArray = []
        for dataset in tempArray:
            spline = scp.interpolate.CubicSpline(dataset[0],dataset[1])
            newArray.append(spline)
        return newArray

    def newTimeArray(self, nFactor): #nFactor=3 will make a time array with 3 times as many points
        timeArray = self.dataArray[0][0]
        maxTime = timeArray[-1]
        nDataPoints = len(timeArray)
        newTimeArray = np.linspace(0,maxTime, nFactor * nDataPoints)
        return newTimeArray

def createDataFiles():
    baffle = dataFile(universe.filenames[0])
    pMirror = dataFile(universe.filenames[1])
    sMirror = dataFile(universe.filenames[2])
    return (baffle, pMirror, sMirror)

def main(): #Just doodle code here to test is my functions work xd. Just ignore this
    a = dataFile(universe.filenames[0])
    splines = a.giveMeASpline()
    x = a.newTimeArray(5)
    plt.plot(a.dataArray[1][0],a.dataArray[1][1])
    plt.plot(x, splines[1](x,1))
    plt.show()
    print(a.getDiscreteMaximaVals())

if __name__ == "__main__": #This will only run if you run this scirpt directly; won't run if you import it in another program
    main()