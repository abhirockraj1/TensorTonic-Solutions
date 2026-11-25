import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    pf = math.comb(n, k) * (p**k) * ((1-p)**(n-k))
    c = 0
    for  i in range(0,k+1):
        c += (math.comb(n, i) )* (p**i) *((1-p)**(n-i))
    return {'pmf': float(pf) , 'cdf': float(c)}    