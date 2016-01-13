#!/usr/bin/python2

"""
Statement:

The decimal number, 585 = 10010010012 (binary),
is palindromic in both bases.

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base,
may not include leading zeros.)

"""

from unittest import TestCase, main


class Problem36(object):

    def __init__(self, bound):
        self.bound = bound

    def palindrome(self, n):
        return True if n == n[::-1] else False

    def fn(self):
        b10 = xrange(*self.bound)
        b2 = map(self.palindrome, [i[2:] for i in map(bin, b10)])
        b10 = map(self.palindrome, map(str, b10))
        return sum(i for i, v in enumerate(b10) if v and b2[i])


class TestProblem36(TestCase):

    def setUp(self):
        self.bound = (0, 1000001)
        self.answer = 872187

    def test_main(self):
        self.assertEqual(Problem36(self.bound).fn(), self.answer)


if __name__ == '__main__':
    main()
