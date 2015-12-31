#!/usr/bin/python2

"""
Statement:

The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence
to contain 1000 digits?
"""


from unittest import TestCase, main
from decimal import Decimal


class Problem25(object):

    def __init__(self, bound):
        self.bound = bound

    def fibn(self, n):
        n = Decimal(n)
        sqroot = Decimal(0.5)
        return int(((1 + (5**sqroot)) ** n - (1 - (5**sqroot)) ** n) /
                   ((2 ** n) * 5**sqroot))

    def fn(self):
        counter, length = 0, 0
        while length < self.bound:
            counter += 1
            length = len(str(self.fibn(counter)))
        return counter


class TestProblem25(TestCase):

    def setUp(self):
        self.bound = 1000
        self.answer = 4782

    def test_main(self):
        self.assertEqual(Problem25(self.bound).fn(), self.answer)


if __name__ == '__main__':
    main()
