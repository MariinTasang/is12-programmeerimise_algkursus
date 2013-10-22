x=0
while x<10:
	for x in xrange(99):
			print "{0:02}".format(x),
			if x%10==9:
				print ""
			x=x+1
print x
