#! /anaconda3/bin/python
import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_exponential(self):
        result = rpn.calculate("2 2 ^")
        self.assertEqual(4, result)
    def value_error_fun(self):
        result = rpn.calculate("1 + +")

    def type_error_fun(self):
        result = rpn.calculate("1 2 3 +")

    def test_error(self):
        self.assertRaises(Exception, self.value_error_fun)
        self.assertRaises(Exception, self.type_error_fun)


def main():
    test = TestBasics()
    test.test_add()
    test.test_subtract()
    test.test_multiply()
    test.test_divide()
    test.test_exponential()
    test.test_error()


if __name__ == '__main__':
    main()