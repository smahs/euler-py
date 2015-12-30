#!/usr/bin/python2


class Utilities(object):

    """
    Reusable utility functions
    """

    @classmethod
    def check_prime(cls, num):
        if not num % 2:
            return False
        for i in xrange(3, int(num**0.5) + 1, 2):
            if not num % i:
                return False
        return True

    @classmethod
    def reverse(cls, num):
        rev_num = 0
        while num:
            rev_num = 10 * rev_num + num % 10
            num /= 10
        return rev_num

    @classmethod
    def reverse_s(string):
        try:
            if not isinstance(string, str):
                string = str(string)
            return string[::-1]
        except:
            return None

    @classmethod
    def check_palindrome(cls, num):
        if num == Utilities.reverse(num):
            return True
        return False
