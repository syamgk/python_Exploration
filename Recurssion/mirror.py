class RTEST:    
# Recursion test on functions
	def __init__(self):
		self.i = 0
		self.j = 0

	def first(self):
#calling second function 
		print "first","IN"
		self.second()

	def second(self):
#calling first function
		print "second","\tIN"
		self.i += 1
		try:
			self.first()
		except:
			print "Count is",self.i
		self.j += 1
		print "second \t OUT<>",self.j
b=RTEST()
b.second()
print '\b',b.i
