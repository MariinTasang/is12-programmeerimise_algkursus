tekst1 = raw_input("Tekst1 kirjutage siia: ")
tekst2 = raw_input("Tekst2 kirjutage siia: ")
tekst3 = raw_input("Tekst3 kirjutage siia: ")
  
print tekst1.upper() + " " + str(len(tekst2)) + " " + tekst3.lower()


print " "

tekst = raw_input ("Tekst kirjutage siia: ")

if (len(tekst)>4) and tekst.find("a")== True:
	print "Tekst on pikem kui 4 m2rki ja sisaldab a t2hte"
else:
	print "Tekst ei ole pikem kui 4 m2rki ja ei sisalda a t2hte"


print " "

from string import maketrans

t2hed = "aeiou"
vaste = "#####"
teisendus = maketrans(t2hed, vaste)

tekst4 = "abcdefgijõgräbföcdüf"
print tekst4.translate(teisendus) 


