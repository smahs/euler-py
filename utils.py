#!/usr/bin/python2


from math import sqrt


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
    sieve[0], sieve[1] = [None] * 2
    counter = 0
    for i, v in enumerate(sieve):
        if not v:
            continue
        sieve[i**2::i] = ([False] *
                            ((limit - 1) / i - (i - 1)))
        counter += 1
    # 1 is neither prime nor composite, 2 is prime
    sieve[0], sieve[1] = (True, False)
    return sieve


def multiples(number, factor):
    counter = 0
    while not number % factor:
        number = number / factor
        counter += 1
    return (number, counter)


def prime_factors(number):
    original = number
    factors, current = ({}, 3)
    if not number % 2:
        number, factors[2] = multiples(number, 2)
    max_factor = int(sqrt(number) + 1)
    while number > 1 and current <= max_factor:
        if not number % current:
            number, factors[current] = multiples(number, current)
        max_factor = int(sqrt(number)+ 1)
        current += 2
    if number is not 1:
        factors[number] = 1
    return factors


def factors(number):
    return set(factor for factors in ((i, number/i) for i in
                                        xrange(1, int(sqrt(number) + 1))
                                        if not number % i)
                for factor in factors)
