#字典
map = {"key1":"value1" , "key2":"value2"}

print("="*40)
print(map)

print(map["key1"])
print(map.get("key1"))
print(map.get("key3"))

if map.get("key3") == None:
	print("key3 not exist")
	
del map["key2"]
print(map)

