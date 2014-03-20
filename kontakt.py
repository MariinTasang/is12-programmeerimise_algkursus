#!/usr/bin/env python
# -*- coding: utf-8 -*-

kontaktid = {}
kontaktid_maxid = 1

class Kontakt:
	
	#def __init__(self):
		#self.id = "1"
		#self.nr= raw_input("Telefoni number: ") 
		#self.omanik = raw_input("Inimese ID: ")
	
	def save(self):
		if self.id == 0:
			self.id = kontaktid_maxid
		voti = self.id
		vaartus = {"number": self.nr, "omanik": self.omanik}
		kontaktid[voti] = vaartus
		
	def id_get(self):
		return self.id
		
	def number_get(self):
		return self.nr
	
	def omanik_get(self):
		return self.omanik
		
	def number_set(self, number):
		self.nr = number
	
	def omanik_set(self, omanik):
		self.omanik = omanik
		

class Inimene:
	
	#def __init__(self):
		#self.id = "1"
		#self.nimi = raw_input("Inimese nimi: ")
		
	def id_get(self):
		return self.id
		
	def nimi_get(self):
		return self.nimi
		
	def nimi_set(self, nimi):
		self.nimi = name
	
		
obj1 = Kontakt()
obj2 = Inimene()

print "ID" + obj2.id_get() + ": " + "Inimesele nimega " + obj2.name_get() + " " + "vastab number " +  obj1.number_get()

#print obj1.id_get()
#print obj2.id_get()

#print obj1.omanik_get()

