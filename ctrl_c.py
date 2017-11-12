import time

try:
	while True:
		print("Hello World")
		time.sleep(1)
except Exception as ex:
	print("press exit")
finally:
	print("exit program")