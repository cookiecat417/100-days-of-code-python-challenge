print("Welcome to Builder Brothers Pizza!")

answer = input("Hello there! Would you like to order a pizza? Y or N: ")
    
if answer == "Yes":
    size = input("Which pie would you like to order? S, M, or L: ")
    if size == "Small":
        bill = 15
        print(bill)

    elif size == "Medium":
        bill = 20
        print(bill)

    elif size == "Large":
        bill = 25
        print(bill)
    
    else:
        print("ORDER. NOW.")

    pepperoni = input("Would you like any pepperonis on your pizza? Y or N: ")
    if pepperoni == "Yes":
        if size == "Small":
            bill += 2
    

    if pepperoni == "Yes":
        if size == "Medium":
            bill += 3
    
    
    if pepperoni == "Yes":
        if size == "Large":
            bill += 3
    
    print(bill)

    cheese = input("Would you like to add any cheese on your pizza? Y or N: ")
    if cheese == "Yes":
            bill += 1
    print(bill)

 
    print(f"Your total is ${bill}.")
else: 
    print("Yup, you're banned.")






# bill = 0
# if (size) == "Small":
#     bill += 15
# elif size == "Medium":
#     bill += 20
# elif size == "Large":
#     bill += 25









    






    

