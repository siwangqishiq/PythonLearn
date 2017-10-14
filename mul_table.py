i = 1
 
while i <= 9:
	k = 1
	while k <= i:
		print("%dx%d=%d  " %(k , i , k * i) , end = "")
		k += 1
	i += 1
	print("")
