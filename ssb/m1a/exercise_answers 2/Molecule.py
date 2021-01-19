class Molecule:
	def __init__(self,name='Test Molecule'):
		self.name = name
		self.atomlist = []

	def addatom(self,atom):
		self.atomlist.append(atom)

	def __repr__(self):
		s = 'Molecule name is %s ' % self.name
		s = s + ' and it has %d atoms\n' % len(self.atomlist)
		for atom in self.atomlist:
			#str = str + Atom.getSymbol() + '\n'
			s = s + str(atom) + '\n'
		return s

