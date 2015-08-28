#checks for overlap in address spaces
from netaddr import IPNetwork
import ipaddr
from filefunction import write_to_file
file=open("input_list.txt")
inputtxt=file.read()
#print inputtxt
list2=inputtxt.split('\n')
list2.pop()

def addressoverlap():
	for i in range(0, len(list2)):
		for j in range (1, len(list2)):
			if i==j:
				continue
			n1 = ipaddr.IPNetwork(list2[i])
			n2 = ipaddr.IPNetwork(list2[j])
			s = n1.overlaps(n2)
			if s:
				v=n1,"overlaps",n2
				write_to_file("AddrOverlap.txt",str(v))
