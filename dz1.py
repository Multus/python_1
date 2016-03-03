import sys

input = input if (sys.version_info.major == 3) else raw_input
questions = {
	'when Python 2.7? won`t work ? ': '2020',
	'how truth means in Python?': 'True',
	'what comand writes something to the console': 'print()',
	'what is the type of this number: 3.14': 'float',
	'when Python emerged': '1991',
	'a=\'string\', b="string". are a и b the same?': 'yes'
}
incorrectAnswers = 0
for question in questions:
	x = True
	while x:
		try:
			if input(question + '\n') != questions[question]:
				incorrectAnswers += 1
				raise(ValueError())
			else: x = False
		except ValueError:
			print('no')
print('you win! fails:', incorrectAnswers)

