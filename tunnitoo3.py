print "Kaal: {0} {1}" .format(11, "kg")
print "Kaal: {0} {1}" .format(1+2/3*4, "kg")

kaal =1+2
print "Kaal: {0} {1}" .format(kaal, "kg")

P=0.08
p= 1-P
print p

S=5.0
M=10.0
V=15.0
summa= S+M+V
pa= M/summa
print pa


S=5.0
M=10.0
V=15.0
summa= S+M+V
summa1= S+V
pb= summa1/summa
print pb


S=5.0
M=10.0
V=15.0
summa= S+M+V
pc1= V/summa
pc2= (V-1)/(summa-1)
pc= pc1*pc2
print pc

S=5.0
M=10.0
V=15.0
summa= S+M+V
pd1= S/summa
pd2= M/(summa-1)
pd= pd1*pd2
print pd

S=5
print "{:f}" .format(S)


S=5.0
M=10.0
V=15.0
summa= S+M+V
summa2= summa-1
pe1=S/summa
pe2=M/summa2
pe3=V/summa2
pe4=M/summa
pe=(pe1*pe2)+(pe1*pe3)+(pe4*pe3)
print pe






