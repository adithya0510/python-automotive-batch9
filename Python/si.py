def add(a,b):
    return a + b 

def sub(a,b):
    return a - b 

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

#simple interest calculation
def simple_interest(P, R, T):
    pr = mul(P, R)
    prt = mul(pr, T)
    si = div(prt, 100)
    return si