def add(num1, num2): 
	num3 = num1 + num2
	return num3 

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

total = add(n1, n2)
print (n1, "+", n2, "=", total)


# This code is obviously more verbose than it needs to be,
# for instance there is no need for the "total" variable
# and the print statement could be:
#
# print (n1, "+", n2, "=", add(n1, n2))
