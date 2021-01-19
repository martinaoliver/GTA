# Function

def calcValue(num1, num2, num3):

	total = num1 + num2 - num3
	
	return total


# Call function as normal

ans = calcValue(5, 10, 6)

print (ans)


# Call function with keywords

ans = calcValue(num1=5, num2=10, num3=6)

print (ans)


# Call function with keywords in different order

ans = calcValue(num3=6, num2=10, num1=5)

print (ans)
