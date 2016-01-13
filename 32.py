#!/usr/bin/python2


"""
Statement:
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""


from unittest import TestCase, main


class Problem32(object):
    def __init__(self, limit):
        self._limit = limit

    def check_pandigital(self, string):
        num_list = [0] * 10
        num_list[0] = 1
        for i in string:
            if num_list[int(i)] == 0:
                num_list[int(i)] = 1
            else:
                return False
        return True

    def fn(self):
        pandigital_list = []
        for i in xrange(1, self._limit + 1, 1):
            j = i + 1
            prod = i * j
            string = str(i) + str(j) + str(prod)
            while(len(string) < 10):
                if len(string) == 9:
                    if self.check_pandigital(string):
                        if prod not in pandigital_list:
                            pandigital_list.append(prod)
                j += 1
                prod = i * j
                string = str(i) + str(j) + str(prod)
        return sum(pandigital_list)


class TestProblem32(TestCase):
    def setUp(self):
        self.limit = 100
        self.answer = 45228

    def test_fn(self):
        self.assertEqual(Problem32(self.limit).fn(), self.answer)


if __name__ == '__main__':
    main()
