def convert_set_list(set_data):
	return list(set_data)

data = [11,22,33,44,11,11,11]

data_set = set(data)
print(data_set)

lst = convert_set_list(data_set)
print(lst)

