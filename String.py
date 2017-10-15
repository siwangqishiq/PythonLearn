num_str = "1001"
num_val = int(num_str)# string --> int

num_str = str(num_val)# int --> string

print(num_str)
print(num_val)
print("len = %d"%(len(num_str)))

a = "老"
b = "王"
c = "赵"

a_b = a + b
a_c = a + c

print(a_b)
print(a_c)

template = "你好%s"%("世界")
print(template)

#下标 切片
str1 = "真相永远只有一个";
print(str1[2])
#print(str1[10])
i = 1;
str_len = len(str1)
print("==========")
while i <= str_len:
	print(str1[-i])
	i += 1

name = "abcdefABCDEF"
sub_name = name[0:6]
print(sub_name)
#逆序输出字符串
print(name[-1::-1])
print(str1[-1::-1])
