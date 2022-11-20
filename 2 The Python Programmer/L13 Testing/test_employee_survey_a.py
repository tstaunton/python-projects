import unittest
from employee_survey import *

# test_survey.py
class TestEmployeeSurvey(unittest.TestCase):
    """Tests for the class EmployeeSurvey."""
    
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What is your current role?"
        my_survey = EmployeeSurvey(question)
        my_survey.store_response('project manager')
        self.assertIn('project manager', my_survey.responses)
        
if __name__ == '__main__':
    unittest.main()