#!/usr/bin/python2


from math import sqrt
from decimal import Decimal


def check_prime(num):
    if not num % 2:
        return False
    for i in xrange(3, int(sqrt(num) + 1), 2):
        if not num % i:
            return False
    return True


def reverse(num):
    rev_num = 0
    while num:
        rev_num = 10 * rev_num + num % 10
        num /= 10
    return rev_num


def reverse_s(s):
    try:
        if not isinstance(s, str):
            s = str(s)
        return s[::-1]
    except:
        return None


def check_palindrome(num):
    return (True if num == int(reverse_s(num))
            else False)


def prime_sieve(limit):
    sieve = [True] * int(limit)
    sieve[0], sieve[1] = [False] * 2
    for i, v in enumerate(sieve):
        if v:
            sieve[i**2::i] = ([False] * (((limit - 1) / i) - (i - 1)))
    return sieve


def multiples(number, factor):
    counter = 0
    while not number % factor:
        number = number / factor
        counter += 1
    return (number, counter)


def prime_factors(number, limit=None):
    original = number
    factors, current = ({}, 3)
    if not number % 2:
        number, factors[2] = multiples(number, 2)
    if limit and factor_length(factors.values()) >= limit:
        return factors
    max_factor = int(sqrt(number)) + 1
    while number > 1 and current <= max_factor:
        if not number % current:
            number, factors[current] = multiples(number, current)
        if limit and factor_length(factors.values()) >= limit:
            break
        max_factor = int(sqrt(number)) + 1
        current += 2
    if number != 1 and number != original:
        factors[number] = 1
    return factors


def factors(number):
    return set(factor for factors in ((i, number/i) for i in
                                      xrange(1, int(sqrt(number) + 1))
                                      if not number % i)
               for factor in factors)


def fibn(n):
    n = Decimal(n)
    root5 = Decimal(sqrt(5))
    return int(((1 + root5) ** n - (1 - root5) ** n) /
               ((2 ** n) * root5))
