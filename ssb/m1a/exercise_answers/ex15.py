# CalcTuple Function

def calcTuple(num1, num2):
    	a = num1 + num2
    	b = num1 * num2
    	c = num1 - num2

    	return (a,b,c) 

tup = calcTuple(10, 20)
print ("First value =", tup[0])
print ("Second value =", tup[1])
print ("Third value =", tup[2])


# CalcList function
	
def calcList(num1, num2):
	a = num1 + num2
	b = num1 * num2
	c = num1 - num2

	return [a,b,c] 

lis = calcTuple(10, 20)
print ("First value =", lis[0])
print ("Second value =", lis[1])
print ("Third value =", lis[2])


# Dictionary function
# Prints the keys and values of a dictionary

def showDictionary(dic):
	for k in dic.keys():
		print ("Key is ", k, "and value is", dic[k])

	
codons = {'ttt':'F', 'tta':'L', 'gga':'G'}
showDictionary(codons)

# Dictionary and list function
# Prints the keys and values of a dictionary using list of keys

def showDictionary(lis, dic):
	for k in lis:
		print ("Key is", k, "and value is", dic[k])


codon_list = ('ttt', 'tta', 'gga')	
codons = {'ttt':'F', 'tta':'L', 'gga':'G'}
showDictionary(codon_list, codons)
