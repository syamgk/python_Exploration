from subprocess import call,check_output
from time import sleep
import random,string,sys
#-------------------------------------------------------------------------------------------------#
def output_lag(content,time):
	sys.stdout.write(content) # print content & blink cursor on same line
	sys.stdout.flush()
	sleep(time)
	if time == 3:print""  # NB: time == 3
def typing(string,time):
	flag = 0
	while flag < len(string):
		output_lag(string[flag],time)
		flag +=1
name = "agent_smith "
machine_name = check_output(["hostname"])[:-1]
q = string.ascii_lowercase+string.printable[:10]+' '
w = random.choice
sys_details = check_output(["lshw","-short"])
print '\x1b[H\x1b[J'
output_lag("login:",1)
typing(name,.1)
output_lag("\nPassword:",3)
call(["cat","/etc/motd"])
output_lag("\n"+name[:-1]+"@"+machine_name+":~$",1)
typing("sudo matrix",.1)
output_lag("\n[sudo] password for "+name[:-1]+":" ,3)
typing("Getting Data\n"+"=="*44+">",.05)
typing(sys_details,.001)
typing("=="*44+">",.05)
typing( '\033[92m'+"Matrix reloaded" ,.4)
n = 0
while n < 105:
	sys.stdout.write(w(q)+" ") 
	n += 1
	if n ==104 : 
		n = 0
		sys.stdout.flush()
		sleep(.2)
