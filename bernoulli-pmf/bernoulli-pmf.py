import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    pmf= []
    for i in x:
        if i:
            pmf.append(p)
        else:
            pmf.append( 1-p)

    return  {"pmf": np.array(pmf), "mean": p*1.0, "variance": (p*(1-p))*1.0 }