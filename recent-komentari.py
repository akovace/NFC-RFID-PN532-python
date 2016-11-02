import threading
import subprocess
import json
import os
import requests

def nfcuid():
	threading.Timer(1.0, nfcuid).start() # Timer koji okida funkciju svake 1 sekunde
	string1 = eb_to_list() # Funkcija za dohvacanje podataka iz os-a i njihovo pretvaranje u listu

	if(string1[2][0] == "R"): # Ako lista sadrzi trazeni podatak
		jsonfile = list_to_json(string1) # U listi nadi trzeni podatak i pretvori u json
		if(len(jsonfile) == 19): # Trazeni podatak treba imati 19 znakova
			os.system('aplay futurebeep3.wav') # zvuk za dohvacanje podataka s xice	
			try:
				response = sent_json_rest(jsonfile) # podatak saljemo na rest 
				if(response[0] == 200): # potvrdan odgovor
					os.system('aplay accessgranted2.wav') #potvrdan zvuk
					print response
				else: 
					os.system('aplay accessdeniedfemale.wav') #Osobe nema u sustavu
			except:
				print "nema interneta"
				os.system('aplay modem.wav')
			
				
		else:
			os.system('aplay bleep_04.wav') #nisu stigli svi podaci s xice
	      	

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
	return(r.status_code, r.json())


nfcuid() # Poziv glavne funkcije
