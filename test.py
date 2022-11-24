#!/usr/bin/python3
import unittest

from Prog1 import add
from Concat import add_string

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        x = 10
        y = 10
        result_1 = add(x,y)

        x = 80
        y = 20
        result_2 = add(x,y)

        result_3 = add_string("Hi","there")

        self.assertEqual(result_1, 20)
        self.assertEqual(result_2, 100)
        self.assertEqual(result_3,"hi there")

if __name__ == '__main__':
    unittest.main()