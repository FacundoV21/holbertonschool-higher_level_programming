#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty(self):
        i = max_integer([])
        self.assertEqual(i, None)

    def test_normal(self):
        i = max_integer([1, 2, 4, 2])
        self.assertEqual(i, 4)

    def test_one(self):
        i = max_integer([5])
        self.assertEqual(i, 5)
        
    def test_negative_values(self):
        i = max_integer([-7, -5, -2, 1])
        self.assertEqual(i, 1)
