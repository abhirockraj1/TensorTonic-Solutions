import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    arr = np.asarray(matrix, dtype=float)
    if arr.ndim != 2 or arr.shape[0] != arr.shape[1]:
        raise ValueError("matrix must be a non-empty square 2D array.")

    # Use np.linalg.eigvals for general square matrices
    eigenvalues = np.linalg.eigvals(arr)

    # Extract real parts and sort in ascending order
    real_eigenvalues = np.real(eigenvalues)
    return np.sort(real_eigenvalues)