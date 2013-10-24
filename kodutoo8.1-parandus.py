# lahendab ruutvorrandi, tulemusena 
# tagastab 2-arvulise massiivi

def rootvorrand1(a, b, c):
	return ((-b)+((b**2)-(4*a*c))**0.5)/(2*a)
print "x1= " + str(rootvorrand1 (5, 9, -2))

def rootvorrand2(a, b, c):
	return (-b)-(((b**2)-(4*a*c))**0.5)/(2*a)
print "x2= " +str(rootvorrand2 (5, 9, -2)) 

# arvutab v2lja 2 arvu keskmise

print ""

n=5
def keskmine(a, b, c, d, e):
	return (a+b+c+d+e)/n
print keskmine (3, 5, 6, 10, 11)

# arvutab fibonacci jada

print ""

def jada (a, b, c, d):
	return (a+b),(b+c),(c+d)
print jada (0, 1, 2, 3)


