#!/usr/bin/python2

"""
Statement:

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly
believe that 49/98 = 4/8, which is correct, is obtained by
cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be
trivial examples.

There are exactly four non-trivial examples of this type of
fraction, less than one in value, and containing two digits
in the numerator and denominator.

If the product of these four fractions is given in its lowest
common terms, find the value of the denominator.

"""

from unittest import TestCase, main
from fractions import Fraction


class Problem33(object):

    def __init__(self, bound):
        self.bound = bound

    def fn(self):
        bucket = []
        for i in xrange(*self.bound):
            for j in xrange(i+1, self.bound[1]):
                if not i % 10 and not j % 10:
                    continue
                num1, num2 = map(set, map(str, (i, j)))
                intsctn = num1.intersection(num2)
                newi, newj = map(str, (i, j))
                for k in intsctn:
                    newi = newi.replace(k, '', 1)
                    newj = newj.replace(k, '', 1)
                if not len(newi) or not len(newj):
                    continue
                newi, newj = map(int, (newi, newj))
                if not newj or newi == i or newj == j:
                    continue
                if Fraction(i, j) == Fraction(newi, newj):
                    bucket.append(Fraction(i, j))
        return reduce(lambda i, j: i * j, bucket).denominator


class TestProblem33(TestCase):

    def setUp(self):
        self.bound = (11, 99)
        self.answer = 100

    def test_main(self):
        self.assertEqual(Problem33(self.bound).fn(), self.answer)


if __name__ == '__main__':
    main()
