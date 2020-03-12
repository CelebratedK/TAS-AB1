import numpy as np
import math as m
import csv
import pandas as pd
import matplotlib.pyplot as plt
import scipy as scp

class universe:
    kelvin = 273.15

class dataFile:
    def __init__(self, fileName, filePath="AB1"):
        self.filePath = f"{filePath}\{fileName}"
        self.dataArray = self.getDataArray()
        self.dataArrayKelvin = self.getdataArrayKelvin()
        self.timeStepHours = self.dataArray[0][0][1] / 3600 #Take first time index, convert it from seconds to hours
        self.timeStepSeconds = self.dataArray[0][0][1]

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
        
        plt.show()


    

def main():
    a = dataFile("Baffle.csv")
    b = dataFile("Primary_mirror.csv")
    a.plotAllGraphs(units='K')
    b.plotAllGraphs(units='K')

if __name__ == "__main__":
    main()