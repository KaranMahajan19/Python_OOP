##################################################################
#
#	Class variable    : NoOfBooks
#	Instance variable : Name, Author
#	Instance method   : Display(),
#
###################################################################

class BookStore:

	NoOfBooks = 0

	def __init__(self):
		self.Name = ""
		self.Author = ""
		BookStore.NoOfBooks += 1

	def Display(self):
		self.Name = input("Enter Book name : ")
		self.Author = input("Enter Author name : ")

		print(self.Name,"by", self.Author,".","No of books :",self.NoOfBooks)

def main():
	Obj1 = BookStore()
	Obj1.Display()
	print()
	Obj2 = BookStore()
	Obj2.Display()

if __name__=="__main__":
	main()


##################################################################
#
#	Input : Enter Book name : Linux System Programming
#		  :	Enter Author name : Robert Love
#	Output:	Linux System Programming by Robert Love . No of books : 1
#			
#	Input :	Enter Book name : C Programming
#		  : Enter Author name : Dennis Ritchie
#	Output: C Programming by Dennis Ritchie . No of books : 2
#
##################################################################