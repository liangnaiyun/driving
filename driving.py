def valid_message():
	print('您可以考駕照')

def invalid_message():
	print('您還不能考駕照')

age = 0
def age_input():
	global age #使用global age 變數
	age = input('請問您的年齡：')
	age = int(age)

country = input('請問您是哪國人：')

if country == '台灣':
	age_input()
	if age >= 18:
		valid_message()
	else:
		invalid_message()
elif country == '美國':
	age_input()
	if age >= 16:
		valid_message()
	else:
		invalid_message()
else:
	print('請輸入台灣或是美國')




