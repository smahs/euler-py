#!/usr/bin/python2

"""
Statement:

n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


from unittest import TestCase, main


class Problem20(object):

    def __init__(self, bound):
        self.bound = 100

    def fn(self):
        return sum(map(int, str(reduce(lambda i, j: i*j,
                                       range(1, self.bound)))))


class TestProblem20(TestCase):

    def setUp(self):
        self.bound = 100
        self.answer = 648

    def test_main(self):
        self.assertEqual(Problem20(self.bound).fn(), self.answer)


if __name__ == '__main__':
    main()
