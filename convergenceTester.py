import dataPlotter
import matplotlib.pyplot as plt
import numpy as np

baffle, pMirror, sMirror = dataPlotter.createDataFiles()

def main(df):
    for component in df.dataArray:
        d = component[1] #dataArray
        t = component[0] #dataArray
        convergenceCriterion = []
        for index in range(round(len(d)/80)):
            convergenceCriterion.append(np.mean(d[0:index * 80]))
        plt.plot(range(round(len(d)/80)),convergenceCriterion)
    plt.show()

if __name__ == "__main__":
    for i in dataPlotter.createDataFiles():
        main(i)