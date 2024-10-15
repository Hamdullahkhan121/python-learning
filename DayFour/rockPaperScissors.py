import random

rockArt = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
                
'''

paperArt ='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
                
'''
scissorsArt = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''





userChoise = int(input("What do you choose? 0 for Rock, 1 for paper, and 2 for scissors "))

compChoise = random.randint(0,2)

if userChoise == 0:
    print(f"Player chose Rock {rockArt}")
elif userChoise == 1:
    print(f"Player chose Paper {paperArt}")
elif userChoise == 2:
    print(f"Player chose scissors {scissorsArt}")
else:
    print("Invalid input. Please choose 0, 1, or 2.")

if compChoise == 0:
    print(f"Computer chose Rock {rockArt}")
elif compChoise == 1:
    print(f"computer chose paper {paperArt}")
elif compChoise == 2:
    print(f"Computer chose scissors {scissorsArt}")

if userChoise == compChoise:
    print("It's a tie!")
elif userChoise > compChoise and compChoise==0:
    if userChoise ==1:
        print("Player Won")
    else:
        print("Computer Won")
elif userChoise ==0 and compChoise !=0:
    if compChoise ==2:
        print("Player Won")
    else:
        print("Computer Won")

#The code is working but its a bit complicated and not optimized i will optimize it in a seprate file