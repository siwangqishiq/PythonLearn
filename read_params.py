import sys

argc = len(sys.argv)
print("argc = "+str(argc))
argv = sys.argv

print("Hello %s %s"%(argv[1] , argv[2]))