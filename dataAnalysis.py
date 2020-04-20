import dataPlotter
import matplotlib.pyplot as plt
import numpy as np

def withinTwoPercent(a,b):
    return abs(1 - a/b) < 0.02

def determinePeriod(array):
    guess = array[1]-array[0]
    guesses = []
    for i in range(len(array)-1):
        value = withinTwoPercent(array[i+1]-array[i], guess)
        guesses.append(value)
    print(guesses)
    return guess

def main():
    baffle = dataPlotter.dataFile("Baffle.csv")
    maxima = baffle.getDiscreteMaximaVals() #list of maxima in format: [[[timelist],[valuelist]],[[timelist],[valuelist]]...
    for i in range(len(maxima)):
        timeArray = maxima[i][0][0]
        valueArray = maxima[i][1][0]
        print(determinePeriod(timeArray))


if __name__ == "__main__":
    main()