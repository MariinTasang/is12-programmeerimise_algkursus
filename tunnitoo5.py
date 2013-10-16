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


kuulid = ["s"]*3 + ["m"]*5 + ["v"]*3
min=0
max= len(kuulid)-1
n = randint (min,max)
kuul1= kuulid[n]
print kuul1
del kuulid[n]

min=0
max= len(kuulid)-1
n = randint (min,max)
kuul2= kuulid[n]
print kuul2
del kuulid[n]

