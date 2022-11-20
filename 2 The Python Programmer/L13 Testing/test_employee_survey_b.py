# test_survey.py

import unittest

from employee_survey import *

class TestEmployeeSurvey(unittest.TestCase):
    """Tests for the class EmployeeSurvey."""
    
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What is your current role?"
        my_survey = EmployeeSurvey(question)
        my_survey.store_response('project manager')
        self.assertIn('project manager', my_survey.responses)
        
    def test_store_three_responses(self):
        """Test that three individual responses can be stored."""
        question = "What is your current role?"
        my_survey = EmployeeSurvey(question)
        responses = ['project manager', 'business analysis', 'product owner']
        for response in responses:
            my_survey.store_response(response)
            
        for response in responses:
            self.assertIn(response, my_survey.responses)
        
if __name__ == '__main__':
    unittest.main()