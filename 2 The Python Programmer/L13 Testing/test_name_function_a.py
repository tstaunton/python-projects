import unittest
from name_function_a import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function'."""
    
    def test_first_last_name(self):
        "Test simple first and last names."
        formatted_name = get_formatted_name('tony', 'staunton')
        self.assertEqual(formatted_name, 'Tony Staunton')
        
if __name__ == '__main__':
    unittest.main()