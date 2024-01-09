"""
Sample Tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test with Cal Module"""
    
    def test_add_numbers(self):
        """ Test adding numbers together. """
        res = calc.add(5, 6)
        
        self.assertEqual(res, 11)
        
    def test_subtract_numbers(self):
        """ Test subtract numbers """
        res = calc.subtract(15, 10)
        
        self.assertEqual(res, 5)