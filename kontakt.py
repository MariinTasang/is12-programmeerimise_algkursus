#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

kontaktid = {}
kontaktid_maxid = 1

inimesed = {}
inimesed_maxid = 1

class Kontakt:
	
	def __init__(self):
		self.id = 0
		
	def save(self):
		global kontaktid_maxid
		global kontaktid
		if self.id == 0:
			self.id = kontaktid_maxid 
			kontaktid_maxid = kontaktid_maxid +1
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
		
	def load(self, id):
		if self.id != 0:
			print "Kontakt load error1"
			sys.exit(1)
		if not id in kontaktid:
			print "Kontakt load error2"
			sys.exit(1)
			
		self.id = id
		self.nr = kontaktid[id]["number"]
		self.omanik = kontaktid[id]["omanik"]		
			
class Inimene:
	
	def __init__(self):
		self.id = 0
		
	def save(self):
		global inimesed_maxid
		global inimesed
		if self.id == 0:
			self.id = inimesed_maxid
			inimesed_maxid = inimesed_maxid +1
		voti = self.id
		vaartus = {"nimi": self.nimi}
		inimesed[voti] = vaartus
		
	def id_get(self):
		return self.id
		
	def nimi_get(self):
		return self.nimi
		
	def nimi_set(self, nimi):
		self.nimi = nimi
		
	def load(self, id):
		if self.id != 0:
			print "Inimesed load error1"
			sys.exit(1)
		if not id in inimesed:
			print "Inimesed load error2"
			sys.exit(1)
		
		self.id = id
		self.nimi = inimesed[id]["nimi"]
	
		
obj1 = Kontakt()
obj1.number_set("34546462")
obj1.omanik_set(3)

obj1.save()


obj2 = Kontakt()
obj2.load(1)

#print kontaktid

obj3 = Inimene()
obj3.nimi_set("Mariin")

obj3.save()

obj4 = Inimene()
obj4.load(1)


#print inimesed
