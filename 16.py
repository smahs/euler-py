#!/usr/bin/python2

"""
Statement:

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""


from unittest import TestCase, main


class Problem16(object):

    def __init__(self, power):
        self.power = 1000

    def fn(self):
        return sum(map(int, str(2**self.power)))


class TestProblem16(TestCase):

    def setUp(self):
        self.power = 1000
        self.answer = 1366

    def test_main(self):
        self.assertEqual(Problem16(self.power).fn(), self.answer)


if __name__ == '__main__':
    main()
