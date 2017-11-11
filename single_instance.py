import sys

class Cat(object):
	__instance = None
	
	def __new__(cls):
			if Cat.__instance == None:
				Cat.__instance = object.__new__(cls)
			return Cat.__instance
	
	def __init__(self):
		self.name = "小花"
	
	def set_cat_name(self , new_name):
		if self.name != new_name :
			self.name = new_name
			
	def miao(self):
		print(self.name + "  Miao miao miao!")
		
cat1 = Cat()
cat1.miao()

cat2 = Cat()
cat2.miao()

cat1.set_cat_name("大黄猫")
cat2.miao()

print(id(cat1))
print(id(cat2))


		
		