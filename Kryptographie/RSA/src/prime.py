import random

from euclid import gcd
from euclid import extgcd


def select_a_list(n):
    if n < 2047:
        return [2]
    elif n < 1373653:
        return [2, 3]
    elif n < 9080191:
        return [31, 73]
    elif n < 25326001:
        return [2, 3, 5]
    elif n < 3215031751:
        return [2, 3, 7]
    else:
        return [i for i in range(2, n - 1)]


def square_and_multiply(base, exp, mod):
    '''Square and Multiply Algorithm'''
    if exp == 0:
        x = 1
    else:
        half = square_and_multiply(base, exp // 2, mod)
        x = half * half
        if exp % 2 == 1:
            x *= base
    return x % mod


def rabin_miller_test(n):
    '''Rabin Miller Test to check primality'''
    a_list = select_a_list(n)
    for a in a_list:
        s = 0
        d = n - 1
        while d % 2 == 0:
            s = s + 1
            d = d >> 1
        x = square_and_multiply(a, d, n)
        if x != 1 and x + 1 != n:
            for r in range(1, s):
                x = square_and_multiply(x, 2, n)
                if x == 1:
                    return False
                elif x == n - 1:
                    a = 0
                    break
            if a:
                return False
    return True


def is_prime(num):
    '''Function to test if a number is prime'''
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 3 == 0:
        return False
    return rabin_miller_test(num)


def generate_primes(lb, ub):
    '''Function to generate random primes'''
    found = False
    if lb % 2 == 0:
        lb += 1
    while not found:
        # Generate just odd random numbers
        p = random.randrange(lb, ub, 2)
        q = random.randrange(lb, ub, 2)
        # Check if random numbers are prime
        if is_prime(p) and is_prime(q) and p != q:
            found = True

    return p, q


def compute_params(phi_n):
    '''Function to compute e and d'''
    d = 0
    e = 0
    found_e = False

    while found_e == False:
        e = random.randint(1, phi_n - 1)
        if gcd(e, phi_n) == 1:
            found_e = True
    _, d, _ = extgcd(e, phi_n)
    if(d < 0):
        d += phi_n
    return d, e


def generate_params(seed=42, lb=3, ub=100, DEBUG=True):
    '''Main function to generate primes and params'''
    p, q = generate_primes(lb, ub)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    d, e = compute_params(phi_n)
    if DEBUG:
        print("P, Q: ", p, q)
        print("N: ", n)
        print("Phi(n): ", phi_n)
        print("E, D: ", e, d)
    return n, d, e
