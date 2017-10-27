def operation(a , b , op):
	result = op(a , b)
	print("result = %d"%result)
	return result
	
num1 = 100
num2 = 200

op = lambda x,y:x-y

operation(num1 , num2 , op)
