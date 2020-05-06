#!/usr/bin/python3 
import os,sys,requests,threading
#soru1
print("PID....",os.getpid())


#soru2

platform = sys.platform
if(platform == "linux"):
	print("load avg.... ",os.getloadavg())
	
load_avg = os.getloadavg()
print("cpu_count....",os.cpu_count())

#soru4
array = ["https://api.github.com","http://bilgisayar.mu.edu.tr/","https://www.python.org/","http://akrepnalan.com/ceng2034","https://github.com/caesarsalad/wow"]

def request1(url):
	
	res = requests.get(url)
	res_code = res.status_code
	
	
	if 199 < res_code < 300:
    		print(url+' ====>This url is valid!') 
	elif 399< res_code <600:
    		print(url+' ====>This url is invalid!')
	else:
    		print(url+" ====> we don't know that url is valid or invalid!")
    		
for i in range(0,5):
		
	thread1 = threading.Thread(target=request1, args=(array[i],))
	thread1.start()
		
#soru3
load_avg_5min = load_avg[1]
nproc = os.cpu_count()

if (nproc-load_avg_5min < 1):
	print("script will exit")
	sys.exit()
	




