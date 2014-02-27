class Postipakk:
	kellelt = ""
	kellele = ""
	status = "koostamisel"
	
	def __init__(self):
		self.kellelt = raw_input("Kellelt: ")
		self.kellele = raw_input("Kellele: ")
		
	def trantsport(self):
		self.status = "trantsport"
	
	def kohal(self):
		self.status = "kohal"
		
	def status_print(self):
		print "Status on " + self.status
		
obj1 = Postipakk()
obj1.status_print()

obj2 = Postipakk()
obj2.kohal()
obj2.status_print()
