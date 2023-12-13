#Write a program to findout the max number from a list

numbers = [3,6,2,8,4,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#o/p
#10