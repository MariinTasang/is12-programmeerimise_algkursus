w=10
h=10

y=1

while y<=h:
	x=1
	while x<=w:
		if (x+y) % 2 == 0:
			print "m",
		else:
			print "",
		x=x+1
	
	print
	y=y+1
