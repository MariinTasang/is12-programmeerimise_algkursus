#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Switch:
	
	def __init__(self, state):
		self.state = state
		
	def on(self):
		self.state=True

	def off(self):
		self.state=False
				
	def state_get(self):
		return self.state
	
class And:
	
	def __init__(self):
		self.inputs = []	
	
	def input_add(self, x):
		self.inputs.append(x)
		
	def state_get(self):
		for i in self.inputs:
			if i == False:
				print "False"
			else:
				print "True"
		return self.inputs
		
obj1 = Switch(True)
print obj1.state_get()

obj2 = And()
obj2.input_add(True)
print obj2.state_get()
