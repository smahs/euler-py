#!/usr/bin/python2

"""
Statement:

Work out the first ten digits of the sum of the following
one-hundred 50-digit numbers.
"""


from unittest import TestCase, main


filename = '13.txt'
with open(filename, 'r') as f:
    numstr = [i for i in f.readlines()]


class Problem13(object):

    def fn(self):
        return str(sum(map(int, numstr)))[:10]


class TestProblem13(TestCase):

    def setUp(self):
        self.answer = '5537376230'

    def test_main(self):
        self.assertEqual(Problem13().fn(), self.answer)


if __name__ == '__main__':
    main()
