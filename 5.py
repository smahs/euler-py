#!/usr/bin/python2

"""
Statement:

2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""


from unittest import TestCase, main
from operator import not_


class Problem5(object):

    least_factors = [11, 13, 14, 16, 17, 18, 19, 20]

    def check(self, n):
        return map(not_, map(bool, map(lambda i: n % i,
                                       self.least_factors)))

    def fn(self):
        n, found = (0, False)
        while not found:
            n += 20
            found = all(self.check(n))
        return n


class TestProblem5(TestCase):

    def setUp(self):
        self.answer = 232792560

    def test_main(self):
        self.assertEqual(Problem5().fn(), self.answer)


if __name__ == '__main__':
    main()
