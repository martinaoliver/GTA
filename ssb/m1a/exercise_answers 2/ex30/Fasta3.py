class FastaRecord(object):
    # Class representing a FASTA record

	def __init__(self, description_line):
		# Initialise an instance of the FastaRecord class
		self.sequence = description_line
		# Remove > and whitespace on ends
		self.description = description_line[1:]
		self.description = self.description.strip()
		self.seqid = (self.description.split())[0]
		self.seq_length = 0

	def add_sequence_line(self, sequence_line):
        
		# Add a sequence line to the FastaRecord instance.
		# This function can be called more than once.
        
		self.seq_length += len(sequence_line.strip())
		self.sequence += sequence_line

	def matchesID(self, searchid):
		# Return description line by ID
		if self.seqid == searchid:
			return True

	def getDescription(self):
		# Return description line
		return self.description 

	def getSeqLength(self):
		# Return seq_length
		return self.seq_length
    
	def __repr__(self):
		# Representation of the FastaRecord instance
		return self.sequence


class FastaParser(object):
   	# Class for parsing FASTA files
	def __init__(self, fpath):
	# Initialise an instance of the FastaParser
		self.fpath = fpath
		self.record_list = []

		fasta_record = None
		with open(self.fpath, 'r') as fh:
			for line in fh:
				if line.startswith('>'):
					if fasta_record:
						self.record_list.append(fasta_record)
					fasta_record = FastaRecord(line)
				else:
					fasta_record.add_sequence_line(line)
			self.record_list.append(fasta_record)

	
	def __repr__(self):
		seqs = ""
		for record in self.record_list:
			seqs += str(record) + "\n"
		return seqs

	def getRecords(self):
		return self.record_list

	def getRecordByID(self, seqid):
		for record in self.record_list:
			if record.matchesID(seqid):
				return record

	def getSeqLength(self, seqid):
		for record in self.record_list:
			if record.matchesID(seqid):
				return record.getSeqLength()

	def getIDs(self):
		ids = []
		for record in self.record_list:
			ids.append(record.seqid)
		return ids

	def getDescriptions(self):
		descriptions = []
		for record in self.record_list:
			descriptions.append(record.description)
		return descriptions


