import numpy as np

wsp_x = 10 * np.random.sample(100) - 5
wsp_y = 10 * np.random.sample(100) - 5

file = open("rands.txt", "w+")

for i in range(100):
    if wsp_y[i] >= (2 * wsp_x[i] - 2):
        file.write(f"{wsp_x[i]} {wsp_y[i]} 1\n")
    else:
        file.write(f"{wsp_x[i]} {wsp_y[i]} 0\n")

file.close()
