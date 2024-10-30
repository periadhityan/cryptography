import random
import math


def is_prime(number):
    if number<2:
        return False
    for i in range(2, number//2+1):
        if number % i == 0:
            return False
    return True

def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)

    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    
    return prime

def mod_inverse(e, phi):
    for d in range(3, phi):
        print("Testing D value = ", d)
        if (d*e) % phi == 1:
            return d
    return ValueError("mod_inverse does not exist")

def RSA():

    #Pick 2 prime numbers
    p, q = generate_prime(1000, 5000), generate_prime(1000, 5000)

    while p==q:
        q = generate_prime(1000, 5000)

    #Calculating the modulus n
    n = p*q

    #Euler's Totient of n
    phi_n = (p-1) * (q-1)

    #Calculating public exponent e
    e = random.randint(3, phi_n-1)

    #e and phi_n (Euler's totient of n) must have the greatest common divisor as 1
    while math.gcd(e, phi_n) != 1:
        e = random.randint(3, phi_n-1)

    #Calculate the mod inverse
    #mod inverse is the value such that ((d*e) mod phi_n) == 1
    good_d = False

    while not good_d:
        d = mod_inverse(e, phi_n)
        if(36*pow(d, 4) < n):
            good_d = True


    return e, n, d
