
while 1:
	try:
		num1 = int(input('输入被除数:'))
		num2 = int(input('输入除数:'))
		result = int(num1)/int(num2)
	except BaseException:
		print ('出现异常' +'\n')
	else:
		print ('运算结果为:{}'.format(result) +'\n')
