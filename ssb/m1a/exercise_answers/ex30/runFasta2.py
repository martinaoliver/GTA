from Fasta2 import FastaParser

parser = FastaParser('multi_sequences.fasta')
print (parser)

print ("Now the list of fasta records")

for fasta_record in parser.getRecords():
	print(fasta_record)



