import sys
import time

def kursor(x, y, tekst):
	sys.stdout.write( "\033 [" +str(y)+";"+str(x)+"H"+tekst
sys.stdout.write ("\033[2J")

def kast(x, y, w, h):
	n = 1
	m = 1
	
	while m <= h:
		kursor(x+m, y, "#")
		kursor(x+w, y+m, "#")
		m = m +1
		
		while n <= w:
			kursor(x+n, y+h, "#")
			kursor(x+y, y, "#")
			n = n +1

kast (4, 5, 5, 4)

sys.stdout.flush()
time.sleep(30)

"""
1 kursor - ylemine kylg ja ylemine vasak nurk
2 kursor - parem kylg ja ylemine parem nurk
3 kursor - valumine kylg ja alumine vasak nurk
4 kursor - .... ja alumine parem nurk
"""
