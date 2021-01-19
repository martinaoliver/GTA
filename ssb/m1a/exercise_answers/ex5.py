seq = "ACTCGGCTTAAATGTTATTCGTACCTACGCCTT"

c_count = 0
t_count = 0

for c in seq:
	if c == "C": 
		c_count +=1
	elif c == "T":
		t_count +=1

print ("Total cytosine = ", c_count)
print ("Total thymine = ", t_count)

