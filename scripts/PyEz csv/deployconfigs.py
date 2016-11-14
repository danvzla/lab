#!/usr/bin/env python
# Maruf Yunus 
# Revision history: 
# version 1 : 2015-Jan-03
# This program junos device configs 

import csv,getpass,sys
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import *


def importCsv(csvfile):
	try:
		my_file=open(csvfile)
		csv_data=csv.reader(my_file)
	   	my_list=[row for row in csv_data]	
		my_list.pop(0)
		my_file.close()
		return my_list
	except Exception,err:
		print("ERROR: Encountered exception while importing csv file :%s. Exception is : %s . \n Exiting the program.")%(csvfile,str(err))
		sys.exit(1)

def printProgress(logtype,hostname,message):
	print("%s:%s:%s")%(logtype,hostname,message)

def deployConfig(my_device_list_dict, my_username, my_password, my_config_template_file):
	my_hostname=""	
	try:
		my_hostname=my_device_list_dict["mgmt_ip"]
		printProgress("INFO",my_hostname,"Connecting to device through netconf")	
		dev=Device(my_hostname,user=my_username,password=my_password)
		dev.open()
		dev.timeout=3*60
		cu = Config(dev)	
		printProgress("INFO",my_hostname,"Going to load template the config now.")
		rsp=cu.load(template_path=my_config_template_file,template_vars=my_device_list_dict)
		printProgress("INFO",my_hostname,"Performing diff between active and candidate config.")
		cu.pdiff()
		printProgress("INFO",my_hostname,"Performing commit check")
		if cu.commit_check():
				printProgress("INFO",my_hostname,"commit check was successfull.")
				printProgress("INFO",my_hostname,"performing commit now.")
				commit_status=cu.commit()
				printProgress("INFO",my_hostname,"dsconnecting from device")
				dev.close()
				return commit_status
		else:
			return False
	except Exception,err:
		printProgress("ERROR",my_hostname,"Encountered exception while deploying config")
		printProgress("ERROR",my_hostname,str(err))
		return False
	

def main():
	print("\nWelcome to Junos firewall deployment tool \n")	
	csv_file=raw_input("Enter your csv file path: ")
	csv_file.strip()
	config_template_file=raw_input("Enter your config template file path: ")
	config_template_file.strip()
	username=raw_input("\nEnter your device username: ")
	password=getpass.getpass(prompt="\nEnter your device password: ")
	raw_csv_list=importCsv(csv_file)
	device_list_dict={}
	for i in raw_csv_list:
		device_list_dict["hostname"]=i[0]
		device_list_dict["trust_interface"]=i[1]
		device_list_dict["trust_ip"]=i[2]
		device_list_dict["admin_user"]=i[3]
		device_list_dict["domain"]=i[4]
		device_list_dict["ntp"]=i[5]
		device_list_dict["dns"]=i[6]
		device_list_dict["mgmt_ip"]=i[7]
	    	if deployConfig(device_list_dict,username,password,config_template_file):
			printProgress("INFO",device_list_dict["hostname"],"Successfully deployed config on device. ")	
		else:
			printProgress("ERROR",device_list_dict["hostname"],"Config deployment failed! ")
		print("")
		

if __name__== "__main__":
	main()
