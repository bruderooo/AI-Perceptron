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
    return array(tab)


# This is activation function
def fun(u):
    if u > 0:
        return 1
    if u <= 0:
        return 0


# eta represents step
eta = 0.1

# Variable - you need it if u want make gif file
images = []

# Seed for rand
seed(1108)

# w represent weights. Weights are random numbers from -1 to 1. They are array with 3 position (0 is bias).
# randWeight return numpy array, in this example this array has size 3, something like this [ 1 2 3 ].
w = randWeight(3)

# x1 and x2 are random numbers from -5 to 5
x1, x2 = randVector(100)

plt.plot(x1, x2, 'o')

# This is the plot's range
plt.xlim(-5, 5)
plt.ylim(-5, 5)

# These are axis descriptions
plt.xlabel('x1')
plt.ylabel('x2')

plt.savefig('./basicPlot.png')

for i in range(len(x1)):
    linearFunction = array([])

    fu = fun(x2[i] * w[2] + x1[i] * w[1] + w[0])

    for j in range(len(x2)):
        linearFunction = append(linearFunction, (-w[1]*x1[j]/w[2]) - (w[0]/w[2]))

    plt.title("Correction No." + str(i))

    # This is the plot's range
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)

    # These are axis descriptions
    plt.xlabel('x1')
    plt.ylabel('x2')

    # This make plot
    plt.plot(x1, x2, 'o', x1, linearFunction)

    # This line save actual plot to file
    plt.savefig('./Plots/plot' + str(i+1) + '.png')

    # This line add plot to list, which is used to make gif file
    images.append(imageio.imread('./Plots/plot' + str(i+1) + '.png'))

    # This line shows plot
    plt.show()

    # In this place, the program correct slope of the linear function
    if fu > fun(linearFunction[0]):
        w = w + array([1, x1[i], x2[i]])*eta
    elif fu < fun(linearFunction[0]):
        w = w - array([1, x1[i], x2[i]])*eta
    else:
        pass

# Plots, which are in list 'images', are convert to gif
imageio.mimsave('./howPlotChangeOverTime.gif', images)
