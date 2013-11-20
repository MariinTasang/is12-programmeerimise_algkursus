tekst = "tere"

print tekst.upper().center(80)

print tekst.upper().center(len(tekst)*4)

print "<" + ">"
# <>

print ("()" + "()")
# ()()

print ("{}" + "{}").format(tekst.upper(), tekst.lower())
# TEREtere

print ("{} {}").format(tekst.upper(), tekst.lower())
# TERE tere

print ("{} {}").format("qqq".upper(), "AAA".lower())
# QQQ aaa

print "{}".format(("a" + "b").upper())
# AB

print "{}".format(("a" + ("b"+"c".center(3))).upper())
# AB C

tekst1 = "asffjgfjjj"
print len(tekst1)

print tekst1 + tekst1.center(80, " ")

print  tekst1 + tekst1.center(28, " ")+ tekst1.rjust(26)


