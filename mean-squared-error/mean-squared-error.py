import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """
    s = 0.0
    for i, j in zip(y_pred, y_true):
        s += (i-j)**2
    return s/len(y_pred)    