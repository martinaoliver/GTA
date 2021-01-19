from pylab import *

in_file = open("5HT1A_HUMAN.fasta")

seq = ""
for line in in_file:
	strip_line = line.rstrip()
	if(strip_line.startswith('>')):
		seqid = strip_line
		seqid = seqid.replace('>','')
	else:
		seq += strip_line
in_file.close()

in_file = open("hydrophobicity_values.txt")
vals_lines = in_file.readlines()

vals = {}  # Initialise the dictionary
for count in range(0, len(vals_lines), 2): 
	vals[vals_lines[count].rstrip()] = vals_lines[count+1].rstrip()	

in_file.close()

y_data = []
for count in range(0, len(seq)):  
	aa = seq[count]   
	print (vals[aa]+",", end="")
	y_data.append(vals[aa])

x_data = range(1, len(y_data)+1)

plot(x_data, y_data)

xlabel("Residue number")
ylabel("Hydrophobicity")
title("Hydrophobicity Plot for "+seqid)
show()

