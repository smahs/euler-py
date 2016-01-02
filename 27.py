#!/usr/bin/python2

"""
Statement:

Euler discovered the remarkable quadratic formula:

    n^2 + n + 41

It turns out that the formula will produce 40 primes for the
consecutive values n = 0 to 39.
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is
divisible by 41, and certainly when n = 41, 41^2 + 41 + 41
is clearly divisible by 41.

The incredible formula  n^2 - 79n + 1601 was discovered, which
produces 80 primes for the consecutive values n = 0 to 79.
The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for
consecutive values of n, starting with n = 0.

===================================================

Prelude:

For n = 0: n^2 + an + b = b. Hence b has to be positive prime itself.
For n = 1: n^2 + an + b = 1 + a + b; which has to be odd to be
a prime. Since b is odd as it is a prime, a has to be odd as well.
However, if b = 2, a has to be even.

It is assumed that the maximum sequence length is bounded by 79,
which proved to be correct in this case. With this bound, we get the
upper bound for the prime sieve as:
    79^2 + 1000*79 + 1000 = 86241
"""


from unittest import TestCase, main
from utils import prime_sieve


class Problem27(object):

    def __init__(self, bound, lim):
        self.bound = bound
        self.seqlim = lim ** 2 + 1000 * lim + 1000

    def fn(self):
        sieve = prime_sieve(self.seqlim)
        a, b, maxlen = 0, 0, 0
        for i in range(-1 * self.bound, self.bound + 1):
            for j in range(1, self.bound + 1):
                if not sieve[j]:
                    seqlen, n = 0, 0
                while sieve[n**2 + i*n + j]:
                    seqlen += 1
                    n += 1
                if seqlen > maxlen:
                    a, b, maxlen = i, j, seqlen
        return a * b

class TestProblem27(TestCase):

    def setUp(self):
        self.bound = 1000
        self.seqlim = 79
        self.answer = -59231

    def test_main(self):
        self.assertEqual(Problem27(self.bound, self.seqlim).fn(),
                         self.answer)


if __name__ == '__main__':
    main()
