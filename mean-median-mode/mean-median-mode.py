from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    
    m = sum(x)/len(x)
    z = sorted(x)
    if (len(x)%2 ==0):
        mi = (z[len(z)//2] + z[(len(z)//2) -1])/2
    else:
        mi = z[len(z)//2]
    d = {}
    for i in x:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1
    b =0
    
    for k,v in d.items():
        if b<d[k]:
            b = d[k]
            mo = k
    return {'mean': m*1.0, 'median': mi*1.0, 'mode' : mo*1.0}        