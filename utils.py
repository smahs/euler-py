#!/usr/bin/python2


class Utilities(object):

    """
    Reusable utility functions
    """

    @classmethod
    def check_prime(cls, num):
        if not num % 2:
            return False
        for i in xrange(3, int(num**0.5) + 1, 2):
            if not num % i:
                return False
        return True

    @classmethod
    def reverse(cls, num):
        rev_num = 0
        while num:
            rev_num = 10 * rev_num + num % 10
            num /= 10
        return rev_num

    @classmethod
    def reverse_s(string):
        try:
            if not isinstance(string, str):
                string = str(string)
            return string[::-1]
        except:
            return None

    @classmethod
    def check_palindrome(cls, num):
        if num == Utilities.reverse(num):
            return True
        return False

    @classmethod
    def prime_sieve(cls, limit):
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
