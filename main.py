import numpy as np
from math_lab import progon


def init_mat():
    size = int(input("Input matrix size: "))
    mat = np.mat(size)
    value = 0
    f = []

    for i in range(size):
        for j in range(size):
            string = "Input matrix elem[" + str(i) + "][" + str(j) + "]: "
            value = input(string)
            mat[i][j] = value

    for i in range(size):
        value = input("Input f[" + str(i) + "]: ")
        f.append(value)

    return mat, f


mat, f = init_mat()
x, res = progon(mat, f)

print("X: " + str(x) + '\n' + "Det: " + str(res) + '\n')