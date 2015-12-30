#!/usr/bin/python2


"""
Statement:

A palindromic number reads the same both ways.
The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the
product of two 3-digit numbers.
"""


from unittest import TestCase, main
from utils import Utilities


class Problem4(object):
    def run(self):
        known = 0
        for first in xrange(999, 99, -1):
            if not first % 11:
                second, decrement = (999, 1)
            else:
                second, decrement = (990, 11)
            while second >= first:
                product = first * second
                if product < known:
                    break
                if Utilities.check_palindrome(product):
                    known = product
                second -= decrement
        return known


class Testproblem4(TestCase):
    def setUp(self):
        self.answer = 906609

    def test_run(self):
        self.assertEqual(Problem4().run(), self.answer)


if __name__ == '__main__':
    main()
