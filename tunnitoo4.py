#!/usr/bin/python

from random import randint

# muutuja = [1, 2, 3, 99]
# print muutuja [3]

# muutuja = ["tere", "headaega", "hello", "kohtumiseni"]
# print muutuja [2]

# a= [1, 2, 3] + [5, 6, 7]
# print a

# a= ["s"]*5
# print a


kuulid = ["s"]*5 + ["m"]*10 + ["v"]*15
print kuulid

print randint (1,3)

print kuulid [0]

print kuulid [randint (0, 29)]

i= randint (0, 29)
print kuulid [i]

for n in xrange (10):
	print n

for n in kuulid:
	print n
