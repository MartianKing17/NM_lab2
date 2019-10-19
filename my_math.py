

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
    beta.append(f[0] / c_dia[0])

    for i in range(1, size-1):
        z.append(c_dia[i] + lam[i - 1] * a_dia[i-1])
        lam.append(-b_dia[i] / z[i-1])
        value = f[i] - beta[i - 1] * a_dia[i-1]
        beta.append(value / z[i-1])

    z.append(c_dia[size - 1] + lam[size - 2] * a_dia[size - 2])
    x = f[size - 1] - (beta[size - 2] * a_dia[size - 2])
    x /= z[size - 2]
    return lam, beta, z, x


def sort_diagonal(mat, k = 0, n = 0, p = 0):
    res = []
    value = len(mat[0])

    for i in range(0, value - p):
        res.append(mat[i+k][i+n])

    return res


def maximum_vector_element(x):
    maximum = 0

    for i in range(len(x)):
        if x[i] > maximum:
            maximum = x[i]

    return maximum


def vector_module(x1, x0):
    x = []

    for i in range(len(x0)):
        x.append(abs(x1[i] - x0[i]))

    return maximum_vector_element(x)


def reinversion_vector_x(x):
    x_new = []
    val = -1
    for i in range(len(x) + val, val, val):
        x_new.append(x[i])

    return x_new