#!/usr/bin/python2

"""
Statement:

Starting with the number 1 and moving to the right in a
clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the
diagonals is 101.

What is the sum of the numbers on the diagonals in a
1001 by 1001 spiral formed in the same way?
"""


from unittest import TestCase, main


class Problem28(object):

    def __init__(self, bound):
        self.bound = bound

    def fn(self):
        bag = [1]
        for i in xrange(1, self.bound/2+1):
            last = bag[-1]
            for j in xrange(1, 5):
                bag.append(last + 2*i*j)
        return sum(bag)

    def alt(self):
        total, last = 1, 1
        for i in xrange(1, self.bound/2+1):
            last = (2 * i - 1) ** 2
            for j in xrange(1, 5):
                total += last + 2*i*j
        return total


class TestProblem28(TestCase):

    def setUp(self):
        self.bound = 1001
        self.answer = 669171001

    def test_main(self):
        self.assertEqual(Problem28(self.bound).fn(), self.answer)

    def test_alt(self):
        self.assertEqual(Problem28(self.bound).alt(), self.answer)


if __name__ == '__main__':
    main()
