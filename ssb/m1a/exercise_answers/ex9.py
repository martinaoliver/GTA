with open('sequence.txt') as in_file:

	seq_list = in_file.readlines()  # Read the file to a list
	seq_name = seq_list.pop(0)  # Remove the sequence name
	seq = seq_list.pop(0)  # Initialise the sequence
	seq = seq.rstrip()  # Remove the newline character
	seq = seq.lower()  # Lower case the sequence

	for line in seq_list:  #  Append the rest of the sequence to seq
		seq += line.rstrip().lower()

with open('codons.txt') as codons_file:
	codons_list = codons_file.readlines()

	codons = {}  # Initialise the dictionary
	for count in range(0, len(codons_list), 2):  # Work through the list
		key = codons_list[count].rstrip()   # Get the codon
		key = key.lower()
		value = codons_list[count+1].rstrip()  # Get the aa, on next line
		value = value.lower()	
		codons[key] = value  # Add to dictionary

out_file = open("translated_seqs.fasta", "w")
for frame in range(0, 3):
	out_file.write("> Frame " + str(frame) + "\n")

	for count in range(frame, len(seq), 3):  # Work through the list
		codon = seq[count:count+3]   # Get 3 nucleotides
		if codon in codons:
			aa = codons[codon]   # Get the associated aa
		else:
			aa = '-'
		out_file.write(aa)

	out_file.write("\n") # Sequence is finished so print newline for next sequence

out_file.close()

