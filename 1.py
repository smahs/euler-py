#!/usr/bin/python2

"""
Statement:

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from unittest import TestCase, main


class Problem1(object):

    def __init__(self, bound):
        self.bound = bound

    def fn(self):
        n = self.bound
        return sum(set(range(3,n,3) + range(5,n,5)))

    def alt(self):
        bound = self.bound - 1  # LESS than 1000
        sum3 = (bound / 3) * (3 + ((bound / 3) * 3)) / 2
        sum5 = (bound / 5) * (5 + ((bound / 5) * 5)) / 2
        sum15 = (bound / 15) * (15 + ((bound / 15) * 15)) / 2
        return sum3 + sum5 - sum15


class TestProblem1(TestCase):

    def setUp(self):
        self.bound = 1000
        self.answer = 233168

    def test_main(self):
        self.assertEqual(Problem1(self.bound).fn(), self.answer)

    def test_alt(self):
        self.assertEqual(Problem1(self.bound).alt(), self.answer)


if __name__ == '__main__':
    main()
