#list 的使用
import random

names = ["毛利兰","工藤新一","灰原哀"]

for name in names:
	print(name+" " , end = "")

print(names)

names.append("隔壁老王")
print(names)
names.insert(0,"隔壁老李")
print(names)

print(len(names))