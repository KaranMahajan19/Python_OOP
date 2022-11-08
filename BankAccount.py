##################################################################
#
#	Class variable    : ROI
#	Instance variable : Name, Amount
#	Instance method   : Deposit(), Withdraw(), CalculateInterest(), 
#						Display()
#
###################################################################

class BankAccount:

	ROI = 10.5

	def __init__(self):
		self.Name = ""
		self.Amount = 0

		self.Name = input("Enter name : ")

	def Deposit(self):
		self.Amount = int(input("Enter Amount to Deposit : "))

	def Withdraw(self):
		user = int(input("Withdraw amount : "))
		self.Amount = self.Amount - user

	def CalculateInterest(self):
		print("Rate of Interst is :",self.Amount * self.ROI / 100)

	def Display(self):
		print("Account Name is : ",self.Name)
		print("Amount is : ",self.Amount,"Rs")


def main():
	Obj_BankAccount = BankAccount()

	Obj_BankAccount.Deposit()
	Obj_BankAccount.Withdraw()
	Obj_BankAccount.CalculateInterest()
	Obj_BankAccount.Display()

if __name__=="__main__":
	main()


#############################################################
#
#	Input : Enter name : Karan Mahajan
#		  : Enter Amount to Deposit : 500
#		  : Withdraw amount : 200
#		
#	Output:	Rate of Interst is : 31.5
#			Account Name is :  Karan Mahajan
#			Amount is :  300 Rs
#
#############################################################