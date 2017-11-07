cache = {}

def fab(n):
	if cache.get(n) != None :
		return cache.get(n)

	ret = 1
	if n <= 2:
		ret = 1
	else:
		ret = fab(n - 1) + fab(n - 2)
	cache[n] = ret
	return ret

		
val = 1
while val <= 100:
	print("fab(%d) = %d" %(val , fab(val)))
	val += 1