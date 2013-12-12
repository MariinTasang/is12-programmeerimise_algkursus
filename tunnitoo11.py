"""
funktsioon mis viib teksti-kursori
soovitud koordinaatidele x, y ja
trykib sinna etteantud teksit.
"""

def kursor(x, y, tekst):
	

	print "\033["+str(y) + ";" +str(x) + "H" + tekst

print "\033[2J"

kursor (5, 10, "Tere")

print ""

