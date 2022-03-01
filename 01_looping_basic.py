valid = False
while not valid:
	response = float(input("Enter a number:  "))
	if response > 0:
		valid = True 
	else:
		print("Please enter value more than 0\n")
	