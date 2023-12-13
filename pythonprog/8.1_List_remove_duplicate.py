# Remove duplicate values from the list

numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

#o/p
#[2, 4, 6, 3, 1]