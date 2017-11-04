class Cat:
	def __init__(self, name , age):
		self.name = name
		self.age = age

	def __str__(self):
		return "name = %s age = %d"%(self.name , self.age)


def changeCat(cat ,new_name , new_age):
	cat.name = new_name
	cat.age = new_age
	
cat1 = Cat("拉普拉斯" , 12)
print(cat1)

changeCat(cat1 , "Hello" , 11)
print(cat1)

cat1.name = "Hello"
cat1.age = 10

