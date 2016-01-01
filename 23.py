#!/usr/bin/python2

"""
Statement:

A perfect number is a number for which the sum of its proper
divisors is exactly equal to the number. For example, the sum
of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors
is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant
numbers is 24. By mathematical analysis, it can be shown that
all integers greater than 28123 can be written as the sum of two
abundant numbers. However, this upper limit cannot be reduced any
further by analysis even though it is known that the greatest number
that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written
as the sum of two abundant numbers.
"""


from unittest import TestCase, main
from utils import factors


class Problem23(object):

    def __init__(self, bound):
        self.bound = bound

    def factors_sum(self, num):
        return sum(factors(num)) - num

    def fn(self):
        abundant = [num for num in xrange(self.bound)
                    if self.factors_sum(num) > num]
        absum = set([i+j for i in abundant for j in abundant
                     if i+j <= self.bound])
        return sum(i for i in xrange(self.bound) if i not in absum)


class TestProblem23(TestCase):

    def setUp(self):
        self.bound = 28123
        self.answer = 4179871

    def test_main(self):
        self.assertEqual(Problem23(self.bound).fn(), self.answer)


if __name__ == '__main__':
    main()
