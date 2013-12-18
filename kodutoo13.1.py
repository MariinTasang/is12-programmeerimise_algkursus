import sys
import time

def kursor(x, y, tekst):
	

	sys.stdout.write( "\033["+str(y) + ";" +str(x) + "H" + tekst)

sys.stdout.write( "\033[2J")

def kast(x, y, w, h):
	
	m = 1
	kursor(x, y, "#" *w)
	kursor(x y+h, "#" *w)

	while m <= h:
		kursor(x, y+m, "#")
		kursor(x+w, y+m, "#")
		m = m+1

kast (5, 5, 5, 5)

sys.stdout.flush()
time.sleep(30)

"""
1 kursor - ylemine kylg ja ylemine vasak nurk
2 kursor - parem kylg ja ylemine parem nurk
3 kursor - valumine kylg ja alumine vasak nurk
4 kursor - .... ja alumine parem nurk
"""
