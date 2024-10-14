print("Welcome to the Tip Calculator")
bill = int(input("Your Total bill is:\n"))
tip = int(input("How much tip would you like to give? 15, 20 0r 25?\n"))
people = int(input("how many people to split the bill?\n"))

tipFraction = tip / 100
tipAmount = bill * tipFraction
totalbill = bill + tipAmount
indivisualBill = round((totalbill / people), 2)

print(f"The total bill inculding tip is {totalbill}, and indivisual bill per person is {indivisualBill}")
