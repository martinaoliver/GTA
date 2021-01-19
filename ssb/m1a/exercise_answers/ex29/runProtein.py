from Protein import Protein
from Atom import Atom 

# Creating a protein molecule:

prot = Protein('Trp-cage')
seq = ""

countaa = 0

with open ("1l2y.coords") as protfile:
	for line in protfile:
		line = line.rstrip()
		split_line = line.split()
		aa = split_line[3]
		aanum = split_line[5]
		at = Atom(split_line[11], float(split_line[6]), float(split_line[7]), float(split_line[8]))  #  Create first atom
		prot.addatom(at, aa, aanum)   #  Add it to the molecule object

		if(int(aanum) > countaa):
			seq += aa + " "
			countaa+=1

prot.addsequence(seq)

print (prot)  # Print the molecule object details 

print ("\nProtein Sequece:")
prot.getsequence()

print ("\nAtom Details:")
prot.getatomdetails(2)

print("\nAA Details")
prot.getaadetails(2)

