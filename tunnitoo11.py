import sys
import time

"""
funktsioon mis viib teksti-kursori
soovitud koordinaatidele x, y ja
trykib sinna etteantud teksit.
"""

def kursor(x, y, tekst):
	

	sys.stdout.write( "\033["+str(y) + ";" +str(x) + "H" + tekst)

sys.stdout.write( "\033[2J")

kursor (5, 10, "Tere")

print ""

"""
funktsioon mis valjastab ekraanile
kasti servad.
Funktsiooni parameetrid x, y, w, h
"""

def kast (x, y, w, h):
		
	kursor(x, y, "#")
	kursor(x+w, y, "#")
	 
	kursor(x, y+h, "#")
	kursor(x+y, y+h, "#")
	 

kast (10, 5, 5, 10)

sys.stdout.flush()

time.sleep(60)
