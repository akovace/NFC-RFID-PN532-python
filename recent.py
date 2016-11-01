import threading
import subprocess
import json
import os
import requests

def nfcuid():
	threading.Timer(1.0, nfcuid).start()
	p = subprocess.Popen(["nfc-mfsetuid"], stdout=subprocess.PIPE)
	output, err = p.communicate()
	string = json.dumps(output)
	lines = string.replace('"', "") 
	lines1 = lines.replace("\\n ", "  y")
	lines2 = lines1.replace("\\n", "  y")
	splitt = lines2.split("  y") 
	string1 = splitt

	if(string1[2][0] == "R"):
	        dct = {}
        	dct["UID"] = string1[9].split(": ")[1]
        	jsonfile = json.dumps(dct)
		
		if(len(jsonfile) == 19):
			os.system('aplay futurebeep3.wav')			
			response = sent_json_rest(jsonfile)
			print response
		

			if(response[0] == 200):
				os.system('aplay accessgranted2.wav')

		else:
			os.system('aplay bleep_04.wav')
        	

	return


def sent_json_rest(json):
	r = requests.post("https://private-44125-nfcapi.apiary-mock.com/login", data=json)
	return(r.status_code, r.json())


nfcuid()
