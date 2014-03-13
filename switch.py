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
	
	def __init__(self, inputs):
		self.inputs = inputs
	
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
	
	def __init__(self, inputs):
		self.inputs = inputs
	
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
		
sw1 = Switch(False)
sw2 = Switch(False)
sw4 = Switch(True)
sw3 = Switch(False)

not1 = Not(sw4)
not2 = Not(sw3)
not3 = Not(sw2)
not4 = Not(sw1)
not5 = Not(sw3)
not6 = Not(sw4)

and1 = And([sw2, not1])
and2 = And([sw1, sw3])
and3 = And([sw2, not2])
and4 = And([not3, sw3, sw4])
and5 = And([not4, not5, not6])

or1 = Or([and1, and2, and3, and4, and5])
print or1.state_get()

