#!/usr/bin/env python
# -*- coding: utf-8 -*-

print ""

klassinimekiri = {0: {"eesnimi": "Mariin", "perenimi": "Tasang", "kursus": "IS12"}}

print "Klassinimekiri_alg: "
print klassinimekiri

print ""
	
print "Valikud: "
valik = {
	'Lisa':'add', 
	'Eemalda':'rm', 
	'Kuva' :'ls', 
	'Katkesta' :'q',
	'Muuda' : 'edit'
}

print valik

while True:
	
	Valik = raw_input("Tegevuse valik: ")

	def Kuva():
		if Valik == "ls":
						
			for loe in klassinimekiri:
				print str(loe),klassinimekiri[loe]
			
	Kuva()
	
	def Muuda():
		if Valik == "edit":
			kirje = int(raw_input("Rea_number: "))
			voti = raw_input("Kas - eesnimi perenimi kursus: ")
			vaartus = raw_input("Uus vaartus: ")
			
			klassinimekiri[kirje][voti.lower()] = vaartus

	Muuda()

	def Eemalda():
		if Valik == "rm":
			kirje = int(raw_input("NUMBER: "))
			del klassinimekiri [kirje]
			
		print ""
			
	Eemalda()

	def Lisa():
		if Valik == "add":
			eesnimi=raw_input("Eesnimi: ")
			perenimi=raw_input("Perenimi: ")
			kursus=raw_input("Kursus: ")

			if len(klassinimekiri):
				sissekanne = sorted(klassinimekiri.keys())[-1]+1
			else:
				sissekanne = 0

			klassinimekiri[sissekanne] = {'eesnimi': eesnimi, 'perenimi':perenimi, 'kursus': kursus}
			
	Lisa()
	 
	def End(): 
		if Valik == "q":
			print "Head aega"	
			print exit()
	End()

	print ""


			
	







