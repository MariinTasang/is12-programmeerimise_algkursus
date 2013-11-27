# esimene ylessanne

tekst= raw_input("Siia sisesta tekst: ")

if tekst.islower() and any(x.isdigit() for x in tekst):
	print "v2iket2hed ja numberid"
elif tekst.islower() and any(x.isdigit() for x in tekst)==False:
	print "v2iket2hed ja numbriteta"
	
if tekst.isupper() and any(x.isdigit() for x in tekst):
	print "suuredt2hed ja numberid"
elif tekst.isupper() and any(x.isdigit() for x in tekst)==False:
	print "suuredt2hed ja numbriteta"

if any(x.isupper()for x in tekst)and any(x.islower()for x in tekst) and any(x.isdigit() for x in tekst):
	print "molemad ja numbrid"
elif any(x.isupper()for x in tekst)and any(x.islower()for x in tekst) and any(x.isdigit() for x in tekst)==False:
	print "molemad ja numbriteta"

else: 
	print " "

# teine ylessanne
