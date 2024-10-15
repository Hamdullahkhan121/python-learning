marks_array = [67, 106, 94, 78, 116, 90, 80, 134, 135, 95, 138, 74, 113, 95]

#the Block is to write sum function
sum = 0
for mark in marks_array:
    sum += mark
print(sum)

#the Block is to find max mark function
num =0
for mark in marks_array:
    if mark >=num:
        num = mark
print(num)  

#This block is to add number from 1 to 100

total =0
for i in range(1,101):
    total+=i
print(total)