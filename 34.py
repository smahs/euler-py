#!/usr/bin/python2

"""
Statement:

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the
factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

===============================================

Prelude:

The upper bound is the first ten digit number.
However, 9! * 10 is 3628800 which is a seven digit number.
Hence a more sensible upper bound would be 9! * 7.
"""

from unittest import TestCase, main
from math import factorial


class Problem34(object):

    def __init__(self, bound):
        self.bound = bound
        self.factorials = {i: factorial(i) for i in range(10)}

    def sum_factorial(self, n):
        total = 0
        num = n
        while num > 0:
            i = num % 10
            num /= 10
            total += self.factorials[i]
            if total > n:
                return 0
        return n if n == total else 0

    def fn(self):
        return sum(map(self.sum_factorial, xrange(*self.bound)))


class TestProblem34(TestCase):

    def setUp(self):
        self.bound = (3, factorial(9) * 7)
        self.answer = 40730

    def test_main(self):
        self.assertEqual(Problem34(self.bound).fn(), self.answer)


if __name__ == '__main__':
    main()
