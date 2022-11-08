##################################################################
#
#	Instance variable : Value
#	Instance method   : ChkPrime(), ChkPerfect(), Factors(), 
#						SumFactors()
#
###################################################################

class Numbers:

	def __init__(self):
		self.Value = int(input("Enter Number : "))

	def ChkPrime(self):
		Flag = True
		for i in range(2,int(self.Value/2+1)):
			if(self.Value % i == 0):
				Flag = False
				break
		return Flag

	def ChkPerfect(self):

		Perfect = 0
		for i in range(1,int(self.Value)):
			if(self.Value % i == 0):
				Perfect += i
		if(Perfect == self.Value):
			return True
		else:
			return False
		return Perfect

	def Factors(self):
		print("Factors are : ")
		for i in range(1,int(self.Value),1):
			if(self.Value % i == 0):
				print(i,end="  ")
			i += 1
		return i

	def SumFactors(self):
		Sum = 0
		for i in range(1,int(self.Value)+1):
			if(self.Value % i == 0):
				Sum = Sum + i
		return Sum

def main():
	Obj_Numbers = Numbers()

	Ret = Obj_Numbers.ChkPrime()
	if(Ret == True):
		print(Ret,": prime number")
	else:
		print(Ret,": not prime number")

	Ret = Obj_Numbers.ChkPerfect()
	if(Ret == True):
		print(Ret,": perfect number")
	else:
		print(Ret,": not perfect number")
	
	Ret = Obj_Numbers.Factors()
	print(Ret)

	Ret = Obj_Numbers.SumFactors()
	print("Addition of all factors is :",Ret)

if __name__=="__main__":
	main()


#############################################################
#
#	Input : Enter Number : 28
#			
#	Ouput : False : not prime number
#			True : perfect number
#			Factors are :
#			1  2  4  7  14  28
#			Addition of all factors is : 56 
#
#############################################################