import sys

class Animal(object):
	def __init__(self):
		print("Animal init func")
	
	def say(self):
		print("hi~~~")
	
class Dog(Animal):
	def __init__(self):
		super().__init__()
		print("Dog init func")

	def fuck(self):
		print("Fuck")
		
wang = Dog()
wang.say()
wang.fuck()