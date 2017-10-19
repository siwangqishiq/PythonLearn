def sum(num1 , num2 , num3):
	return num1 + num2 + num3

def average(total):
    return total / 3

num1 = int(input("请输入第一个数"))
num2 = int(input("请输入第二个数"))
num3 = int(input("请输入第三个数"))

a = average(sum(num1 , num2 , num3))

print("average = %d"%a)


