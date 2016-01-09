#!/usr/bin/python2

"""
Statement:

In England the currency is made up of pound, P, and pence, p,
and there are eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, P1 (100p) and P2 (200p).

It is therefore possible to make P2 in the following way:
    1xP1, 1x50p, 2x20p, 1x5p, 1x2p, 3x1p

How many different ways can P2 be made using any number of coins?

=======================================================

Prelude:

This problem is a modified version of coin change or integer
partition problem, which can be solved by recursion. To improve
the performance, memoization or caching can be used.

However since the sub problems (recusive calls) overlap each other,
and one of them is the globally optimal solution, it satisfies
the necessary conditions of a dynamic programming problem.

While the actual construction of the problem is not shown
here, some suitable references are listed below:
[1] http://www.algorithmist.com/index.php/Coin_Change
[2] https://andrew.neitsch.ca/publications/m496pres1.nb.pdf
"""


from unittest import TestCase, main


class Problem31(object):

    def __init__(self, bound):
        self.bound = bound
        self.coins = [1, 2, 5, 10, 20, 50, 100, 200]

    def fn(self):
        mat = [0 for i in xrange(len(self.coins) - 1)]
        mat = [[1] + mat for i in xrange(self.bound)]
        for amt in xrange(self.bound):
            for ci, cv in enumerate(self.coins[1:]):
                mat[amt][ci+1] = mat[amt][ci]
                if amt >= cv:
                    mat[amt][ci+1] += mat[amt-cv][ci+1]
        return mat[-1][-1]


class TestProblem31(TestCase):

    def setUp(self):
        self.bound = 200 + 1  # (2 pounds in lowest denomination)
        self.answer = 73682

    def test_main(self):
        self.assertEqual(Problem31(self.bound).fn(), self.answer)


if __name__ == '__main__':
    main()
