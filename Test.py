#!/usr/bin/python3
import unittest

from Division import divide

class Tests(unittest.TestCase):    
    def pass_test_case_1(self):
        a = 10
        b = 5
        
        result = divide(a, b)
        self.assertEqual(result, 2.0)
        
    def pass_test_case_2(self):
        a = 1
        b = 4
        
        result = divide(a, b)
        self.assertEqual(result, 0.25)
        
    def pass_test_case_3(self):
        a = -4
        b = 2
        
        result = divide(a, b)
        self.assertEqual(result, -2.0)
        
    def fail_test_case_1(self):
        a = 10
        b = 0
        
        result = divide(a, b)
        
    def fail_test_case_2(self):
        a = 100
        b = 2
        
        result = divide(a, b)
        self.assertEqual(result, 500.0)

if __name__ == '__main__':
    unittest.main()