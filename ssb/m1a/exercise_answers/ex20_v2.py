# Dictionary for the reverse complementing of the nucleic acids

trans = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

# As a default value is used in the function definition this time the positions
# have to be in a list. The default value also needs to be last

def translate(seq, pos, strand=1):

	code_seq = ""
	for p in range(0, len(pos), 2):
		start = pos[p]
		end = pos[p+1]

		ex_seq = seq[start-1:end]

		if strand == -1:
			# Reverse the sequence
			revseq = ""
		
			ex_seq = ex_seq[::-1]
			for base in ex_seq:
				if base in trans:
					revseq += trans[base]
				else:
					revseq += "N"
			ex_seq = revseq
		
		code_seq += ex_seq

	aaseq = ""
	for count in range(0, len(code_seq), 3):  # Work through the list
		codon = code_seq[count:count+3]   # Get 3 nucleotides
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

with open('blumeria_seq.fasta') as in_file:

	seq_list = in_file.readlines()  # Read the file to a list
	seq_name = seq_list.pop(0)  # Remove the sequence name
	seq = seq_list.pop(0)  # Initialise the sequence
	seq = seq.rstrip()  # Remove the newline character
	
	for line in seq_list:  #  Append the rest of the sequence to seq
		seq += line.rstrip()
	seq = seq.upper()  # Upper case the sequence

	# As a default value is used in the function definition this time the positions
	# have to be in a list
	# In the first 2 genes the strand is not included as the default is used

	exons = (4550, 4636, 4698, 4796, 4852, 5565, 5623, 5715)

	aaseq = translate(seq, exons)

	print ("Gene 1 Translation:", aaseq)

	exons = (7647, 7759, 7854, 8216, 8267, 8660)
 
	aaseq = translate(seq, exons)
 
	print ("Gene 2 Translation:", aaseq)

	exons = (17433, 17709, 17243, 17370)

	# For this gene the strand is included to override the default

	aaseq = translate(seq, exons, -1)

	print ("Gene 3 Translation:", aaseq)





