from random import randint

klass= ["Art", "Janis", "Egert", "Kerto", "Eveli", "Jasper", "Mario", "Kairo", "Ardo", "Janar", "Katerin", "Rait", "Aulis", "Mariin", "Timo", "Aleks", "Aigar", "Arti" ]

for i in xrange(100):

	n= randint (0, len(klass)-1)

	element= klass[n]
	del klass[n]

	klass= klass+[element]

	print klass
