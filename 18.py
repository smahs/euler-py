#!/usr/bin/python2


"""
Statement:

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method! ;o)
"""

instr = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


from unittest import TestCase, main
from copy import deepcopy


instr = [[int(i) for i in s.split(' ')]for s in instr.split('\n') if s]


class Problem18(object):
    def __init__(self, instr):
        self._matrix = instr
        self._solution = deepcopy(instr)

    def fn(self):
        max_sum = 0
        for i in xrange(len(self._matrix) - 1):
            for j in xrange(i + 1):
                self._solution[i + 1][j] = (self._solution[i][j]
                                            + self._matrix[i + 1][j]
                                            if self._solution[i][j]
                                            + self._matrix[i + 1][j]
                                            > self._solution[i + 1][j]
                                            else self._solution[i + 1][j])
                self._solution[i + 1][j + 1] = (self._solution[i][j]
                                                + self._matrix[i + 1][j + 1]
                                                if self._solution[i][j]
                                                + self._matrix[i + 1][j + 1]
                                                > self._solution[i + 1][j + 1]
                                                else self._solution[i + 1][j + 1])
                tmp = (self._solution[i + 1][j] if self._solution[i + 1][j]
                       > self._solution[i + 1][j + 1]
                       else self._solution[i + 1][j + 1])
                max_sum = (tmp if tmp > max_sum else max_sum)
        return max_sum


class TestProblem18(TestCase):
    def setUp(self):
        self.instr = instr
        self.answer = 1074

    def test_fn(self):
        self.assertEqual(Problem18(self.instr).fn(), self.answer)


if __name__ == '__main__':
    main()
