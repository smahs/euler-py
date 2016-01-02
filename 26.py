#!/usr/bin/python2

"""
Statement:

A unit fraction contains 1 in the numerator. The decimal
representation of the unit fractions with denominators
2 to 10 are given:

    1/2 =   0.5
    1/3 =   0.(3)
    1/4 =   0.25
    1/5 =   0.2
    1/6 =   0.1(6)
    1/7 =   0.(142857)
    1/8 =   0.125
    1/9 =   0.(1)
    1/10    =   0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest
recurring cycle in its decimal fraction part.

=====================================================

Prelude:

According to [1], the longest repeating periods are generated
by primes in the denominator of a fraction m/n.

Repeating terms are given by (10^p -1) / n. This is obtained by
realizing that 1/n is represented as
    1/n = r * 10^-p + r * 10^-2p + ...  (Geometric series)
    1/n = r * 1/(10^p - 1)      (Sum of geometric series)
    r = (10^p - 1) / n

[1] http://mathworld.wolfram.com/DecimalExpansion.html
"""


from unittest import TestCase, main
from utils import prime_sieve


class Problem26(object):

    def __init__(self, bound):
        self.bound = bound

    def terms(self, denom):
        left, sub, count = 9, 9, 1
        while sub % denom:
            sub = sub * 10 + left
            count += 1
        return count

    def fn(self):
        primes = prime_sieve(self.bound)
        primes = [i for i, v in enumerate(primes) if v][1:]
        bag = {i: self.terms(i) for i in primes
               if i is not 2 and i is not 5}
        return max(bag, key=bag.get)


class TestProblem26(TestCase):

    def setUp(self):
        self.bound = 1000
        self.answer = 983

    def test_main(self):
        self.assertEqual(Problem26(self.bound).fn(), self.answer)


if __name__ == '__main__':
    main()
