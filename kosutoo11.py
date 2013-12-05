# opetaja versioon

import math

h = 26

y =0

while y<h:
	rad = 2.0 * math.pi * y / h
	w = math.sin(rad)
	w = 1.0 + w
	w = w/ 2.0
	w = w * 80.0
	w = int(w)
	
	print "#" * w
	
	y=y+1
