###########################################################################
#	Instance variable : Radius, Area, Circumference
#	Instance method   : Accept(), CalculateArea(), CalculateCircumference(),
#						Display()
#	Class variable    : PI
############################################################################

class Circle:
	
	PI = 3.14

	def __init__(self):
		self.Radius = 0.0
		self.Area = 0
		self.Circumference = 0

	def Accept(self):
		self.Radius = float(input("Enter value of Radius : "))

	def CalculateArea(self):
		self.Area = self.PI * self.Radius * self.Radius

	def CalculateCircumference(self):
		self.Circumference = 2 * self.PI * self.Radius
	
	def Display(self):
		print("Value of Radius is        : ",self.Radius)
		print("Value of Area is          : ",self.Area)
		print("Value of Circumference is : ",self.Circumference)
	

def main():
	Obj_Circle = Circle()

	Obj_Circle.Accept()
	Obj_Circle.CalculateArea()
	Obj_Circle.CalculateCircumference()
	Obj_Circle.Display()

if __name__ == "__main__":

	main()


############################################################
#	
#	Input  : Enter value of Radius : 2.14
#	
#	Output :
#			Value of Radius is        :  2.14
#			Value of Area is          :  14.379944000000002
#			Value of Circumference is :  13.439200000000001
#
#############################################################