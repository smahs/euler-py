#!/usr/bin/python2

"""
Statement:

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is
3025 - 385 = 2640.

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.
"""


from unittest import TestCase, main


class Problem6(object):

    def __init__(self, bound):
        self.bound = bound

    def fn(self):
        n = self.bound + 1
        return (map(lambda i: i*i, [sum(range(1, n))])[0]
                - sum(map(lambda i: i*i, range(1, n))))

class TestProblem6(TestCase):

    def setUp(self):
        self.bound = 100
        self.answer = 25164150

    def test_main(self):
        self.assertEqual(Problem6(self.bound).fn(), self.answer)


if __name__ == '__main__':
    main()
