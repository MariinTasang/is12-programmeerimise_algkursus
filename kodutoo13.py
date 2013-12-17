from random import randint

def taevas(x, y, tekst):
	arv = 0
	
	while arv < 48:
		x = randint(0, 70)
		y = randint(0, 20)
		
		arv = arv +1
		
		sys.stdout.write("\033["+str(y)+";"+str(x)+"H" + txt)
		
taevas (70, 20, "*")
