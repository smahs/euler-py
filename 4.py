#!/usr/bin/python2


from unittest import TestCase, main
from utils import Utils


class Problem4(object):
    def __init__(self):
        pass

    def run(self):
        pal = 0
        for i in xrange(1000, 100, -1):
            if i % 11 == 0:
                j = 999
                db = 1
            else:
                j = 990
                db = 11
            while(j >= i):
                if i * j < pal:
                    break
                if Utils.check_palindrom(i * j):
                    pal = i * j
                j -= db
        return pal


class Testproblem4(TestCase):
    def setUp(self):
        self.answer = 906609

    def test_run(self):
        self.assertEqual(Problem4().run(), self.answer)


if __name__ == '__main__':
    main()
