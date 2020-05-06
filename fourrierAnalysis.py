import matplotlib.pyplot as plt
import numpy as np
from scipy import fft
import dataPlotter


def fourrierTransform(dataArray, inverseXAxis=False): #expects [[timelist],[datalist]]
    x = dataArray[0]
    y = dataArray[1]

    N = len(y)
    T = x[1]-x[0]
    
    yf = fft(y)
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    xlabel = "Frequency (Hz)"

    if inverseXAxis:
        xf = 1/xf
        xlabel = "Period (s)"

    
    plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
    plt.grid()
    plt.xlabel(xlabel)
    plt.ylabel("Amplitude (-)")
    


def main():
    baffle, pMirror, sMirror = dataPlotter.createDataFiles()
    splines = baffle.giveMeASpline()
    names = baffle.getArrayNames()

    index = int(input("Index: (number between 0 and 7) \n"))

    t = baffle.newTimeArray(5)
    d = splines[index](t,1)

    fourrierTransform([t,d],inverseXAxis=False)


    plt.title(names[index])
    plt.show()


if __name__ == "__main__":
    while 1:
        main()