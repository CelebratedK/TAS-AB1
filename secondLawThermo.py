import dataPlotter
import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

baffle, pMirror, sMirror = dataPlotter.createDataFiles()

def formatGraphs(dataFile): #put all the formatting stuff here
    plt.legend(dataFile.getArrayNames(),loc='upper left')
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (K)")
    plt.show()

def fourrierTransform(dataArray): #expects [[timelist],[datalist]]
    x = dataArray[0]
    y = dataArray[1]

    N = len(y)
    T = x[1]-x[0]
    
    yf = fft(y)
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    
    plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
    plt.grid()
    plt.show()

def main(): #Just doodle code here to test is my functions work xd. Just ignore this

    splines = baffle.giveMeASpline() #this array has shape [[splineFunction],[splineFunction]]
    newDataPoints = baffle.newTimeArray(5)

    for function in splines:
        dydx = function.derivative(1)
        plt.plot(newDataPoints, dydx(newDataPoints))
        roots = dydx.roots()
        print(roots)
        input()

    plt.legend(baffle.getArrayNames(),loc='upper left')
    plt.xlabel("Time (s)")
    plt.ylabel("Rate of change of temperature (K/s)")

    plt.show()

    xtest = baffle.newTimeArray(5)
    ytest = splines[0](xtest,1)

    fourrierTransform(np.array([xtest/3600,ytest]))



if __name__ == "__main__": #This will only run if you run this scirpt directly; won't run if you import it in another program
    main()