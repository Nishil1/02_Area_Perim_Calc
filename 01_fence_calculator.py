print("****Fence Cost Caculator****")
while True :
    width = float(input("Width: "))
    lenght = float(input ("Lenght: "))
    Price = float(input("Price per meter: \n$" ))
    
    

    print("-----------------------------------------")

    perimeter = 2*(width + lenght)
    cost_fencing = perimeter * Price
    print("Perimeter: ", perimeter) 
    print("Cost of fencing: $",cost_fencing)
    
    repeat = input("\nPress <enter> to repeat or press another key to quit")
    
    if repeat != "":
        print("Thanks for using Fencing Cost Calculator")
        break;
    
    


