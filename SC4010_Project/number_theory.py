# File containing all the arithmetic necessary for calculating RSA values

def gcd(a, b):

    if(b>a):
        temp = b
        a = b
        b = temp

    while b:
        a, b = b, a%b
    return a

def extended_euclid_gcd(a, b):
    a, b = (b, a) if a<b else a, b
    
    u, u1, = 1, 0
    v, v1 = 0, 1

    while b:
        q = a //b
        u, u1 = u1, u - q * u1
        v, v1 = v1, v - q * v1
        a, b = b, a - q * b
    return u, v, a

def modular_inverse(e, n):

    return extended_euclid_gcd(e, n)[0]%n

def eulers_totient(p, q):
    totient = (p-1)*(q-1)
    return totient
def bitlength(x):

    assert x >= 0
    n = 0

    while x> 0:
        n = n+1
        x = x >>1
    return n


def is_sqrt(n):

    if n<0:
        raise ValueError('Square root is not defined for neagtive numbers')
    
    if n == 0:
        return 0
    
    a, b = divmod(bitlength(n), 2)
    x = 2 ** (a+b)

    while True:
        y = (x+n//x)//2

        if y >= x:
            return x
        x = y

def is_perf_sq(n):

    h = n & 0xF

    if h > 9:
        return -1
    
    if (h!=2 and h!=3 and h!=5 and h!=6 and h!=7 and h!=8):
        t = is_sqrt(n)
        if t*t == n:
            return t
        else:
            return -1
    
    return -1
