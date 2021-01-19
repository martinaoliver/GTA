with open('CAUH01000012.gff') as in_file:
	for line in in_file: 
		if line.startswith('CAUH01000012'):
			values = line.split()
			if values[2] == 'CDS':	
				print ("Start =", values[3], "and end =", values[4])

