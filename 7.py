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

Limit for search is given by prime number theorem.
A 20% margin is added for uncertainty.
"""


from unittest import TestCase, main
from math import log


class Problem7(object):

    def __init__(self, bound):
        self.bound = bound
        self.limit = int(1.2 * bound * log(bound))

    def fn(self):
        sieve = [True] * int(self.limit)
        sieve[0], sieve[1] = [None] *2
        counter = 0

        for i, v in enumerate(sieve):
            if not v:
                continue
            sieve[i**2::i] = ([False] *
                              ((self.limit - 1) / i - (i - 1)))
            counter += 1
            if counter == self.bound:
                return i


class TestProblem7(TestCase):

    def setUp(self):
        self.bound = 10001
        self.answer = 104743

    def test_main(self):
        self.assertEqual(Problem7(self.bound).fn(), self.answer)


if __name__ == '__main__':
    main()
