print("welcome to the RollerCoaster!")
height = int(input("What is your height in cm? "))
age = int(input("You have to pay $18 if you are 18 or older you will pay $12 if you are over 12 and $8 if you are 12 or younger\nSo what is your age? "))
bill = 0


if height >= 120:
    print("Please enjoy the ride!!")
    if age >= 18:
        bill =18
        print(f"You have to pay ${bill} for the adult ticket")
    elif age > 12:
        bill =12
        print(f"You have to pay ${bill} for the youth ticket")
    else:
        bill =8
        print(f"You have to pay ${bill} for the child ticket")

    photo = input("would you like to take a photo? that would be $3 to your bill\nenter y for Yes and n for No: ")
    if photo == 'y':
        bill +=3
        print(f"your new bill is ${bill}")
    else:
        print(f"your new bill is ${bill}")
    
else:
    print("Sorry! you have to be atleast 120cm to take this Rollercosater ride")