# 01_looping_basic.py
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
			print("Please enter a number")


			
	

print("***Area Perimeter Calculator***")

keep_going = ""
while keep_going == "":

	width = num_check("Width:")
	height = num_check("height:")
	print()
	print("width",width)
	print("height",height)
	print()
	area = width*height 
	perimeter = 2*(width + height)
	print("Perimeter: {:.2f} units".format (perimeter))
	print("area: {:.2f} square units".format (area))                         

	keep_going = input("Press <enter> to keep going or any key to quit")

print("Thank you for using the area / perimeter calculator\n")



