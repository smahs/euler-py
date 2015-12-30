#!/usr/bin/python2

"""
Statement:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

=================================================

Prelude:

This problem is solved with an implementation of
Sieve of Eratosthenes.
"""


from unittest import TestCase, main
from utils import Utilities


class Problem10(object):

    def __init__(self, bound):
        self.bound = bound

    def fn(self):
        sieve = Utilities.prime_sieve(self.bound)
        sieve = [i for i, v in enumerate(sieve) if v]
        return sum(sieve)


class TestProblem10(TestCase):

    def setUp(self):
        self.bound = 2000000
        self.answer = 142913828922

    def test_main(self):
        self.assertEqual(Problem10(self.bound).fn(), self.answer)


if __name__ == '__main__':
    main()
