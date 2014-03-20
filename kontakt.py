#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Kontakt:
	
	def __init__(self):
		self.telefoni_id = "1"
		self.telefoni_nr= raw_input("Telefoni number: ") 
		self.omanik = raw_input("Inimese ID: ")
		
	def id_get(self):
		return self.telefoni_id
		
	def number_get(self):
		return self.telefoni_nr
	
	def omanik_get(self):
		return self.omanik
		

class Inimene:
	
	def __init__(self):
		self.inimese_id = "1"
		self.inimese_nimi = raw_input("Inimese nimi: ")
		
	def id_get(self):
		return self.inimese_id
		
	def name_get(self):
		return self.inimese_nimi
	
		
obj1 = Kontakt()
obj2 = Inimene()

print "ID" + obj2.id_get() + ": " + "Inimesele nimega " + obj2.name_get() + " " + "vastab number " +  obj1.number_get()

#print obj1.id_get()
#print obj2.id_get()

#print obj1.omanik_get()

