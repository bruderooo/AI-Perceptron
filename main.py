from numpy import array, append
from random import random, seed
import matplotlib.pyplot as plt
import imageio


def randVector(n):
    tab1, tab2 = [], []
    for i in range(n):
        tab1.append(random() * 10 - 5)
        tab2.append(random() * 10 - 5)
    return array(tab1), array(tab2)


def randWeight(n):
    tab = []
    for i in range(n):
        tmp = random() * 2 - 1
        if tmp == 0:
            tmp = random() * 2 - 1
        tab.append(tmp)
    return tab


def fun(u):
    if u > 0:
        return 1
    if u <= 0:
        return 0


# eta = input("Podaj krok: ")
eta = 0.1
images = []

seed(2137)
w = array(randWeight(3))
x1, x2 = randVector(100)

for i in range(len(x1)):
    linearFunction = array([])
    fu = fun(x2[i] * w[2] + x1[i] * w[1] + w[0])
    for j in range(len(x2)):
        linearFunction = append(linearFunction, (-w[1]*x1[j]/w[2]) - (w[0]/w[2]))

    plt.xlim(-5, 5)
    plt.ylim(-5, 5)

    plt.xlabel('x1')
    plt.ylabel('x2')

    plt.plot(x1, x2, 'o', x1, linearFunction)
    plt.savefig('./Plots/cos' + str(i) + '.png')
    images.append(imageio.imread('./Plots/cos' + str(i) + '.png'))
    plt.show()

    if fu > fun(linearFunction[0]):
        w = w + array([1, x1[i], x2[i]])*eta
    elif fu < fun(linearFunction[0]):
        w = w - array([1, x1[i], x2[i]])*eta
    else:
        pass

imageio.mimsave('./movie.gif', images)
