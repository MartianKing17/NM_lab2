import numpy as np


def sort_diagonal(mat, k = 0, n = 0, p = 0):
    res = []
    value = len(mat[0])

    for i in range(0, value - p):
        res.append(mat[i+k][i+n])

    return res


def reinversion_vector_x(x):
    x_new = []
    val = -1
    for i in range(len(x) + val, val, val):
        x_new.append(x[i])

    return x_new


def prepare_lam_beta_z_and_x_n(c_dia, a_dia, b_dia, f):
    size = len(c_dia)

    # lambda1 = - (b1/c1)
    # beta1 = (f1/c1)
    # z_i = c_i + lambda_i-1 * a_i
    # lambda_k = -(b_k / z_k)
    # beta_k = (f_k - beta_k-1 * a_k)/z_k, k = 1,n-1
    # x_n = beta_n

    z = []
    lam = []
    beta = []
    lam.append(- b_dia[0] / c_dia[0])
    beta.append(float(float(f[0]) / c_dia[0]))

    for i in range(1, size-1):
        z.append(c_dia[i] + lam[i - 1] * a_dia[i-1])
        lam.append(-b_dia[i] / z[i-1])
        value = float(f[i]) - beta[i - 1] * a_dia[i-1]
        beta.append(value / z[i-1])

    z.append(c_dia[size - 1] + lam[size - 2] * a_dia[size - 2])
    x = float(f[size - 1]) - (beta[size - 2] * a_dia[size - 2])
    x /= z[size - 2]
    return lam, beta, z, x


def enter_x_arr(lam, beta, x, size):

    len = size - 2
    val = -1

    # x_i = beta_i + lambda_i * x_i+1

    for i in range(len, val, val):
        value = beta[i] + lam[i] * x[abs(i - len)]
        x.append(value)

    return x


def det_mat(c, z):
    res = c

    #det = c1 * z2 * .... * zn

    for i in range(0, len(z)):
        res *= z[i]

    return res


def thomas_algorithm(mat, f):
    c_dia = sort_diagonal(mat)
    a_dia = sort_diagonal(mat, n = 1, p = 1)
    b_dia = sort_diagonal(mat, k = 1, p = 1)
    size = len(mat[0])
    x = []
    lam, beta, z, value = prepare_lam_beta_z_and_x_n(c_dia, a_dia, b_dia, f)
    x.append(value)
    x = enter_x_arr(lam, beta, x, size)
    x = reinversion_vector_x(x)
    res = det_mat(c_dia[0], z)
    return x, res


def yacobi(mat):
    return 0







