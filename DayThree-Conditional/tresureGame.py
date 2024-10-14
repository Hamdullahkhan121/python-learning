print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print("You are standing at the entrance of a dark cave. choose L for Left and R for Right")
choise1 = input("where will you go first? left or right? ")

if choise1.lower() == "l":
    print("You found a hidden path. choose L for Left and R for Right")
    choise2 = input("where will you go next? ")
    if choise2.lower() == "r":
        print("You found a lake path. choose w for wait and s for swim")
        choise3 = input("where will you go next? ")
        if choise3.lower() == "w":
            print("You found a boat to cross the lake and crossed it")
            choise4 = input("You found 3 door. Blue (B), Yellow (Y) and Red (R). Choose the door to enter ")
            if choise4.lower() == "b":
                print("Eaten by beasts.\nGame Over.")
            elif choise4.lower() == "y":
                print("You found a treasure chest. You win!")
            else:
                print("Burned by fire.\nGame Over.")
        else:
            print("you got attacked by lake monster.\nGame Over.")

    else:
        print("you Fell into a hole.\nGame Over.")
else:
    print("you Fell into a hole.\nGame Over.")

