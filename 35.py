#!/usr/bin/python2


"""
Statement:
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from unittest import TestCase, main
from utils import prime_sieve


class Problem35(object):
    def __init__(self, limit):
        self._limit = limit

    def circular_num(self, prime):
        circular_nums = [prime]
        length = len(str(prime))
        mf = 1
        for i in xrange(length - 1):
            mf *= 10
        for i in xrange(length - 1):
            tmp = mf * (prime % 10)
            prime = tmp + prime / 10
            circular_nums.append(prime)
        return circular_nums

    def fn(self):
        count = 0
        primes = prime_sieve(self._limit)
        for i, v in enumerate(primes):
            if v:
                circular_nums = self.circular_num(i)
                if all(primes[p] for p in circular_nums):
                    count += 1
        return count


class TestProblem35(TestCase):
    def setUp(self):
        self.limit = 1000000
        self.answer = 55

    def test_fn(self):
        self.assertEqual(Problem35(self.limit).fn(), self.answer)


if __name__ == '__main__':
    main()
