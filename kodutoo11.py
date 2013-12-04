import math

# h n2itab seda mitu seda graafikut 
# tuleb y n2itab korgus
h = 17.00
y = 0.00

# tsykkel k2ib kuni korgus on
# vordne graafiku arvuga
 
while y <= h:
	
# x n2itab laiust
	x = 0
	
# tsykkel k2ib kuni laius
# on vordne sin(y) vaartusega

	while x <= math.sin(y):
		
# kui sin(y) vaartus on vaiksem
# voi vordne 0-ga siis laiuse vaartus l2heb 
# 0.09 vorra suuremaks
		if math.sin(y)<=0:
			x=x+0.09
# kui sin(y) vaartus on suurem kui 0
# siis kuvatakse # ja laius vaartus
# laheb 0.09 vorra suuremaks
		else:
			print "#",
			x=x+0.09
# kui sin(y)on vaiksem voi vordne 0-ga
# siis korgus laheb 0.09 vorra suuremaks
	if math.sin(y)<=0:
		y = y+0.09
# kui sin(y) on suurem kui 0
# siis valjastatakse uus rida ja korgus laheb 
# 0.09 vorra suuremaks 	
	else:
		print 
		y = y+0.09
