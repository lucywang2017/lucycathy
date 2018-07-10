
while 1:
	try:
		num1 = int(input('输入被除数:'))
		num2 = int(input('输入除数:'))
		result = int(num1)/int(num2)
	except ZeroDivisionError:
		print ('0不能做除数' + '\n')

	except ValueError:
		print ('请勿输入空值或者字母' + '\n')
	else:
		print ('运算结果为:{}'.format(result) +'\n')
