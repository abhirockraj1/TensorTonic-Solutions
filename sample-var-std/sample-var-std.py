import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    m = sum(x)/len(x)
    s = 0
    for i in x:
        s += (i-m)**2
    v = s/(len(x)-1)
    return {"variance": v, "standard_deviation": v **0.5}