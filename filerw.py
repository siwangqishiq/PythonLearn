#写文件
file = open("想对女友说的话","w")
file.write("你好 世界\n")
file.write("Run or Die!!!!\n")
file.close()

read_file = open("想对女友说的话" , "r")
content = read_file.read()
read_file.close()

print("文件内容%s"%content)