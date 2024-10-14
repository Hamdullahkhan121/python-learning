print("Welcome to the python pizza Deliveries!!")
size = input("What size piza do you want? S, M or L? ")
pepperoni = input("Do you want Pepperoni on your pizza? Y or N: ")
extraCheese =input("Do you want Extra Cheese on your Pizza? Y or N: ")
bill =0

if size == "s":
    bill = 10
    print("a large pizza would be ${bill}")
elif size == "m":
    bill = 15
    print("a large pizza would be ${bill}")
else:
    bill = 20
    print("a large pizza would be ${bill}")

if pepperoni == "y":
    bill += 5
    print(f"Your new bill for pizza with pepperoni is ${bill}") 
else:
    print(f"Your bill for pizza is ${bill}")

if extraCheese == "y":
    bill += 3
    print(f"with extra cheese Your final bill for pizza is ${bill}") 
else:
    print(f"Your final bill for pizza is ${bill}") 