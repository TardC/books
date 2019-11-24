from survey import AnonymousSurvey

# Define a question and create an AnonymousSurvey object
# that represents the survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question and store answers.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
