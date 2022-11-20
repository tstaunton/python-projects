# employee_survey_questions_b.py
from employee_survey import *

# Define a question and create a survey
question = "What is your current role?"
my_survey = EmployeeSurvey(question)

# Show the question and store responses to the question
my_survey.show_question()
print("Enter 'q' to quit.\n")
while True:
    response = input("Current role: ")
    if response == 'q':
        break
    my_survey.store_response(response)
    
# Show the results
print("\nThank you for your time.")
my_survey.show_results()