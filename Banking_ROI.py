

#	Instance variable : Name, Amount, Address, AccountNo
#	Instance method   : CreateAccount(), DisplayAccountInfo()
#	Class variable 	  : Bank_Name, ROI_On_FD
# 	Class method      : DisplayBankInformation()
#	Static method     : DisplayKYCInfo()

class Bank_Account:

	Bank_Name = "HDFC Bank PVT LTD"
	ROI_On_FD = 6.7						# Rate of Interest

	def __init__(self):					# Constructor
		self.Name = ""
		self.Amount = 0
		self.Address = ""
		self.AccountNo = 0

	def CreateAccount(self):			# like a Accept method
		print("Enter your name : ")
		self.Name = input()			#input : dont typecast cz bydefault str

		print("Enter your Account number : ")
		self.AccountNo = int(input())

		print("Enter your initial amount : ")
		self.Amount = int(input())

		print("Enter your address : ")
		self.Address = input()

	def DisplayAccountInfo(self):
		print("---------Your Account information is as below---------")
		print("Name of Account Holder : ",self.Name)
		print("Account number : ",self.AccountNo)
		print("Current Amount in Acount : ",self.Amount)
		print("Address of Account Holder : ",self.Address)

	@classmethod									# decorator
	def DisplayBankInformation(cls):				# cls : Class method
		print("******Welcome to Banking Console******")
		print()
		print("Name of our bank is : ",cls.Bank_Name)
		print("Rate of Interest we offer on Fixed Deposite is : ",cls.ROI_On_FD,"%")
		
	@staticmethod
	def DisplayKYCInfo():			# () empty,classmethod means static 
		print("Please consider below KYC Information")
		print("According to the rules of Gov.India you have to sub,ite below documents")
		print("1. Clear and recent passport size photo")
		print("2. Photo of Aadhar card")
		print("3. Photo of PAN card")

	def Deposite(self,Value):
        self.Amount = self.Amount + Value

    def Withdraw(self,Value):
        self.Amount = self.Amount - Value

def main():

	Bank_Account.DisplayKYCInfo()
	
	print()
	print("Name of Bank : ",Bank_Account.Bank_Name)
	print("Rate of Interst on Fixed Deposite : ",Bank_Account.ROI_On_FD,"%")

	print()
	Bank_Account.DisplayBankInformation()
	print()
	User1 = Bank_Account()			# obj creation
	User2 = Bank_Account()

	print("------Account Creation------")
	print("Creating the first Account__")
	User1.CreateAccount()			# obj calling
	
	print()
	print("Creating the second Account__")
	User2.CreateAccount()

	print()
#   objname.Methodname()
	User1.DisplayAccountInfo()
	print()
	User2.DisplayAccountInfo()

	print()
	User1.Deposite(500)
	User2.Deposite(1200)
	print("Amount of {} after deposite is {}: ",User1.Amount)
	print("Amount of {} after deposite is {}: ",User2.Amount)

	print()
	User1.Withdraw(200)
	User2.Withdraw(3000)
	print("Amount of {} after deposite is {}: ",User1.Amount)
	print("Amount of {} after deposite is {}: ",User2.Amount)
	
	


if __name__ == "__main__":
	main()