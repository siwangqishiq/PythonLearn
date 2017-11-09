import sys

class Animal(object):
	def __init__(self):
		self.__age = 10
		self.age = 11
		self.name = "animal"
		print("Animal init func")
	
	def say(self):
		print("hi~~~")
	
class Dog(Animal):
	def __init__(self):
		super().__init__()
		print("Dog init func")

	def fuck(self):
		print("Fuck")
		print("name = %s"%self.name)
		print("age = %s"%self.age)
		
wang = Dog()
wang.say()
wang.fuck()

#print(Dog._maro_())