#!/usr/bin/python3
import unittest

from Division import divide

class Tests(unittest.TestCase): 
    def test_case_pass_1(self):
        a = 10
        b = 5
        
        result = divide(a, b)
        self.assertEqual(result, 2.0)
        print("test_case_pass_1 passed!")
        
    def test_case_pass_2(self):
        a = 1
        b = 4
        
        result = divide(a, b)
        self.assertEqual(result, 0.25)
        print("test_case_pass_2 passed!")
        
    def test_case_pass_3(self):
        a = -4
        b = 2
        
        result = divide(a, b)
        self.assertEqual(result, -2.0)
        print("test_case_pass_3 passed!")
        
if __name__ == '__main__':
    unittest.main()