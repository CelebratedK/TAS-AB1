import dataPlotter
import matplotlib.pyplot as plt

def formatGraphs(dataFile): #put all the formatting stuff here
    plt.legend(dataFile.getArrayNames(),loc='upper left')
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (K)")
    plt.show()

def plotDataFromObject(dataFile):
    dataFile.plotAllGraphs(units='K')
    formatGraphs(dataFile)

def main():
    namelist = dataPlotter.universe.filenames #This is a list: ["Baffle.csv","Primary_mirror.csv","Secondary_mirror.csv"]
    
    baffleData = dataPlotter.dataFile(namelist[0])
    primaryMData = dataPlotter.dataFile(namelist[1])
    SecondaryMData = dataPlotter.dataFile(namelist[2])

    plotDataFromObject(baffleData)
    plotDataFromObject(primaryMData)
    plotDataFromObject(SecondaryMData)


if __name__ == "__main__":   #This segment of code will only run if you are running it directly (it won't run if you import it to another file)
    main()