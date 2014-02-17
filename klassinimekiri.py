# -*- coding: utf-8 -*-

print ""

klassinimekiri = [
["Mariin  Tasang  IS12"],
["Eveli   Kauksi  IS13"],
["Katerin Oroperv IS14"]
]

print "Klassinimekiri:"

print ""

print "Eesnimi" +" "+ "Perenimi" +" "+ "Kursus"

for element in klassinimekiri:
	print element
	
print ""

valik = ["add", "rm", "ls", "q"]

print "Valikud:"

print ""

for element in valik:
	print element
	
print ""
	
Valik = raw_input("Tegevuse valik: ")

print ""

def Kuva():
	if Valik == "ls":
		print "Klassinimekiri:"
		
		print ""
		
		for element in klassinimekiri:
			print element
Kuva()

def Eemalda():
	if Valik == "rm":
		Eemalda = int(raw_input("Mitmes elenent: "))
		kustuta = klassinimekiri.pop (Eemalda)
		
		print ""
		
		for element in klassinimekiri:
			print element
Eemalda()


def Lisa():
	if Valik == "add":
		Lisa = ([raw_input("Eesnimi: "), raw_input("Perenimi: "), raw_input("Kursus: ")])
		kuskirje = klassinimekiri.append(Lisa)
		
		print ""
		
		for element in klassinimekiri:
			print element
Lisa()
 
def End(): 
	if Valik == "q":
		print "Head aega"	
		print exit()
End()


print "Edasine tegevus:"
for element in valik:
	print element
	
