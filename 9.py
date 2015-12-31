#!/usr/bin/python2

"""


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from unittest import TestCase, main


class Problem9(object):
    def __init__(self, bound):
        self._bound = bound

    def fn(self):
        for num1 in xrange(1, self._bound / 2 - 1, 1):
            for num2 in xrange(num1 + 1, self._bound / 2, 1):
                    num3 = self._bound - num1 - num2
                    if num1 * num1 + num2 * num2 == num3 * num3:
                        return num1 * num2 * num3


class TestProblem9(TestCase):
    def setUp(self):
        self.bound = 1000
        self.answer = 31875000

    def test_fn(self):
        self.assertEqual(Problem9(self.bound).fn(), self.answer)


if __name__ == '__main__':
    main()
