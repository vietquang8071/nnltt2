
def sinTaylor(x):
    e = 1e-15
    term = x
    n = 0
    total = 0
    while abs(term) > e:
        total += term
        n+=1
        term *= - (x * x) / ((2 * n) *(2 * n + 1))    
    return total


def cosTaylor(x):
    e = 1e-15
    term = 1
    n = 0
    total = 0
    while abs(term) > e:
        total += term
        n+=1
        term *= - (x * x) / ((2 * n - 1) *(2 * n))    
    return total