import random, miller_rabin, number_theory


def get_prime_pair(len_bits):

    p = miller_rabin.gen_prime(len_bits)
    q = miller_rabin.gen_prime_range(p+1, 2*p)

    return p, q

def gen_vulnerable_keys():
    len_bits = 1024
    assert len_bits%4 == 0

    p, q = get_prime_pair(len_bits//2)
    n = p*q
    phi = number_theory.eulers_totient(p, q)

    vuln_d = False
    i = 0
    while not vuln_d:
        if (i%1000000 == 0):
            print(i, "Finding Vulnerable D")
        i += 1
        d = random.getrandbits(len_bits//4)

        if (number_theory.gcd(d, phi) == 1 and 36*pow(d, 4) < n):
            vuln_d = True
    
    e = number_theory.modular_inverse(d, phi)
    return e, n, d
