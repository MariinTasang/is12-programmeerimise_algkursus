def faktoriall(n):
	f=1
	i=1 #mitmes kord on
	while i<=n:
		f= f *i
		i= i + 1
	return f

print "5!=" + str(faktoriall(5))
print "7!=" + str(faktoriall(7))
