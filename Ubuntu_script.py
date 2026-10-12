#!/usr/bin/env python3

import subprocess #runs linux command
import datetime  #get current date for the filename report
today=datetime.datetime.now()
date=today.strftime("%Y-%m-%d")

system_inf=subprocess.check_output(["uname","-a"]) #shows system and kernel inf.
print(system_inf.decode()) #prints system and kernel

check_hostname=subprocess.check_output(["hostname"]) #shows the hostname of the server.
print(check_hostname.decode()) #print the hostname

check_ip=subprocess.check_output(["ip","addr"]) #shows ip address and network interface 
print(check_ip.decode()) #prints the ip address and interface


check_router=subprocess.check_output(["route"]) #shpws router and gateway information
print(check_router.decode()) #prints the router information.

check_dns=subprocess.check_output(["resolvectl","status"]) #shows the DNS information for the Ubuntu Server
print(check_dns.decode()) #prints the DNS inf.  


with open(f"/home/rpayamps/Network_Reports/network_inf_Rosanyelis_Payamps_{date}.txt", "w") as file: #save the network inf into a text file inside the folder
	file.write(system_inf.decode())
	file.write(check_hostname.decode())
	file.write(check_ip.decode())
	file.write(check_router.decode())
	file.write(check_dns.decode())
