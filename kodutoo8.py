# if
x = 0
if x < 0: 
#kui x on v2iksem kui 0
	print "negatiivne muudetud nulliks"
elif x == 0: 
#juhul kui x on vordne nulliga
	print "Null"
elif x == 1:
	print "yks"
else: 
# teistel juhtudel
	print "Rohkem"
# vastus on Null sest x on vordne nulliga	

print ""

# for
words = ["kass", "aken", "kotttool"]
for w in words:
	print w, len(w)
# trykib v2lja sonad ja nende pikkuse

print ""

words = ["kass", "aken", "tool"]
for w in words [:]:
	if len(w)>6:
		words.insert (0,w)
print words
# trykib sonad mis on yle 6 t2hem2rgi pikad kaks korda.
# alla 6 t2hem2rgised sonad trykib yhe korra.

print ""

# range ()
print range (15)
# kuvab numbrite vahemiku 0-st 14-ni
print range (5, 17)
# kuvab numbrid vahemikus 5-st 16-ni
print range (0, 10, 3)
# kuvab numbrid 0, 3, 6, 9
print range (-10, -100, -30)
# kuvab numbrid -10, -40, -70

print ""

a = ["Mary", "had", "a", "little", "lamb"]
for i in range (len(a)):
	print i, a[i]
# kuvab sonad koos j2rjekorra nr yksteise all

print ""

# pass statements
# while True:
	#pass
# katkestamiseks ctrl+c
#class MyEmptyClass:
	#pass
#def initlog (*args):
	#pass

print ""

#defining functions
def fib(n):
	a, b = 0, 1
	while a < n:
		print a,
		a, b = b, a+b
fib (2000)

print ""

fib(0)
print fib(0)

print ""

def fib2(n):
	result = []
	a, b = 0,1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result
f100 = fib2(100)
print f100



