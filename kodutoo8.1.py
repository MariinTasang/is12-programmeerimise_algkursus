# arvutab v2lja 2 arvu keskmise

l = [16, 34]
print sum(l) /float(len(l))

print ""

# arvutab fibonacci jada

def fib(n):
	if n==1:
		return 0
	elif n==1:
		return 1
	else:
		return fib(n-1)+fib(n-2)
print fib

# lahendab ruutvorrandi, tulemusena 
# tagastab 2-arvulise massiivi

print ""

import math
a= 5
b= 9
c= -2
d= b**2-4*a*c
if d<0:
	print "lahendid puuduvad"
elif d==0:
	x=(-b+math.sqrt(d))/(2*a)
	print "Yks lahend: ", x
else:
	x1=(-b+math.sqrt(d))/(2*a)
	x2=(-b-math.sqrt(d))/(2*a)
	print "Kaks lahendit: ", x1, " ja", x2



