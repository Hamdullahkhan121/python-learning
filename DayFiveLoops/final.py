import random
import string
print("welcome to the PyPassword")

passLength = int(input("How many letter would you like in your password\n"))
specialChar = int(input("How many special Characters do you want in your password\n"))
digits = int(input("How many special Characters do you want in your password\n"))
list= []
password=""

for i in range(passLength):
    x = random.choice(string.ascii_letters)
    list.append(x)

for j in range(specialChar):
    z = random.choice(string.punctuation)
    random1 = random.randint(0,passLength-1)
    list[random1]= z 

for k in range(digits):
    z = random.choice(string.digits)
    random2 = random.randint(0,passLength-1)
    list[random2]= z

for item in list:
    password +=item
print(password)


#This below block will create a random passport of how many letters in a passowrd inputed
# for i in range(passLength):
#     x = random.choice(string.ascii_lowercase)
#     # list.append(x)
#     y += x
#     print(y)