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
		if len(self.inputs)==0:
			return False
		for i in self.inputs:
			if i.state_get() == False:
				return False
			
		return True
		
		
class Or:
	
	def __init__(self):
		self.inputs = []	
	
	def input_add(self, x):
		self.inputs.append(x)
		
	def state_get(self):
		if len(self.inputs)==0:
			return False
		for i in self.inputs:
			if i.state_get() == True:
				return True
			
		return False

class Not:
	def __init__(self, obj):
		self.input = obj
		
	def state_get(self):	
		return not self.input.state_get()
		
sw1 = Switch(True)
sw2 = Switch(False)
#print obj1.state_get()

obj2 = Or()
obj2.input_add(sw1)
obj2.input_add(sw2)

obj3 = Not(sw2)
print obj3.state_get()
