import numpy as np


def sort_and_checking_c_dia(mat):
    c_dia = []
    value = len(mat[0])

    for i in range(0, value):
        c_dia.append(mat[i][i])

    for i in range(0, len(c_dia)):

        if i == 0:
            value = c_dia[i]
            continue

        if value == c_dia[i]:
            continue
        else:
            raise ValueError

    return c_dia


def sort_and_checking_a_dia(mat):
    a_dia = []
    value = len(mat[0])

    for i in range(value-1):
        a_dia.append(mat[i][i+1])

    for i in range(0, len(a_dia)):

        if i == 0:
            value = a_dia[i]
            continue

        if value == a_dia[i]:
            continue
        else:
            raise ValueError

    return a_dia


def sort_and_checking_b_dia(mat):
    b_dia = []
    value = len(mat[0])

    for i in range(value - 1):
        b_dia.append(mat[i+1][i])

    for i in range(0, len(b_dia)):

        if i == 0:
            value = b_dia[i]
            continue

        if value == b_dia[i]:
            continue
        else:
            raise ValueError

    return b_dia


def resort_vector_x(x):
    x_new = []

    for i in range(len(x)-1,0):
        x_new.append(x[i])

    return x_new


def prepare_lam_beta_z_and_x_n(c_dia, a_dia, b_dia, f):
    size = len(c_dia)

    z = []
    lam = []
    beta = []
    lam.append(- b_dia[0] / c_dia[0])
    beta.append(f[0] / c_dia[0])

    for i in range(1, size-1):
        z.append(c_dia[i] + lam[i - 1] * a_dia[i])
        lam.append(-b_dia[i] / z[i])
        value = f[i] - b_dia[i - 1] * a_dia[i]
        beta.append(value / z[i])

    z.append(c_dia[size - 1] + lam[size - 2] * a_dia[size - 1])
    value = f[size - 1] - b_dia[size - 2] * a_dia[size - 1]
    value /= z[size - 1]
    return lam, beta, z, value


def enter_x_arr(lam, beta, x, size):
    j = size - 1
    for i in range(size-1, 0):
        value = beta[i] - lam[i] * x[abs(i - size)]
        x.append(value)

    return x


def det_mat(c, z):
    res = c

    for i in range(1, len(z)):
        res *= z[i]

    return res


def progon(mat, f):
    try:
        c_dia = sort_and_checking_c_dia(mat)
        a_dia = sort_and_checking_a_dia(mat)
        b_dia = sort_and_checking_b_dia(mat)
    except:
        print("Some problem with matrix")

    value = 0
    size = len(mat[0])
    x = []
    lam, beta, z, value = prepare_lam_beta_z_and_x_n(c_dia, a_dia, b_dia, f)
    x.append(value)
    x = enter_x_arr(lam, beta, x, size)
    x = resort_vector_x(x)
    res = det_mat(c_dia[0], z)
    return x, res


def yacobi(mat):
    return 0







