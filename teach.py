import numpy as np
import matplotlib.pyplot as plt

nG = 0


def draw(fx_draw1, fy_draw1, fx_draw2, fy_draw2, fw):
    global nG
    if nG == 0:
        frys = [2 * -5 - 2, 2 * 5 - 2]
    else:
        frys = [(-fw[1] * (-5) / fw[2]) - (fw[0] / fw[2]), (-fw[1] * 5 / fw[2]) - (fw[0] / fw[2])]

    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.plot(fx_draw1, fy_draw1, 'g^', fx_draw2, fy_draw2, 'ro', [-5, 5], frys)
    plt.savefig(f'./plots/{nG}.png')
    plt.show()
    nG += 1


def file_to_array(name):
    xf, yf, fclass = [], [], []
    file = open(name, "r")
    lines = file.readlines()
    for line in range(len(lines)):
        lines[line] = lines[line].split()
        xf.append(float(lines[line][0]))
        yf.append(float(lines[line][1]))
        fclass.append(float(lines[line][2]))
    return np.array(xf), np.array(yf), np.array(fclass)


def for_plot(name):
    xf_draw1, xf_draw2, yf_draw1, yf_draw2 = [], [], [], []
    file = open(name, "r")
    lines = file.readlines()
    for line in range(100):
        lines[line] = lines[line].split()
        if lines[line][2] == "0":
            xf_draw1.append(float(lines[line][0]))
            yf_draw1.append(float(lines[line][1]))
        else:
            xf_draw2.append(float(lines[line][0]))
            yf_draw2.append(float(lines[line][1]))
    file.close()
    return np.array(xf_draw1), np.array(xf_draw2), np.array(yf_draw1), np.array(yf_draw2)


def fun(u):
    if u >= 0:
        return 1
    else:
        return 0


file_name = "rands.txt"
x_train, y_train, klasa = file_to_array(file_name)
x_draw1, x_draw2, y_draw1, y_draw2 = for_plot(file_name)
w = 2 * np.random.sample(3) - 1

draw(x_draw1, y_draw1, x_draw2, y_draw2, w)
draw(x_draw1, y_draw1, x_draw2, y_draw2, w)

eta = 1

for epoch in range(5):
    for element in range(100):
        u = x_train[element] * w[1] + y_train[element] * w[2] + w[0]

        if fun(u) == 0 and klasa[element] == 1:
            w[0] += eta
            w[1] += eta * x_train[element]
            w[2] += eta * y_train[element]
        elif fun(u) == 1 and klasa[element] == 0:
            w[0] -= eta
            w[1] -= eta * x_train[element]
            w[2] -= eta * y_train[element]
        else:
            pass
    if epoch == 1:
        draw(x_draw1, y_draw1, x_draw2, y_draw2, w)

draw(x_draw1, y_draw1, x_draw2, y_draw2, w)
