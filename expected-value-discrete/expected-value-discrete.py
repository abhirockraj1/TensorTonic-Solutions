import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    e = 0
    for i , j in zip(x, p):
        e += i*j
    return e * 1.0