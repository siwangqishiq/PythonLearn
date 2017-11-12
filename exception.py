#异常
import sys

class Cat(object):
	def say(self):
		print("喵喵!")
		
cat = Cat()
cat.say()

try:
	print(count)
	print("Haha")
except NameError:
	print("NameError")

try:
	cat = None
	cat.say()	
except:
	print("NullPointer Error")

try:	
	file = open("exception.py")
	content = file.read()
	print(content)
	file.close()
except Exception as ex :
	print("读文件发生异常 : ")
	print(ex)
else:
	print("没有异常发生")
finally:
	print("hahaha   finally")
	