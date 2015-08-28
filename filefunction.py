#Set of functions to perform file operations and derive whois info
from netaddr import IPNetwork
from subprocess import PIPE, Popen
import os 
def write_to_file(file_name, somevalue): 
	ff = open(file_name,'a')
	ff.write(somevalue)
	ff.write('\n') # python will convert \n to os.linesep
	ff.close()
	return None

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]
