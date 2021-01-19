# Default parameters

def calcValue(num1, num2=20, num3=8):

	total = num1 + num2 - num3

	return total


ans = calcValue(6)

print (ans)


# Call it with 2 numbers so only num3 uses the default

ans = calcValue(6, 10)

print (ans)


# Can still call it with 3 different numbers

ans = calcValue(6, 10, 5)

print (ans)


# Can also change just one of the defaults

ans = calcValue(6, num3=4)

print (ans)


# Variable number of parameters in a list

def calcValue(num1, num2, *morenums):

	total = num1 + num2
	for n in morenums:
		total += n

	return total


ans = calcValue(2, 4,  5, 12, 15)
print (ans)
		

# Variable number of parameters in a dictionary

def testFunc (val1, val2, **morevals):

	print ("Val1 is", val1)
	print ("Val2 is", val2)

	print ("The dictionary")

	for k in morevals.keys():
		print ("Key is", k, "Value is", morevals[k])



testFunc("First", "Second", Third=3, Fourth=4, Fifth=5)

