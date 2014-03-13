#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = 1
b = a
a = 2
print a,b

class Abc:
	value = 1
	
x = Abc()
x.value = 5
y = x
x.value = 0
print x.value, y.value	
