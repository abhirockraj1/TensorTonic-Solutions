import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    r,c = (len(A)), len(A[0])
    a = np.empty((c, r))

    for i in range(r):
        for j in range(c):
            a[j][i] = A[i][j]
            
    return a        
