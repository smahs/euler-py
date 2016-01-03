#!/usr/bin/python2

"""
Statement:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

=================================================

Prelude:

This algorithm follows a reduction approach: Travelling from 1,
if a number is divisible by a factor, then the other factor
becomes the upper limit for finding the next factor.
This upper limit could be the largest prime, if it is prime.

Further, any factor divisible by 2 is not a prime factor.

Also, any composite number will have its largest prime factor
less than the sqaure root of that number. If it is prime,
the only factor larger than its square root is itself.
"""


from unittest import TestCase, main
from utils import prime_factors


class Problem3(object):

    def __init__(self, bound):
        self.bound = bound

    def fn(self):
        return max(prime_factors(self.bound).keys())


class TestProblem3(TestCase):

    def setUp(self):
        self.bound = 600851475143
        self.answer = 6857

    def test_main(self):
        self.assertEqual(Problem3(self.bound).fn(), self.answer)


if __name__ == '__main__':
    main()
