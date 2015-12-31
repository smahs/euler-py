#!/usr/bin/python2

"""
Statement:

You are given the following information, but you may prefer
to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4,
    but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the
twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


from unittest import TestCase, main
from calendar import Calendar, SUNDAY


class Problem19(object):

    def __init__(self):
        self.cal = Calendar()

    def fn(self):
        return len([1 for day in [week for year in range(1901, 2001)
                                  for month in self.cal.yeardayscalendar(year)
                                  for weeks in month for week in weeks]
                    if day[SUNDAY] == 1])


class TestProblem19(TestCase):

    def setUp(self):
        self.answer = 171

    def test_main(self):
        self.assertEqual(Problem19().fn(), self.answer)


if __name__ == '__main__':
    main()
