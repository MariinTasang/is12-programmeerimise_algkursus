from random import randint

kuulid = ["s"]*3 + ["m"]*5 + ["v"]*3
print kuulid

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

	kuulid= kuulid+[kuul1]+[kuul2]

print kuulid
