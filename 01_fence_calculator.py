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

print("****Fence Cost Caculator****")
while True :

    width = num_check("Width:")
    lenght =num_check("Lenght: ")
    Price = num_check("Price per meter: \n$" )

    print("-----------------------------------------")

    perimeter = 2*(width + lenght)
    cost_fencing = perimeter * Price
    print("Perimeter: ", perimeter) 
    print("Cost of fencing: $",cost_fencing)
    
    repeat = input("\nPress <enter> to repeat or press another key to quit")
    if repeat != "":
        print("Thanks for using Fencing Cost Calculator")
        break;
    
    


