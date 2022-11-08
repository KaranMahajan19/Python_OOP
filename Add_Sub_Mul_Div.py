###########################################################################
#
#	Instance variable : VAlue1, Value2
#	Instance method   : Accept(), Addition(), Subtraction(), Multiplication(),
#						Division()
#
############################################################################

class Arithmetic:

	def __init__(self):
		self.Value1 = 0
		self.Value2 = 0
		
	def Accept(self):
		self.Value1 = int(input("Enter first number : "))
		self.Value2 = int(input("Enter second number : "))

	def Addition(self):
		Result = 0
		Result = self.Value1 + self.Value2
		return Result
	
	def Subtraction(self):
		Result = 0
		Result = self.Value1 - self.Value2
		return Result

	def Multiplication(self):
		Result = 0
		Result = self.Value1 * self.Value2
		return Result

	def Division(self):
		Result = 0
		Result = self.Value1 / self.Value2
		return Result

def main():

	Obj_Arithmetic = Arithmetic()

	Obj_Arithmetic.Accept()

	print("Result : ")
	Add = Obj_Arithmetic.Addition()
	print("Addition is       : ",Add)

	Sub = Obj_Arithmetic.Subtraction()
	print("Subtraction is    : ",Sub)
	
	Mul = Obj_Arithmetic.Multiplication()
	print("Multiplication is : ",Mul)

	Div = Obj_Arithmetic.Division()
	print("Division is       : ",Div)

if __name__ == "__main__":

	main()


############################################################
#	
#	Input  : Enter first value  : 20
#			 Enter secind value : 10
#	
#	Output :
#			Addition is       :  30
#			Subtraction is    :  10
#			Multiplication is :  200
#			Division is       :  2.0
#
#############################################################