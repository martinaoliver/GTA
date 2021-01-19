class Protein:
	def __init__(self,name='Test Molecule'):
		self.name = name
		self.atomlist = []
		self.aa_dict = {}
		self.aanum_dict = {}
	def addatom(self,atom, aa, aanum):
		self.atomlist.append(atom)
		self.aa_dict[len(self.atomlist)] = aa
		self.aanum_dict[len(self.atomlist)] = aanum
	def addsequence(self,seq):
		self.sequence = seq
	def getsequence(self):
		print (self.sequence)
	def getatomdetails(self, atom_pos):
		at = self.atomlist[atom_pos - 1]
		print (self.aa_dict[atom_pos], at)
	def getaadetails(self, aapos):
		
		for atpos in range(0, len(self.atomlist)):
			#print (self.aanum_dict[atpos], aapos)
			if atpos in self.aanum_dict and int(self.aanum_dict[atpos]) == int((aapos)):
				self.getatomdetails(atpos)
	def __repr__(self):
		s = 'Molecule name is %s ' % self.name
		s = s + ' and it has %d atoms\n' % len(self.atomlist)
		for atom in self.atomlist:
			s = s + str(atom) + '\n'
		return s

