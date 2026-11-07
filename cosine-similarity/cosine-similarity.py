import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    s ,ssa, ssb= 0.0, 0, 0
    for i ,j in zip(a,b):
        s += i*j
        ssa += i**2
        ssb += j**2
        
    if( ssa == 0 or ssb ==0):
        return 0.0
    return s/((ssa**0.5 ) *(ssb**0.5))