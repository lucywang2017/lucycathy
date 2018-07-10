
dict ={
	'Hello':'hello',
	'what is your name?':"Lilei",
	'Nice to meet you':'Nice to meet you',
	'Good night':'Good night'
}


#t-train 训练机器人对话 c-chat同机器人聊天 l-leave 让机器人离开

flag = 'c' #机器人默认是聊天状态
work = True #机器人默认是工作的

print('Hi, my name is python')
print('Do you want chat with me?')

while flag =='c' or 't':
	flag = input("你想跟我聊天(c)还会训练我对话(t),还是让我离开(l)")
	#训练状态：
	if flag =="t":
		question = input("请输入问题(key):")
		answer = input("请输入回答(value)")
		dict[str(question)] = str(answer)
		print("训练成功")
		print("现在我已经会{}个问题了".format(len(dict)))
		continue

	elif flag =='c':
		if(len(dict)) ==0:
			print("我现在还不会任何问题，请先训练我！")
			continue
		chat_word = input("谢谢你跟我聊天，你想对我说什么：")

		for key in sorted(dict.keys()):
			if str(chat_word) == key:
				work = True
				print (dict[key])
				break
			else:
				work = False
		if work == False:
			print ("抱歉，这句话我还不会回答")
			work = True

	elif flag =='l':
		print ("好的，下次再见")
		break
	else:
		print ("请输入提示的指令:")
		continue






