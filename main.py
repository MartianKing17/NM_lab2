import numpy as np
from computational_methods import thomas_algorithm
from computational_methods import Jacobi


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
            value = float(input(string))
            mat[i][j] = value

    for i in range(size):
        value = float(input("Input f[" + str(i) + "]: "))
        f.append(value)

    return mat, f


def main():
    mat = 0
    f = 0

    method = 1

    while True:
        method = int(input("Input method number(Thomas algorithm - 1, Jacobi - 2, exit - 3): "))

        if method == 1:

            try:
                mat, f = init_mat()
            except ArithmeticError:
                print("The dimension of the matrix should be greater than fbo equal to 3")
                break

            x, res = thomas_algorithm(mat, f)
            print("X: " + str(x) + '\n' + "Det: " + str(res) + '\n')

        elif method == 2:

            try:
                mat, f = init_mat()
            except ArithmeticError:
                print("The dimension of the matrix should be greater than fbo equal to 3")
                break

            x = [0, 0, 0]
            ell = float(input("Enter ellipsis: "))
            x, res = Jacobi(mat, f, x, ell)
            print("X: " + str(x) + '\n' + "Num: " + str(res) + '\n')

        elif method == 3:
            break
        else:
            continue


main()
