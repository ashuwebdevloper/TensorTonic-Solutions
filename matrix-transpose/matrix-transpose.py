import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Option 1: Use the .T attribute (most common)
    return np.array(A).T

    # Option 2: Use the np.transpose() function
    return np.transpose(A)