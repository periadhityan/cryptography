from sage.all import *

def strong_rsa():
    p = random_prime(2**1024, False, 2**1023)
    q = random_prime(2**1024, False, 2**1023)

    n = p*q
    phi = (p - Integer(1)) * (q - Integer(1))

    e = ZZ.random_element(phi)

    while(gcd(e, phi) != Integer(1)):
        e = ZZ.random_element(phi)

    bezout = xgcd(e, phi)

    d = Integer(mod(bezout[Integer(1)], phi))

    print("n = ", n)
    print()
    print("e = ", e)
    print()
    print("d = ", d)
    print()

    return n, e, d

def vulnerable_rsa():
    e = random_prime(2**16-1, False, 2**15)
    first_loop = True
    while first_loop or gcd(e, phi) != 1 or n.nbits() != 2048:
        first_loop = False
        # Note: Product of two 1024-bit primes not always 2048 bit
        # As this is just a proof of concept, we just reject if n < 2048 bits.
        p = random_prime(2**1024-1, False, 2**1023)
        q = random_prime(2**1024-1, False, 2**1023)
        n = p * q
        phi = (p - 1) * (q - 1)
    bezout = xgcd(e, phi)
    d = Integer(mod(bezout[1], phi))
    assert mod(d * e, phi) == 1
    # swap the public and private exponent
    e, d = d, e

    print("n = ", n)
    print()
    print("e = ", e)
    print()
    print("d = ", d)
    print()
    
    return n, e, d