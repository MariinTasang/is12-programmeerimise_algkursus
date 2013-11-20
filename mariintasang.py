import math

arv = raw_input(" Siia kirjuta komaarv: ")
arv = float(arv)

print arv**0.5
print math.cos(arv)
print math.sin(arv)
print "{:.2}".format(((arv+1)/(arv-1))**(1.0/3))

tehe = ((arv+1)/(arv-1))**(1.0/3)
if 1 <= tehe and tehe<=2:
	print "ok"
	
# Esimene ülessanne:

tekst1 = raw_input(" Tekst1 kirjuta siia: ")
tekst2 = raw_input(" Tekst2 kirjuta siia: ")

if "tekst1".find("tekst2"):
	print " Tekst1 sisaldub tekst2-s"
else:
	print " Tekst1 ei sisaldu tekst2-s"

tekst3 = tekst1 + " " + tekst2

print tekst3.upper().center(80, " ")
