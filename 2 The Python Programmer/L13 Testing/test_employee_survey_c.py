# test_employee_survey_c.py

import unittest

from employee_survey import *

class TestEmployeeSurvey(unittest.TestCase):
    """Tests for the class EmployeeSurvey."""
    
    def setUp(self):
        """create a survey and a set of respones for use in all test methods."""
        question = "What is your current role?"
        self.my_survey = EmployeeSurvey(question)
        self.responses = ['project manager', 'business analysis', 'product owner']
        
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        
    def test_store_three_responses(self):
        """Test that three individual responses can be stored."""
        for response in self.responses:
            self.my_survey.store_response(response)   
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
        
if __name__ == '__main__':
    unittest.main()