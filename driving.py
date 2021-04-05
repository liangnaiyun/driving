country = input('請問您是哪國人：')
age = input('請問您的年齡：')
age = int(age)
if country == '台灣':
	if age >= 18:
		valid_message()
	else:
		invalid_message()
elif country == '美國':
	if age >= 16:
		valid_message()
	else:
		invalid_message()

def valid_message():
	print('您可以考駕照')

def invalid_message():
	print('您還不能考駕照')


