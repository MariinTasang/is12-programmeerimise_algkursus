print '{0}, {1}, {2}'.format('a', 'b', 'c')
# a, b, c
print '{2}, {1}, {0}'.format('a', 'b', 'c')
# c, b, a
print '{2}, {1}, {0}'.format(*'abc')
# c, b, a
print '{0}{1}{0}'.format('abra', 'cad')
# abracadabra

print 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
# Coordinates: 37.24N, -115.81W
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print 'Coordinates: {latitude}, {longitude}'.format(**coord)
# Coordinates: 37.24N, -115.81W

c = 3-5j
('The complex number {0} is formed from the real part {0.real} '
'and the imaginary part {0.imag}.').format(c)
class Point(object):
		def __init__(self, x, y):
			self.x, self.y = x, y
		def __str__(self):
			return 'Point({self.x}, {self.y})'.format(self=self)
print str(Point(4, 2))
# Point(4, 2

coord = (3, 5)
print 'X: {0[0]};  Y: {0[1]}'.format(coord)
# X: 3;  Y: 5

print  "repr() shows quotes: {0!r}; str() doesn't: {1!s}".format('test1', 'test2')
# repr() shows quotes: 'test1'; str() doesn't: test2

print '{0:<30}'.format('left aligned')
# vasakule joondus
print '{0:>30}'.format('right aligned')
# paremale joondus
print '{0:^30}'.format('centered')
# keskele joondus
print '{0:*^30}'.format('centered')
# keskele joondus
# tarnid

print '{0:+f}; {0:+f}'.format(3.14, -3.14)
# +3.140000; +3.140000
print '{0: f}; {0: f}'.format(3.14, -3.14)
#  3.140000;  3.140000
# + margi asemel on tyhik
print '{0:-f}; {0:-f}'.format(3.14, -3.14)
# 3.140000; 3.140000

print "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
# int: 42;  hex: 2a;  oct: 52;  bin: 101010
print "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
# int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010

points = 19.5
total = 22
print 'Correct answers: {0:.2%}.'.format(points/total)
# Correct answers: 88.64%

import datetime
d = datetime.datetime(2013, 9, 15, 13, 33, 58)
print '{0:%Y-%m-%d %H:%M:%S}'.format(d)
# 2013-09-15 13:33:58

octets = [192, 168, 0, 1]
print '{0:02X}{1:02X}{2:02X}{3:02X}'.format(*octets)
# C0A80001

width = 5
for num in range(5,12):
 for base in 'dXob':
	 print '{0:{width}{base}}'.format(num, base=base, width=width)
 print
# 5
# 5
# 5
# 101

# 6
# 6
# 6
# 110

# 7
# 7
# 7
# 111

# 8
# 8
# 10
# 1000

# 9
# 9
# 11
# 1001

# 10
# A
# 12
# 1010

# 11
# B
# 13
# 1011




