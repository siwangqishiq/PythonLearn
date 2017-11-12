#import my_module

#my_module.test1()
#my_module.test2()

#cat = my_module.Cat()
#cat.say()

#from my_module import test1,test2,Cat,count
from my_module import *
test1()
test2()
cat = Cat()
cat.say()
print(count)