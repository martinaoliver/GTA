from sys import *

def add(num1, num2): 
	num3 = num1 + num2
	return num3 

n1 = int(argv[1])
n2 = int(argv[2])

total = add(n1, n2)
print (n1, "+", n2, "=", total)

# Note that input needs to be converted to an integer.
# Without this the 2 numbers would be treated as strings
# and just appended together 
