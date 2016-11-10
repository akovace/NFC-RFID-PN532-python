import threading
import subprocess
import json
import os
import requests
from requests.auth import HTTPBasicAuth

def nfcuid():
	threading.Timer(1.0, nfcuid).start()
	string1 = eb_to_list() 
	if(string1[2][0] == "R"): 
		jsonfile = list_to_json(string1)
		if(len(jsonfile) == 19):
			os.system('aplay futurebeep3.wav')	
			try:
				response = sent_json_rest(jsonfile) 
				if(response[0] == 200):
					os.system('aplay accessgranted2.wav')
					print response
				else: 
					os.system('aplay accessdeniedfemale.wav')
			except:
				print "nema interneta"
				os.system('aplay modem.wav')
			
				
		else:
			os.system('aplay bleep_04.wav')
	      	

	return

def eb_to_list():
	p = subprocess.Popen(["nfc-mfsetuid"], stdout=subprocess.PIPE)
	output, err = p.communicate()
	string = json.dumps(output)
	lines = string.replace('"', "") 
	lines1 = lines.replace("\\n ", "  y")
	lines2 = lines1.replace("\\n", "  y")
	splitt = lines2.split("  y") 
	string1 = splitt
	return(string1)

def list_to_json(string1):
	dct = {}
   	dct["UID"] = string1[9].split(": ")[1]
   	jsonfile = json.dumps(dct)
	return(jsonfile)
	
def sent_json_rest(json):
	r = requests.post("https://private-44125-nfcapi.apiary-mock.com/login", data=json)
	# r = requests.get('http://recent.cekomat.com/api/users/5', auth=HTTPBasicAuth('masimo.orbanic', '123'), data=json)
	return(r.status_code, r.json())


nfcuid()
