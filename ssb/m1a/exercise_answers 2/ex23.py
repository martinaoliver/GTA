import matplotlib.pyplot as plt
import re

# The script creates a function to produce the plot
def plotGC(seq):
	# Comple REs to identify the nucleotides
	c = re.compile("C")
	g = re.compile("G")
	a = re.compile("A")
	t = re.compile("T")

	# Initialise lists for the plot data
	x_data = []
	y_data = []
	y_data2 = []

	# Work through the sequence, slicing 100 nucleotides at a time
	for pos in range(0, len(seq), 100):
		subseq = seq[pos:pos+100]
	
		# Use subn to count the matches for each nucleotide
		gc = g.subn("G", subseq)[1]
		gc += c.subn("C", subseq)[1]
		at = a.subn("A", subseq)[1]
		at += t.subn("T", subseq)[1]

		# Append the data to the plot lists
		x_data.append(pos)
		y_data.append(gc)
		y_data2.append(at)

	# Create and display the plot, with a legend
	plt.plot(x_data, y_data, 'r', label='GC')
	plt.plot(x_data, y_data2, 'b', label='AT')
	plt.xlabel("Position (nuc)")
	plt.ylabel("Percentage GC")
	plt.legend(loc='upper right')
	plt.title("GC/AT Content of Entamoea Sequence")

	plt.show()

# Open the sequence file and strip off the header line
seqfile = open('Entamoeba_Sequence.fasta')
seq_lines = seqfile.readlines()
seq_lines.pop(0)

# Create the sequence string, ensuring it is upper case
# to match the RE nucleotide definitions
seq = ''
for line in seq_lines:
	seq += line.rstrip().upper()

# Call the plotting function
plotGC(seq)

