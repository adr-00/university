# Métodos iterativos de Jacobi y Gaus-Seidel

import numpy as np

def jacobi(A, b, tolerance=1e-10, max_iter=1000):
    x = np.zeros_like(b, dtype=np.double)
    T = A - np.diag(np.diagonal(A))
    for k in range(max_iter):
        x_old = x.copy()
        x[:] = (b - (np.dot(T, x)) / np.diagonal(A))
        num_error = np.linalg.norm(x - x_old, ord=np.inf)
        den_error = np.linalg.norm(x, ord=np.inf)
        error = num_error / den_error
        if error < tolerance:
            break
    return x



def gauss_seidell(A, b, tolerance=1e-10, max_iter=1000):
    x = np.zeros_like(b, dtype=np.double)
    for k in range(max_iter):
        x_old = x.copy()
        for i in range(A.shape[0]):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]))-np.dot(A[i, (i+1):], x_old[(i+1):]) / A[i, i]
        num_error = np.linalg.norm(x - x_old, ord=np.inf)
        den_error = np.linalg.norm(x, ord=np.inf)
        error = num_error / den_error
        if error < tolerance:
            break
    return x
    
