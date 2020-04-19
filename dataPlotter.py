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
        self.localMaximaDiscrete = self.getDiscreteMaxima()
        self.localMinimaDiscrete = self.getDiscreteMinima()

    def getDataArray(self):
        data = pd.read_csv(self.filePath,skiprows=5)
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

    

def main(): #Just doodle code here to test is my functions work xd. Just ignore this
    a = dataFile("Baffle.csv")
    plt.plot(a.dataArray[0][0],a.dataArray[0][1])
    print(a.dataArray[0][0][a.localMaxima[0]])
    plt.show()

if __name__ == "__main__": #This will only run if you run this scirpt directly; won't run if you import it in another program
    main()