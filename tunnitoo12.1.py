
# ruudu valjaloikamine

#kordinadid = (x, y)

x = 10
y = 20

w = 20
h = 10

x1 = 40

print "G XY GOTO " + str(x) + " " +str(y)

#print "G XY GOTO " +str(kordinadid).format(

print "G Z ON"

print "G X MOVE " +str(w)

print "G Y MOVE " +str(h)

print "G X MOVE " +str(-w)

print "G Y MOVE " +str(-h)

print "G Z OFF "

# uus kujund korvale

print "G XY GOTO " + str(x1) + " " +str(y)

print "G Z ON"

print "G X MOVE " +str(w)

print "G Y MOVE " +str(h)

print "G X MOVE " +str(-w)

print "G Y MOVE " +str(-h)

print "G Z OFF "

