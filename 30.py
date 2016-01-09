#!/usr/bin/python2

"""
Statement:

Surprisingly there are only three numbers that can be written
as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as
the sum of fifth powers of their digits.
"""

from unittest import TestCase, main


class Problem30(object):

    def __init__(self, bound):
        self.bound = bound

    def power_sum(self, number, power):
        temp, total = number, 0
        while temp:
            digit = temp % 10
            total += digit ** power
            if total > number:
                return False
            temp /= 10
        return True if total == number else False

    def fn(self):
        return sum(i for i in xrange(*self.bound) if self.power_sum(i, 5))

    def alt(self):
        """ This solution is about 4x slower than above. """
        return sum(i for i in xrange(*self.bound)
                   if sum(map(lambda i: i**5, map(int, str(i)))) == i)


class TestProblem30(TestCase):

    def setUp(self):
        self.bound = (2, 6 * 9 ** 5)  # max sum of digit ** 5
        self.answer = 443839

    def test_main(self):
        self.assertEqual(Problem30(self.bound).fn(), self.answer)

    def test_alt(self):
        self.assertEqual(Problem30(self.bound).alt(), self.answer)


if __name__ == '__main__':
    main()
