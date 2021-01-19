class DNA: 
 
	def __init__(self, s): 
		# Create DNA instance initialized to by the sequence s
		self.seq = s 
		self.comp = {'a':'t', 't':'a', 'g':'c', 'c':'g'}
	
	def reverse(self): 
        	# Return the reversed sequence
		self.revseq = self.seq[::-1]
		return self.revseq 

	def complement(self): 
		# Return the complementary sequence
		compseq = ""
		for nuc in self.seq:
			compseq += self.comp[nuc] 
		return compseq 
     
	def reversecomplement(self): 
		# Return the reverse complement of the sequence
		compseq = ""
		for nuc in self.seq:
			compseq += self.comp[nuc]
		return compseq[::-1] 
     
	def gc(self): 
		# Return the percentage of sequence composed of G and C
		# Note the limitation of these next two methods are that they are case sensitive
		# They need to be modified to work with a sequence in upper case
		gc = self.seq.count('g') + self.seq.count('c') 
		return gc * 100.0 / len(self.seq) 
 
	def codons(self): 
		# Return a list of codons for the sequence
		codons = []
		for count in range(0, len(self.seq), 3):  
			codons.append(self.seq[count:count+3])
		 
		return codons 

	# Return the printable representation of the object, the sequence
	def __repr__(self):
		return self.seq
  
