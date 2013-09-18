print("{:.2f}".format(3.1415926) )
# 3.14
print("{:+.2f}".format(3.1415926) )
# +3.14
print("{:+.2f}".format(-1) )
# -1.00
print("{:.0f}".format(2.71828) )
# 3
print("{:0>2d}".format(5) )
# 05
print("{:x<4d}".format(5) )
# 5xxx
print("{:x<4d}".format(10) )
# 10xx
print("{:,}".format(1000000) )
# 1,000,000
print("{:.2%}".format(0.25) )
#25.00%
print("{:.2e}".format(1000000000) )
# 1.00e+09
print("{:10d}".format(13) )
# arv 13 parem joondusega 10 kohta
print("{:<10d}".format(13) )
# arv 13 vasak joondusega
print("{:^10d}".format(13) )
# arv 13 keskjoondusega 5 kohta ees ja 5 kohta taga

s1 = "so much depends upon {}".format("a red wheel barrow")
print s1
# so much depends upon a red wheel barrow
s2 = "glazed with {} water beside the {} chickens".format("rain", "white")
print s2
# glazed with rain water beside the white chickens

s1 = " {0} is better than {1} ".format("emacs", "vim")
print s1
# emacs is better than vim
s2 = " {1} is better than {0} ".format("emacs", "vim")
print s2
# vim is better than emacs

pi = 3.14159
print(" pi = %1.2f " % pi)
# pi = 3.14

s1 = "cats"
s2 = "dogs"
s3 = " %s and %s living together" % (s1, s2)
print s3
# cats and dogs living together

madlib = " I {verb} the {object} off the {place} ".format(verb="took", object="cheese", place="table")
print madlib
# I took the cheese off the table

str = "Oh {0}, {0}! wherefore art thou {0}?".format("Romeo")
print str
# Oh Romeo, Romeo! wherefore art thou Romeo?

print("{0:d} - {0:x} - {0:o} - {0:b} ".format(21))
# 21 - 15 - 25 - 10101

print(" The {} set is often represented as {{0}} ".format("empty"))
# The empty set is often represented as {0}