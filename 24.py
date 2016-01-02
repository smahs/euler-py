#!/usr/bin/python2

"""
Statement:

A permutation is an ordered arrangement of objects. For example,
3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of
0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

===================================================

Prelude:

This problem is about combinations without repetitions.
Hence fixing the first position, there are (n-1)! possible
combinations for the remaining terms. In this case, it is
9! = 362880. So the first term must be 2 for the millionth
combination. Similarly, there are 40320 possible combinations
for the last 8 terms fixing the second term. Thus, for the
millionth term, the second term must be 7.

Repeating this process, we can arrive at the result. This
solution is way faster than the iterative alt1 and alt2
solutions.

The solution is explained at:
http://www.mathblog.dk/project-euler-24-millionth-lexicographic-permutation/

Note 1: The last term in combinatorics algorithm is actually
the last remaining unused term as this has only one possibility.
Hence we have find the first terms for the first n-1 combinations.

Note 2: Solution alt1 is a representation of itertools based alt2.
Both alt1 and alt2 are memory safe, and should not cause
stackoverflow exception! These solutions are more generic and
can be used for non alphanumeric terms as well.
"""


from unittest import TestCase, main
from itertools import permutations
from math import factorial
from copy import deepcopy


class Problem24(object):

    def __init__(self, bound):
        self.bound = bound
        self.seq = range(10)

    def fn(self):
        left = self.bound - 1  # Note 1 above
        tracker = deepcopy(self.seq)
        num = ''
        for i in self.seq[1:]:
            fact = factorial(len(self.seq) - i)
            divisor = left / fact
            left %= fact
            num += str(tracker[divisor])
            tracker.remove(tracker[divisor])
            if not left:
                break
        return num + ''.join(map(str, tracker))

    def alt1(self):
        """
        Ensure self.bound <= factorial(len(self.seq))
        Or fix it below by checking if i==0!
        """
        seq = self.seq
        counter = 1
        while counter < self.bound:
            i, j = len(seq) - 2, len(seq) - 1
            while seq[i] >= seq[i+1]:
                i -= 1
            while seq[i] >= seq[j]:
                j -= 1
            seq[i], seq[j] = seq[j], seq[i]
            seq[i+1:] = reversed(seq[i+1:])
            counter += 1
        return ''.join(map(str, seq))

    def alt2(self):
        counter = 0
        perm = permutations(self.seq)
        while counter < self.bound:
            seq = perm.next()
            counter += 1
        return ''.join(map(str, seq))


class TestProblem24(TestCase):

    def setUp(self):
        self.bound = 1000000
        self.answer = '2783915460'

    def test_main(self):
        self.assertEqual(Problem24(self.bound).fn(), self.answer)

    def test_alt1(self):
        self.assertEqual(Problem24(self.bound).alt1(), self.answer)

    def test_alt2(self):
        self.assertEqual(Problem24(self.bound).alt1(), self.answer)


if __name__ == '__main__':
    main()
