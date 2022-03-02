# checks input is a number more than 0

def num_check(question):
	valid = False
	while not valid:
		error = "Please enter value more than 0\n"
		try:
			# ask user to enter a number

			response = float(input(question))
			
			# check if the number is more than 0
			
			if response > 0:
				return response  

			#outputs error if the input is invalid

			else:
				print(error)
		except ValueError: 
			print(error)
	






width = num_check("Width:")
height = num_check("height:")
print()
print("width",width)
print("height",height)
print()
area = width*height 
perimeter = 2*(width + height)
print("Perimeter:", perimeter, "units")
print("area:", area, "square units")


