from random import randint

print ""
# Esimene ylessanne

a = "Tere tulemast "
b = "Head aega "
c = "Oli tore"
d = "Kohtumiseni"

print "a= " +str(a)
print "b= " +str(b)
print "c= " +str(c)
print "d= " +str(d)

print ""
valik = raw_input ("Sisesta t2ht: ")

print ""

if valik == "a":
	print str(a)
elif valik == "b":
	print str(b)
elif valik == "c":
	print str(c)
elif valik == "d":
	print str(d)
else:
	print "Vigane tekst"

print ""
# Teine ylesanne

n = 5
m = 0

while n >= 1:
	arv = raw_input("Sisesta t2isarv: ")
	n = n-1
	m = m+int(arv)

print ""
print "Arvude summa = " +str(m)

print ""
# Kolmas ylessanne

password = "abc123"

Parool = raw_input ("Sisesta parool: ")

print ""

while True:
	if str(Parool) == password:
		print "Parool oige"
		break
		
	else:
		print "Vale parool - proovi uuesti"
		Parool = raw_input ("Sisesta parool: ")
	
print ""
# Neljas ylessanne

def joud (q1, q2, r):
	k = 1
	F = float(k*((q1*q2) / r**2))
	return F

print joud (6,5,2)

print ""
# Viies ylessanne

q = randint (1,10)
while True:
	arv = raw_input ("Sisesta arva 1...10: ")
	a = int(arv)
	
	if a == q:
		print "ok"
		break
		
	else:
		print "proovi uuesti"
		arv = raw_input ("Sisesta arva 1...10: ")

