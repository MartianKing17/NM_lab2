import numpy as np
from math_lab import thomas_algorithm


def init_mat():
    size = int(input("Input matrix size: "))

    if size < 3:
        raise ArithmeticError

    mat = np.zeros((size, size))
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


def main():
    mat = 0
    f = 0

    try:
        mat, f = init_mat()
    except:
        print("The dimension of the matrix should be greater than fbo equal to 3")
        return 0

    x, res = thomas_algorithm(mat, f)
    print("X: " + str(x) + '\n' + "Det: " + str(res) + '\n')


main()