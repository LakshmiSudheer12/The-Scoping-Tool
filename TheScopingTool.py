#Takes an input file and outputs 5 files 
#1. Ip_list.txt : List of Ip Addresses
#2. Whois and non client whois domain information
#3: Total number of hosts
#4: Adress Space overlap
from netaddr import IPNetwork
from filefunction import write_to_file
from filefunction import cmdline
from CheckAddressOverlap import addressoverlap
import os
total = 0
client_name = raw_input('Enter client name: ')

file = open("input_list.txt")

while 1:
	line = file.readline()
	if not line:
		break
	else:
		count = 0
		for ip in IPNetwork(line):
			z = str(ip)
			write_to_file("IP_list.txt", z )
			count = count + 1

		ip_who = line.split('/')
		ip2 = "whois " + ip_who[0]
		s = cmdline(ip2)
		if client_name.lower() in s.lower():
			write_to_file("Whois_Info.txt", s )
		else:
			write_to_file("Non_Client_Whois_Info.txt", s )
		hostst = str(line) + " : " + str(count)
		write_to_file("Hosts_total.txt", hostst)
		total = total + count

total_to_file = "Total Hosts: " + str(total)
write_to_file("Hosts_total.txt", total_to_file)
addressoverlap()