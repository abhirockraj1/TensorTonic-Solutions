import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    
    p = math.exp(-lam)*(lam **k)/math.factorial(k)
    c = 0
    for i in range(0,k+1):
        c += math.exp(-lam)*(lam **i)/math.factorial(i)
    return {'pmf': float(p),'cdf': float(c)}    
        