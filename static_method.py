import sys

class Tool(object):
	count = 0
	use = 0
	
	def __init__(self,new_name = "Tool"):
		self.name = new_name
		print("init Tool")
		Tool.count += 1
	
	def do_something(self):
		print(self.name + " do some thing")		
		Tool.use += 1
	
	#静态方法
	@staticmethod
	def show():
		print("========")
		print("========")
		print("========")
		#print(Tool.use)
	
	@classmethod
	def show2(cls):
		print("=====classmethod=====")
		print("="+str(cls.use))
		print("=====classmethod=====")
		
class LanTool(Tool):
	fuck = 1
	
	def __init__(self):
		pass
	


tool = Tool()
tool.do_something()

tool2 = Tool("小辣椒飞机杯")
tool2.do_something()

print(tool2.name)
print("count = %d   use = %d"%(Tool.count , Tool.use))

#lan = LanTool()
#print(LanTool.count)

#LanTool.show()
#LanTool.show2()

#tool.show()
tool.show2()


