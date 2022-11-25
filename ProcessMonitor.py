from sys import *
import psutil
import time
import os

def ProcessDisplay(log_dir="Automation"):
	listprocess = []

	if not os.path.exists(log_dir):
		try:
			os.mkdir(log_dir)
		except:
			pass

	seperator = "-" * 100
	log_path = os.path.join(log_dir,"AutomationLog%s.log"%(time.strftime("%H%M%S")))
														  # time.time
														  # datetime.datetime
	f = open(log_path,'w')
	f.write(seperator + "\n")
	f.write("Automation Process Logger : "+time.ctime() + "\n")
	f.write(seperator + "\n")

	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid',	'name',	'username'])
			vms = proc.memory_info().vms / (1024 * 1024)
			pinfo['vms'] = vms
			listprocess.append(pinfo)
		except(psutil.NoSuchProcess,AccessDenied,psutil.ZombieProcess):
			pass

	for element in listprocess:
		f.write("%s\n" % element)


def main():

	print("----------------Automation by Karan_Mahajan----------------")

	print("Application name : "+argv[0])

	if(len(argv) != 2):
		print("Error : Invalid numbers of arguments")
		exit()

	if(argv[1] == "-h") or (argv[1] == "-H"):
		print("This script is used log record of running processess")
		exit()

	if(argv[1] == "-u") or (argv[1] == "-U"):
		print("Usage : Application_Name AbsolutePAth_Of_Directory")
		exit()
	
	try:
		ProcessDisplay(argv[1])

	except OSError:
		print("Error : Invalid arguments")
	except ValueError:
		print("Error : Invalid datatype of input")

	except Exception:
		print("Error : Invalid input")


if __name__=="__main__":
	main()

'''
# task: 
	store in csv

'''