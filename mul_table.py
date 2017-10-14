import random

j = 0
while j < 100:
	val = random.randint(0,5)
	print(val)
	j += 1

i = 1
 
while i <= 9:
	k = 1
	while k <= i:
		print("%dx%d=%d\t" %(k , i , k * i) , end = "")
		k += 1
	i += 1
	print("")
	
