#!/usr/bin/python2

"""
Contains the functions defination which are commonly used
"""
from math import sqrt


class Utils(object):
    @classmethod
    def check_prime(cls, num):
        for i in xrange(2, int(sqrt(num)) + 1, 1):
            if num % i == 0:
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
    def check_palindrom(cls, num):
        if num == Utils.reverse(num):
            return True
        return False
