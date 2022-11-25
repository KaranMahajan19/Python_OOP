
import os
from sys import * 
import hashlib
import time

def hashfile(Dir_Name,blocksize = 1024):
	fd = open(Dir_Name,'rb')
	hasher = hashlib.md5()
	buff = fd.read(blocksize)

	while len(buff) > 0:
		hasher.update(buff)
		buff = fd.read(blocksize)

	fd.close()

	return hasher.hexdigest()

def FindDuplicate(Dir_Name):

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
				
				if file_hash in dups:
					dups[file_hash].append(Dir_Name)
				else:
					dups[file_hash] = [Dir_Name]
		return dups
			
	else:
		print("Invalid directory")

def PrintResult(Arr):
	#						Condition to perform   # list
	results = list(filter(lambda x : len(x) > 1, Arr.values()))

	if len(results) > 0:
		print("Duplicates Found")
		print("The following files are identical.")

		for result in results:
			for subresult in result:
					print('\t\t%s' % subresult)
	else:
		print("No duplicates files found.")

def DeleteFiles(Arr):
	results = list(filter(lambda x : len(x) > 1, Arr.values()))

	iCnt = 0
	if len(results) > 0:
		
		for result in results:
			for subresult in result:
				iCnt += 1
				if iCnt >= 2:
					os.remove(subresult)
			iCnt = 0
		
	else:
		print("No duplicates file found.")

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
		arr = {}
		Start_Time = time.time()
		arr = FindDuplicate(argv[1])
		PrintResult(arr)
		DeleteFiles(arr)
		End_Time = time.time()	

		print("Took %s seconds to execute."% (End_Time - Start_Time))
	except ValueError:
		print("Error : Invalid datatype of inuput.")
	except Exception as E:
		print("Error : Invalid input",E)
if(__name__=="__main__"):
	main()