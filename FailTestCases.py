#!/usr/bin/python3
import unittest

from Division import divide

class Tests(unittest.TestCase): 
    def test_case_fail_1(self):
        a = 10
        b = 0
        
        result = divide(a, b)
        print("test_case_fail_1 passed!")
        
    def test_case_fail_2(self):
        a = 100
        b = 2
        
        result = divide(a, b)
        self.assertEqual(result, 500.0)
        print("test_case_fail_2 passed!")

if __name__ == '__main__':
    unittest.main()