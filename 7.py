#!/usr/bin/python2

"""
Statement:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?

=================================================

Prelude:

This problem is solved with an implementation of
Sieve of Eratosthenes.

Limit for search is given by the prime number theorem.
A 20% margin is added for uncertainty.
"""


from unittest import TestCase, main
from math import log
from utils import prime_sieve


class Problem7(object):

    def __init__(self, bound):
        self.bound = bound
        self.limit = int(1.2 * bound * log(bound))

    def fn(self):
        sieve = prime_sieve(self.limit)
        sieve = [i for i, v in enumerate(sieve) if v]
        return sieve[self.bound]


class TestProblem7(TestCase):

    def setUp(self):
        self.bound = 10000  # python indices are zero based
        self.answer = 104743

    def test_main(self):
        self.assertEqual(Problem7(self.bound).fn(), self.answer)


if __name__ == '__main__':
    main()
