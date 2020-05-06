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
            try:
                convergenceCriterion.append(np.mean(d[(index-1)*80:index * 80]))
            except Exception:
                pass
        plt.plot(range(round(len(d)/80)),convergenceCriterion)

        finalAvgDifference = convergenceCriterion[-2] - convergenceCriterion[-3]
        factor = finalAvgDifference / convergenceCriterion[-1]
        print(f"Average temperature difference in the last two orbits was {finalAvgDifference} Kelvins, which is a {factor} convergence factor")
    print("next csv file: \n")
    plt.show()

if __name__ == "__main__":
    for i in dataPlotter.createDataFiles():
        main(i)