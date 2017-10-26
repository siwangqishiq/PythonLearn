
def main():
	data = [{"name":"毛利兰","age":17},{"name":"工藤新","age":18},{"name":"鲁鲁修","age":16},{"name":"夜神月","age":20}]
	for d in data:
		print(d)

	print("="*50)
	
	data.sort(key = lambda x:x["age"])	
	
	for d in data:
		print(d)

main()
