seq_list = ["GGTAG", "GGTAC", "GATAG", "GGTCC"]
# The PWM requires 4 lists, one for each nucleotide count. These lists need
# to be the same length as the MSA sequences so this value is obtained
# from the first sequence in the list
n = len(seq_list[0])

# Next the 4 lists are initialised at the required length
A = [0] * n
C = [0] * n
G = [0] * n
T = [0] * n

pwm = [A, C, G, T]
# In the first for loop work through each sequence
for dna in seq_list:
    # In the inner for loop use enumerate to obtain each nucleotide in
    # the sequence and its position
    for i, nuc in enumerate(dna):
        # Check the nucleotide and increment the PWM count at the
        # appropriate position
        base = dna[i]
        if base == "A":
            pwm[0][i] += 1
        elif base == "C":
            pwm[1][i] += 1
        elif base == "G":
            pwm[2][i] += 1
        elif base == "T":
            pwm[3][i] += 1

print(pwm)
