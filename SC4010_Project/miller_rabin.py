import random, sys

def miller_rabin_pass(a, s, d, n):
    """
    n is an odd number with 
    n-1 = (2^s)*d,
    d is odd,
    a is the base: 1 < a < n-1
    
    returns True iff n passes Miller Rabin test for a
    """

    a_to_power = pow(a, d, n)
    i = 0
    #InvariantL a_to_power = a^(d*2^i)modn
    
    #Test whether (a^d) = 1 modn

    if a_to_power == 1:
        return True
    
    #Test whether a^(d*2^i) = n-1 mod n
    #for 0<=i<=s-1

    while(i<s-1):
        if a_to_power == n - 1:
            return True
        
        a_to_power = (a_to_power*a_to_power) % n
        i += 1

    #if i = s-1, test failed

    return a_to_power == n-1

def miller_rabin(n):
    """
    Applies Miller Rabin test to n

    returns True iff n passes Miller Rabin test for K random bases
    """
    print("Testing number", n)

    #Compute s and d such that n-1 = (2^s)*d, d is odd

    d = n-1
    s = 0

    while d%2 == 0:
        d >>= 1
        s += 1

    #Applies test K times
    #Probablility of a false positive is less than (1/4)^K

    k = 20

    i = 1

    while(i<=k):
        a = random.randrange(2, n-1)
        if not miller_rabin_pass(a, s, d, n):
            return False
        i += 1
    return True

def gen_prime(len):
    """
    Generates prime of length len bits using Rabin Miller test
    """

    while True:
        p = random.getrandbits(len)
        p |= 2**len | 1
        
        if miller_rabin(p):
            return p

def gen_prime_range(start, stop):
    """
    Generate prime within given range using Rabin Miller test
    """

    while True:
        p = random.randrange(start, stop-1)
        p |= 1

        if miller_rabin(p):
            return p 