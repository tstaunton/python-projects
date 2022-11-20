# test_name_function_c.py

import unittest
from name_function_c import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function'."""
    
    def test_first_last_name(self):
        "Test simple first and last names."
        formatted_name = get_formatted_name('tony', 'staunton')
        self.assertEqual(formatted_name, 'Tony Staunton')
        
    def test_first_last_middle_name(self):
        """Do middle names work?"""
        formatted_name = get_formatted_name('tony', 'staunton', 'frank')
        self.assertEqual(formatted_name, 'Tony Frank Staunton')
        
if __name__ == '__main__':
    unittest.main()