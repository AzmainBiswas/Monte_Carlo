import numpy as np
import csv


def evaluate_pi(N):
    Circ = 0
    for _ in range(1, N):
        X = np.random.uniform(-1, 1)
        Y = np.random.uniform(-1, 1)
        if X**2 + Y**2 <= 1:
            Circ = Circ + 1

    Area_of_circle = Circ / N
    value_of_pi = Area_of_circle * 4

    return value_of_pi


with open("Estimation_of_Pi.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["n", "Monte Carlo Estimate of PI"])

    for i in [100, 1000, 10000, 100000, 1000000, 10000000]:
        csv_writer.writerow([i, evaluate_pi(i)])
    file.close
