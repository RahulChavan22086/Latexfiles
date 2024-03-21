import random
# import numpy as np
# import math
import matplotlib.pyplot as plt

n=20
N=100000

def realisation():
    sum = 0
    for i in range(n):
        if random.random() < 0.5:
            sum += 1 / (3 ** i)
    return sum

realisations = []
for j in range(N):
    realisations.append(realisation)

plt.hist(realisations)
plt.show()