#!/usr/bin/python

import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)

    def test_sub(self):
        result = rpn.calculate('4 3 -')
        self.assertEqual(1, result)

    def test_toomany(self):
        with self.assertRaises(ValueError):
            result = rpn.calculate('1 2 3 +')

    def test_exp(self):
        result = rpn.calculate('2 3 ^')
        self.assertEqual(8, result)
        result = rpn.calculate('10 4 ^')
        self.assertEqual(10000, result)

    def test_multiply(self):
        result = rpn.calculate('4 5 *')
        self.assertEqual(20, result)





