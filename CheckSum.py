import os
from sys import * 
import hashlib

def hashfile(Dir_Name,blocksize = 1024):
	fd = open(Dir_Name,'rb')
	hasher = hashlib.md5()
	buff = fd.read(blocksize)

	while len(buff) > 0:
		hasher.update(buff)
		buff = fd.read(blocksize)

	fd.close()

	return hasher.hexdigest()

def DisplayCheckSum(Dir_Name):

					# asel tr -> exists
	flag = os.path.isabs(Dir_Name)
	# nasel tr
	if flag == False:		# convert
		Dir_Name = os.path.abspath(Dir_Name)
	exists = os.path.isdir(Dir_Name)
	
	dups = {}
	if exists:
		for (dirName,subdirs,fileList) in os.walk(Dir_Name):
			print("Current folder is : "+dirName)
			for filen in fileList:
				Dir_Name = os.path.join(dirName, filen)
				file_hash = hashfile(Dir_Name)					# call -> hashfile()
				print(Dir_Name)
				print(file_hash)
				print("	")
			
	else:
		print("Invalid directory")

def PrintDuplicate(dupFile):
	results = list(filter(lambda x : len(x) > 1, dupFile.values()))

	if len(results) > 0:
		print("Duplicates Found")
		print("The following files are identical.")

		iCnt = 0
		for result in results:
			for subresult in result:
				iCnt += 1
				if iCnt >= 2:
					print('\t\t%s' % subresult)
	else:
		print("No duplicates files found.")

def main():
	print("Application name : "+argv[0])

	if(len(argv) != 2):
		print("Error : Invalid number of arguments.")
		exit()

	if(argv[1] == "-h"):
		print("This script will travel the directory and display the names of all entries")
		exit()

	if(argv[1] == "-u"):
		print("Usage : Application_Name Directory_Name")
		exit()

	try:
		arr = DisplayCheckSum(argv[1])

	except ValueError:
		print("Error : Invalid datatype of inuput.")

	except Exception as E:
		print("Error : Invalid input",E)

if(__name__=="__main__"):
	main()