#!/usr/bin/python2

"""
Statement:

Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list.
So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""


from unittest import TestCase, main
from string import letters


filename = '22.txt'


class Problem22(object):

    def __init__(self):
        with open(filename, 'r') as f:
            self.names = sorted(i.strip('"').lower()
                                for i in f.read().split(','))
        self.letters = sorted(list(set(letters.lower())))

    def fn(self):
        return sum(((self.names.index(name)+1) *
                    sum(self.letters.index(char)+1 for char in name)
                    for name in self.names))


class TestProblem22(TestCase):

    def setUp(self):
        self.answer = 871198282

    def test_main(self):
        self.assertEqual(Problem22().fn(), self.answer)


if __name__ == '__main__':
    main()
