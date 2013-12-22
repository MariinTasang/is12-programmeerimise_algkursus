# ruudud

def CNC(x, y, w, h):
	
	print "G XY GOTO " + str(x) + " " +str(y)
	print "G Z ON"
	print "G X MOVE " +str(w)
	print "G Y MOVE " +str(h)
	print "G X MOVE " +str(-w)
	print "G Y MOVE " +str(-h)
	print "G Z OFF "
	
#CNC(10, 20, 20, 10)

#print ""

# CNC(40, 20, 20, 10)

print ""

Xmax = 1000
x = 10

while x+10+30 < Xmax :
	CNC (x, 20, 20, 10)
	print ""
	x = x+30
	
# kolmurgad

def CNC(x, y, w, h):
	
	print "G XY GOTO " + str(x) + " " +str(y)
	print "G Z ON"
	print "G XY MOVE " +str(w) + " " +str(h)
	print "G X MOVE " +str(-w)
	print "G Y MOVE " +str(-h)
	print "G Z OFF "
	
#CNC(10, 20, 20, 10)
	
print ""

Xmax = 1000
x = 10

while x+10+30 < Xmax :
	CNC (x, 20, 20, 10)
	print ""
	x = x+30	
