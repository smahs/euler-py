#!/usr/bin/python2

"""
Statement:

Starting in the top left corner of a 2x2 grid, and only being
able to move to the right and down, there are exactly 6 routes
to the bottom right corner.

How many such routes are there through a 20x20 grid?

====================================================

Prelude:

This is an NP-hard problem whose size increases very quickly
through time and space. A dynamic programming approach is more
suitable, with backtracking.

For a grid G(m,n) with the top left most point being G(0,0),
to travel the first square G(1,1) there are exactly two paths.
That is either right-down or down-right. For G(2,1) and G(1,2),
there are exactly three paths each, 1 step from G(1,1). To arrive
at the next diagonal point, i.e. G(2,2), there are exactly two
immediate neighbours, i.e. G(2,1) and G(1,2). Hence the total
number of paths to G(2,2) is the sum of paths to G(2,1) and G(1,2).

This can be generalized for traversing along the diagonal as:
    1. Traverse right by summing j and j-1 (paths to point j)
    2. Traverse below by multiplying by 2 (paths to the diagonal)
"""


from unittest import TestCase, main


class Problem15(object):

    def __init__(self, bound):
        self.bound = bound

    def fn(self):
        grid = [1] * self.bound
        for i in range(len(grid)):
            for j in range(i):
                grid[j] = grid[j]+grid[j-1]
            grid[i] = 2 * grid[i - 1]
        return grid[len(grid) - 1]


class TestProblem15(TestCase):

    def setUp(self):
        self.bound = 20
        self.answer = 137846528820

    def test_main(self):
        self.assertEqual(Problem15(self.bound).fn(), self.answer)


if __name__ == '__main__':
    main()
