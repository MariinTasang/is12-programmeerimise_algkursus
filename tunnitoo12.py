import sys
import time

def kursor(x, y, tekst):
	

	sys.stdout.write( "\033["+str(y) + ";" +str(x) + "H" + tekst)

sys.stdout.write( "\033[2J")

kursor (5, 10, "tere")

sys.stdout.flush()
time.sleep(60)

# prindib sona tere
# koordinaadi jargi
