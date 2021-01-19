# Dictionary for the reverse complementing of the nucleic acids

trans = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}


def translate(seq):
	aaseq = ""
	for count in range(0, len(seq), 3):  # Work through the list
		codon = seq[count:count+3]   # Get 3 nucleotides
		if codon in codons:
			aa = codons[codon]   # Get the associated aa
		else:
			aa = '-'
		
		aaseq += aa

	return aaseq


with open('codons.txt') as codons_file:
	codons_list = codons_file.readlines()

	codons = {}  # Initialise the dictionary
	for count in range(0, len(codons_list), 2):  # Work through the list
		key = codons_list[count].rstrip()   # Get the codon
		key = key.upper()
		value = codons_list[count+1].rstrip()  # Get the aa, on next line
		value = value.upper()	
		codons[key] = value  # Add to dictionary

with open('sequence.txt') as in_file:

	seq_list = in_file.readlines()  # Read the file to a list
	seq_name = seq_list.pop(0)  # Remove the sequence name
	seq = seq_list.pop(0)  # Initialise the sequence
	seq = seq.rstrip()  # Remove the newline character
	
	for line in seq_list:  #  Append the rest of the sequence to seq
		seq += line.rstrip()
	seq = seq.upper()  # Upper case the sequence

	for i in range(1, 3):
		if i == 1:
			print ("Forward Strand")
		else:
			print ("\nReverse Strand")
		for j in range(1, 4):
			aaseq = translate(seq[j-1:])

			print ("Frame", j, ":\n", aaseq)
		
		# Reverse the sequence
		revseq = ""
		seq = seq.upper()
		if i == 1:
			seq = seq[::-1]
			for base in seq:
				if base in trans:
					revseq += trans[base]
				else:
					revseq += "N"
			seq = revseq
	



