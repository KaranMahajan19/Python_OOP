######################################################
#	Instance variable : No1, No2
#	Instance method   : Fun(), Gun()
#	Class variable    : Value
######################################################

class Demo:
	
	Value = 0
	def __init__(self,A,B):
		self.No1 = A
		self.No2 = B

	def Fun(self):
		print("Value of No1 inside fun is : ",self.No1)
		print("Value of No2 inside fun is : ",self.No2)

	def Gun(self):
		print("Value of No1 inside gun is : ",self.No1)
		print("Value of No2 inside gun is : ",self.No2)

def main():
	obj1 = Demo(11,21)
	obj2 = Demo(51,101)
	
	obj1.Fun()
	obj2.Fun()
	print()
	obj1.Gun()
	obj2.Gun()
	
if __name__ == "__main__":

	main()


######################################################
#	
#	Output :
#		Value of No1 inside fun is :  11
#		Value of No2 inside fun is :  21
#		Value of No1 inside fun is :  51
#		Value of No2 inside fun is :  101
#
#		Value of No1 inside gun is :  11
#		Value of No2 inside gun is :  21
#		Value of No1 inside gun is :  51
#		Value of No2 inside gun is :  101 
#
######################################################