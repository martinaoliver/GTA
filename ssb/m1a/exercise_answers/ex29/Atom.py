class Atom:
	def __init__(self,symbol,x,y,z):
		self.symbol = symbol
		self.position = (x,y,z)
	def getSymbol(self):
		return self.symbol
	def __repr__(self):
		return '%s %10.4f %10.4f %10.4f' % (self.getSymbol(), self.position[0], self.position[1],self.position[2])


