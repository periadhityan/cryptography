from sage.all import *

def sage_rsa():
    p = (Integer(2)**Integer(1024) - Integer(1))
    q = (Integer(2)**Integer(1024) - Integer(1))

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

def sage_vuln_rsa():
    p = (Integer(2)**Integer(1024) - Integer(1))
    q = (Integer(2)**Integer(1024) - Integer(1))

    n = p*q
    phi = (p - Integer(1)) * (q - Integer(1))

    e = ZZ.random_element(phi)

    while(gcd(e, phi) != Integer(1)):
        e = ZZ.random_element(phi)

    bezout = xgcd(e, phi)

    d = Integer(mod(bezout[Integer(1)], phi))

    while ((d**4)*3) > n:
        d = Integer(mod(bezout[Integer(1)], phi))

    print("n = ", n)
    print("e = ", e)
    print("d = ", d)

    return n, e, d