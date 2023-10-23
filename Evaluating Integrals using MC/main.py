import numpy as np
import matplotlib.pyplot as plt
import csv

UpLimit = 1  # upper limit
LowerLimit = 0  # lower limit


def fun(x):  # function to be integrated
    return np.exp(-(x**2) / 2)


def MonteCarlo(fun, UpLimit, LowerLimit, SimNumber):
    I = 10000  # number of itaration
    IntegralValues = []
    for i in range(SimNumber):
        X = np.random.uniform(LowerLimit, UpLimit, I)
        ValuesOfFunction = fun(X)
        SumfFunction = ValuesOfFunction.sum()
        IntegralValue = SumfFunction / float(len(ValuesOfFunction))
        IntegralValues.append(IntegralValue)
    return sum(IntegralValues) / len(IntegralValues)


with open("Value_of_Integral.csv", "w", newline='') as file:
    writter = csv.writer(file)
    writter.writerow(["n", "Value of Integration"])
    for n in [50, 100, 1000, 10000, 100000]:
        writter.writerow([n,MonteCarlo(fun=fun, UpLimit=UpLimit, LowerLimit=LowerLimit, SimNumber=n)])
    file.close
    
