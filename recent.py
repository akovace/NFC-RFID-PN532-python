import threading
import subprocess
import json
import os

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
		os.system('aplay /home/pi/bleep_01.wav')

        	print jsonfile
#        else:
#		print "ne radi"	
	return


nfcuid()
