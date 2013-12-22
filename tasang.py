#1 ylesanne

a = "Tere"
b = "Head aega"
c = "Tere tulemast"
d = "Mine minema"

print "a= " +str(a)
print "b= " +str(b)
print "c= " +str(c)
print "d= " +str(d)

print ""

valik = raw_input("Valik: ")

if valik == a:
	print str(a)
elif valik == b:
	print str(b)
elif valik == c:
	print str(c)
elif valik == d:
	print str(d)
else:
	print "Vale valik"
		
# 2 ylesanne

n = 1

while n <= 5 :
	arv = raw_input("Sisesta arv: ")
	arv = int()
	n = n+1

print n


# 4 ylesanne


def joud(q1, q2, r, k):
	arvutus = k * ((q1*q2)/r **2)
	return arvutus
	
print joud (10, 2, 3, 11)
	
