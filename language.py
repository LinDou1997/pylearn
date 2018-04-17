from survey import Survey
question = 'What language did you learn to speak?'
my_survey = Survey(question)
my_survey.show()
print('Enter q at any time to quit.')
while True:
	response = input('Language:')
	if response == 'q':
		break
	my_survey.store(response)
print('\nThank you to everyone who participated in the survey!')
my_survey.show_results()