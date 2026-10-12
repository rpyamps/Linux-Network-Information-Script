#/usr/bin/env python3

import subprocess #runs linux command
import datetime #gets current date

today=datetime.datetime.now() #gets cuurent day
todaydate=today.strftime("%Y-%m-%d") #date formart year,month,day

system_information=subprocess.check_output(["uname", "-a"]) #shows centOs system and kernel inf
print(system_information.decode())

check_hostname=subprocess.check_output(["hostname"]) #shows the hostname of the server
print(check_hostname.decode())


check_ip=subprocess.check_output(["ip","addr"]) #shows the ip address and network interfaces
print(check_ip.decode())


check_router=subprocess.check_output(["route"]) #shows routing table and default gateway.
print(check_router.decode())


check_dns=subprocess.check_output(["cat", "/etc/resolv.conf"]) #shows DNS servers
print(check_dns.decode())

#saves the network inf to a text file in the Network Reports folder.
with open(f"/home/rosanyelis/Network_Reports/network_inf_Rosanyelis_Payamps_{todaydate}.txt","w") as file:
	file.write(system_information.decode())
	file.write(check_hostname.decode())
	file.write(check_ip.decode())
	file.write(check_router.decode())
	file.write(check_dns.decode())
