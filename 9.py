#!/usr/bin/python2

"""
Statement:

A Pythagorean triplet is a set of three natural numbers,
a < b < c, for which, a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which
a + b + c = 1000.

Find the product abc.
"""

from unittest import TestCase, main


class Problem9(object):
    def __init__(self, bound):
        self.bound = bound

    def fn(self):
        limit = self.bound / 2 - 1
        for i in xrange(1, limit):
            for j in xrange(i+1, limit):
                    k = self.bound - i - j
                    if i*i + j*j == k*k:
                        return i*j*k


class TestProblem9(TestCase):
    def setUp(self):
        self.bound = 1000
        self.answer = 31875000

    def test_fn(self):
        self.assertEqual(Problem9(self.bound).fn(), self.answer)


if __name__ == '__main__':
    main()
