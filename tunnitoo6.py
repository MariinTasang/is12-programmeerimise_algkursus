from random import randint

kuulid = ["s"]*3 + ["m"]*5 + ["v"]*3
# print kuulid

erinevad= 0
korrad= 0

for i in xrange (100):
	
	min=0
	max= len(kuulid)-1
	n= randint(min, max)
	kuul1=kuulid[n]
	del kuulid[n]

	min=0
	max= len(kuulid)-1
	n= randint(min, max)
	kuul2=kuulid[n]
	del kuulid[n]
	
	if kuul1==kuul2:
		erinevad=erinevad+1
	korrad = korrad+1

	kuulid= kuulid+[kuul1]+[kuul2]

# print kuulid

print 100*erinevad/korrad

if 1+1 ==2:
	print "true"
	
	
nimi= "Aigar"
if nimi == "Timo":
	print "False"
	

kuul1="s"
kuul2="m"
if kuul1!=kuul2:
	print "erinevad"

