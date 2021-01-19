for i in range(1, 21):
	if i % 4 == 0 or i % 5 == 0:
		if i % 4 == 0:
			print (i, "divisible by 4")
		if i % 5 == 0:
			print (i, "divisible by 5")
	else:
		print (i, "not divisible by 4 or 5")

