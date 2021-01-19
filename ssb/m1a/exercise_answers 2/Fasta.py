class FastaRecord():
    # Class representing a FASTA record

    def __init__(self, description_line):
        # Initialise an instance of the FastaRecord clas
        self.description = description_line.rstrip()
        self.sequences = []

    def add_sequence_line(self, sequence_line):
        
        # Add a sequence line to the FastaRecord instance.
        # This function can be called more than once.
        
        self.sequences.append( sequence_line.strip() )

    def matches(self, search_term):
        # Return True if the search_term is in the description
        return self.description.find(search_term) != -1
    
    def __repr__(self):
        # Representation of the FastaRecord instance
        lines = [self.description,]
        lines.extend(self.sequences)
        return '\n'.join(lines)


class FastaParser():
    # Class for parsing FASTA files

    def __init__(self, fpath):
        # Initialise an instance of the FastaParser
        self.fpath = fpath

    def __iter__(self):
        # Yield FastaRecord instances
        fasta_record = None
        with open(self.fpath, 'r') as infile:
            for line in infile:
                if line.startswith('>'):
                    if fasta_record:
                        yield fasta_record
                    fasta_record = FastaRecord(line)
                else:
                    fasta_record.add_sequence_line(line)
        yield fasta_record





