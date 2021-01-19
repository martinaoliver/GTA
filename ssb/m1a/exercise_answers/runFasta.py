from Fasta import FastaParser

for fasta_record in FastaParser('multi_sequences.fasta'):
	print(fasta_record.description)
    	#if fasta_record.matches('Q9Y233'):
        #	print(fasta_record)

print ("Now the iterator")

for fasta_record in FastaParser('multi_sequences.fasta'):
	print(fasta_record)


