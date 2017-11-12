import sys

class TooShortException(Exception):
	def __init__(self , tips):
		self.tips = tips

s = input("请输入")

try:
	s_len = len(s)
	if s_len < 3:
		raise TooShortException("老子就填这么短啊")
	print(s +" len = "+str(s_len))
except TooShortException as ex:
	print(ex.tips)
