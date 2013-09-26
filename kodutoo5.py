from random import randint

klass= ["Art", "Janis", "Egert", "Kerto", "Eveli", "Jasper", "Mario", "Kairo", "Ardo", "Janar", "Katerin", "Rait", "Aulis", "Mariin", "Timo", "Aleks", "Aigar", "Arti" ]
# print klass
# print len(klass)

min= 0
max= len(klass)-1
n= randint (min,max)

element= klass[n]
del klass[n]
# print klass

klass= klass+[element]

print klass
