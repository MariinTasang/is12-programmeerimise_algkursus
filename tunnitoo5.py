from random import randint

# urn = ["s"]*5
# urn[1]= "s"
# print urn[1]

# klass= ["kairo", "aigar", "timo", "janis", "mario", "aulis", "mariin"]
# print klass
# print len(klass)

# min= 0
# max= len(klass)-1
# n= randint (min,max)
# print klass [n]

# print klass[randint(0, len(klass)-1)]

# print klass
# del klass [2]
# print klass

# klass = ["a", "b", "c", "d", "e"]
# print klass
# n= 2
# element= klass[n]
# del klass[n]
# klass= klass+[element]
# print klass


kuulid = ["s"]*5 + ["m"]*5 + ["v"]*5
# print kuulid
min=0
max=len(kuulid)-1
kuul1 = randint (min,max)
del kuulid[kuul1]
print kuulid

kuul2 = randint (min, max)
del kuulid[kuul2]






