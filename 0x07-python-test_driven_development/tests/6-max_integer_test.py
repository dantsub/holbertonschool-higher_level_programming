#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Class testing
    """
    def testing(self):
        self.assertEqual(max_integer([1, 3, 4, 56, 78, 9]), 78)
        self.assertEqual(max_integer([-80, 80, 92, 99]), 99)
        self.assertEqual(max_integer([1.190, 78.2, 6.3, float(1)]), float(78.2))
        self.assertEqual(max_integer([-1000, 1]), 1)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-98.5, -7.4]), -7.4)
        self.assertEqual(max_integer([1.1, 1.2, 1.3, 1.4]), 1.4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-10]), -10)
        self.assertEqual(max_integer([1.1, 1, 2.2, 2]), 2.2)
        self.assertEqual(max_integer([3/2, 1, 0.4, 1-0]), 3/2)
    
