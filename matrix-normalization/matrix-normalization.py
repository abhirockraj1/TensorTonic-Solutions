import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    x = np.array(matrix)
    eps: float = 1e-12
    if norm_type == "l1":
        denom = np.abs(x).sum(axis=axis, keepdims=True)
    elif norm_type == "l2":
        denom = np.linalg.norm(x, axis=axis, keepdims=True)
    elif norm_type == "max":
        denom = np.abs(x).max(axis=axis, keepdims=True)
    else:
        raise ValueError(f"Unsupported norm_type: {norm_type!r}. Use 'l1', 'l2', or 'max'.")
    print(denom)
    return x / np.maximum(denom, eps)