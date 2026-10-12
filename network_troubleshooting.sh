#!/bin/bash

echo "Networking Troubleshooting for Ubuntu And CentOS"

echo "1. Ubuntu"
echo "2. CentOS"


read -p "Please select your server press 1 or 2:"  server  #ask user to select Ubuntu or CentOS



if [ "$server" = "1" ]; then      #if user selects 1 run the ubuntu commands
	echo "You selected Ubuntu"

#Shows Ubuntu troubleshooting commmands
echo "1.----Check Internet Connection----"
	echo "ping  8.8.8.8"



echo "2.----Check DNS ----"
	echo "ping www.google.com"



echo "3.----Check ip address and network interfaces----"
	echo "ip addr"
	echo "ip link"



echo "4.----Check nslookup----"
	echo "nslookup amazon.com"



echo "5.----Check routing table----"
	echo "ip route"



echo "6.----Check Traceroute----"
	echo "traceroute amazon.com"



echo "7. ----Check static IP configuration----"
	echo "ls /etc/netplan/99-static-ip.yaml"



elif [ "$server" = "2" ]; then  #if user select 2 run CentOS command 
	echo "You have selected CentOS"
#shows CentOS Troubleshooting commands


echo "1.----Check Internet Connection----"
	echo "ping 8.8.8.8"



echo "2.----Check DNS----"
	echo "ping www.amazon.com"


echo "3.----Check IP adress and Network Interface"
	echo "ip addr"
	echo "ip link"


echo "4.----Check nslookup----"
	echo "nslookup amazon.com"


echo "5.---Check routing table----"
	echo "ip route"


echo "6.----Check Traceroute----"
	echo "traceroute 8.8.8.8"


echo "7.----Check static IP Configuration"
	echo "ip addr show enp0s8"


fi  #the end 
