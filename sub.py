import os 
import requests



print ('\033[1;31m _   _    _     _   _   _       ')
print ('\033[1;31m| | / /  | |   / / | | | |      ')
print ('\033[1;31m| |/ /   | |  / /  | |_| |      ')
print ('\033[1;31m| |\ \   | | / /   \___  |      ')
print ('\033[1;31m| | \ \  | |/ /        | |      ')
print ('\033[1;31m|_|  \_\ |___/         |_| KV4 ')      
print ('      ') 
print ('facebook ==> Arasmahmoud6') 
print ('Instagram ==> almcompany6') 
print ('Linkedin ==> almcompany') 
print ('Udemy ==> Arasmahmoud\033[1;37m .')
print ("  ")

TAR =input("enter target domains >> ")
print (" ")
TT = int(input("1 for http //// 2 for https >> "))
########## sub.py broutforce subdomains #########
if (TT == 1):
    wlist = open('wlist.txt' , 'r')
    lr = wlist.read()
    content = lr.splitlines()
    for subs in content :
        url = f"http://{subs}.{TAR}/"
        try :
                req = requests.get(url)
                print("[+]FOUND SUB >>>> ", url)
                ws = open('subdomains.txt' , 'a')
                ws.write(url + " \n")
        except requests.ConnectionError :
            pass

    wlist.close()


elif (TT == 2) :
	wlist = open('wlist.txt' , 'r')
lr = wlist.read()
content = lr.splitlines()
for subs in content :
	url = f"https://{subs}.{TAR}/"
	try :
		req = requests.get(url)
		print("[+]FOUND SUB >>>> ", url)
		wwss = open('subdomains.txt' , 'a')
		wwss.write(url + " \n")
	except requests.ConnectionError :
		 pass
	wlist.close()


else :
    print ("!!!! ERROR TRY again !!!! ") 



