from random import random, seed
import matplotlib.pyplot as plt


def randVector(n, weightTab):
    tab = []
    for i in range(n):
        tmp = []
        tmp.append(random() * 10 - 5)
        tmp.append((-tmp[0]*weightTab[1]/weightTab[2])-weightTab[0]/weightTab[2])
        tab.append(tmp)
    return tab


def randWeight(n):
    tab = []
    for i in range(n):
        tmp = random() * 2 - 1
        if tmp == 0:
            tmp = random() * 2 - 1
        tab.append(tmp)
    return tab


def fun(fu):
    if fu > 0:
        return 1
    if fu <= 0:
        return 0


# eta = input("Podaj krok: ")
eta = 0.1

seed(44)
W = randWeight(3)
X = randVector(100, W)

plt.plot(X, 'o')
plt.show()
