#!/usr/bin/python2

"""
Statement:

The following iterative sequence is defined for the set
of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the
following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and
finishing at 1) contains 10 terms. Although it has not been
proved yet (Collatz Problem), it is thought that all
starting numbers finish at 1.

Which starting number, under one million, produces
the longest chain?

NOTE: Once the chain starts the terms are allowed to
go above one million.

====================================================

Prelude:

Sequences lengths are saved for quick lookups. So for
any integer n, lengths of all integers upto n-1 are known.
"""


from unittest import TestCase, main


class Problem14(object):

    def __init__(self, bound):
        self.bound = bound
        self.lengths = [0] * bound

    def chain(self, number, counter=1):
        newnum = number
        while newnum > 1:
            if newnum < number:
                counter += self.lengths[newnum-1]
                newnum = 1
            else:
                newnum = (newnum / 2 if not newnum % 2
                          else (3 * newnum + 1))
                counter += 1
        self.lengths[number-1] = counter

    def fn(self):
        map(self.chain, xrange(1, self.bound+1))
        return self.lengths.index(max(self.lengths)) + 1


class TestProblem14(TestCase):

    def setUp(self):
        self.bound = 1000000
        self.answer = 837799

    def test_main(self):
        self.assertEqual(Problem14(self.bound).fn(), self.answer)


if __name__ == '__main__':
    main()
