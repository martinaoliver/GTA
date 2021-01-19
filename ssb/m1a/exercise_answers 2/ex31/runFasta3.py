from Fasta3 import FastaParser

parser = FastaParser('multi_sequences.fasta')
print (parser)

#for fasta_record in parser:
#	print(fasta_record.description)
    	#if fasta_record.matches('Q9Y233'):
        #	print(fasta_record)

print ("Now the list of fasta records")

for fasta_record in parser.getRecords():
	print(fasta_record)


# Get sequence by ID
print ("Record by ID")

print(parser.getRecordByID("DS572233"))

# Get the description lines

descriptions = parser.getDescriptions()
print(descriptions)

# Get the IDs

ids = parser.getIDs()
print(ids)

# Get sequence length by ID

seqlen = parser.getSeqLength("DS572233")
print(seqlen)
