import numpy as np


# def normal(x):
#     fac = abs(x).max()
#     x_n = x / x.max()
#     return fac, x_n

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps

    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    eigenvector = np.random.rand(len(data))
    eigenvalue = 0.
    ### YOUR CODE HERE
    for _ in range(num_steps):
        # error is too large with those methods:

        # eigenvector = np.matmul(data, eigenvector)
        # eigenvalue = max(abs(eigenvector))
        # eigenvector = eigenvector / eigenvalue

        # eigenvector = np.dot(data, eigenvector)
        # eigenvalue, eigenvector = normal(eigenvector)

        eigenvector = data @ eigenvector / np.linalg.norm(data @ eigenvector)
        eigenvalue = (eigenvector.T @ data @ eigenvector) / (eigenvector.T @ eigenvector)

    return float(eigenvalue), eigenvector
