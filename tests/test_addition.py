import unittest

from addition import add_numbers

class Testaddition(unittest.TestCase):
    
    def test_addition_positive_numbers(self):
        self.assertEqual(add_numbers(4, 3), 7)
        
    def test_addition_positive_numbers(self):
            self.assertEqual(add_numbers(5, 3), 8)
    
    def test_addition_positive_numbers(self):
            self.assertEqual(add_numbers(10, 5), 15)
    
    
