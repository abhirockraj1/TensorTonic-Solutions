import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code hered
    s =0.0
    for i,j in zip(x,y):
        s += i*j
    return s