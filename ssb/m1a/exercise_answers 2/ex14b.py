
# Calc function

def calc(num1, num2):
    	a = num1 + num2
    	b = num1 * num2
    	c = num1 - num2

    	return a,b,c 
	
d, e, f = calc(10, 5)
print (d, e, f)


# Tuple function

def calcTuple(num1, num2):
    	a = num1 + num2
    	b = num1 * num2
    	c = num1 - num2

    	return (a,b,c) 
	
tup = calc(10, 5)
print ("First value =", tup[0])
print ("Second value =", tup[1])
print ("Third value =", tup[2])


# List function

def calcList(num1, num2):
    	a = num1 + num2
    	b = num1 * num2
    	c = num1 - num2

    	return (a,b,c) 
	
lis = calc(10, 5)
print ("First value =", lis[0])
print ("Second value =", lis[1])
print ("Third value =", lis[2])



