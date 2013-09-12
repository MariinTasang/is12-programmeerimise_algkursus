print "abc" .capitalize ()
# Abc
print "abc" .center (7, ".")
# ..abc..
print "mariin" .count ("i", 0, 100)
# 2

# siin peaks olema .decode
# siin peaks olema .encode
# siin peaks olema .endswith
# siin peaks olema .expandtabs

print "abc" .find ("c", 0, 100)
# 2
print "The sum on 1+2 is {}" .format (1+2)
# The sum on 1+2 is 3

print "abc" .index ("b", 0, 100)
# 1

# siin peaks olema .isalnum

print "12345" .isalpha()
# False
print "abcde" .isalpha()
# True
print "1111" .isdigit()
# True
print "11aa" .isdigit()
# False
print "abc" .islower ()
# True
print "ABC" .islower()
# False
print " " .isspace()
# True
print "a" .isspace()
# False

# siin peaks olema istitle

print "abab" .isupper()
# False
print "ABAB" .isupper ()
# True"

# siin peaks olema join (iterable)
# siin peaks olema ljust (width[, fillchar])

print "ABAB" .lower()
# abab
print "tere" .lstrip ("t")
# ere
print "muusika" .partition ("i")
# ("muus", "i", "ka")
print "kala" .replace ("a", "o", 1)
# kola
print "muusika" .rfind ("i", 0, 100)
# 4
print "muusika" .rindex ("s", 0, 100)
# 3

# siin peaks olema .rjust (width, fillchar)
# siin peaks olema .rpartition (sep)


print "Mariin" .rsplit ("r")
#["Ma" , "iin"]

# siin peaks olema .rstrip (chars)

print "A/B/C/D" .split ("/")
# ["A","B","C","D"]

# siin peaks olema .splitlines (keepends)
# siin peaks olema .startswith (prefix, start, end)

print "www.example.com" .strip ("w")
# .example.com
print "maRIin" .swapcase()
# MAriIN
print "tere tulemast kooli" .title()
# Tere Tulemast Kooli
print "tere tulemast kooli" .translate (None, "euo")
# tr tlmast kli
print "abc" .upper ()
# ABC

# siin peaks olema .zfill ()
# siin peaks olema .isnumeric ()
# siin peaks olema .usdecimal()




