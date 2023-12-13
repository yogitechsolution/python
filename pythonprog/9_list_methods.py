numbers = [1,2,3,4,5,4]
print(numbers)

numbers2 = numbers.copy()
numbers.append(10)
print(numbers) #appended value
print(numbers2) #original values since we used copy fun

numbers.sort() #print number in sorting order
print(numbers) 
numbers.reverse() #reverse the sorting order
print(numbers)

print(numbers.index(4)) #print number at that index
#print(numbers.index(10)) #index which not exists - ValueError: 10 is not in list

print(numbers.count(4)) # Count occurance of a number

numbers.pop() #removes last number from the list
print(numbers)

numbers.append(6)
print(numbers)

numbers.insert(0, 6)
print(numbers)

numbers.remove(3)
print(numbers)

print(1 in numbers)
print(10 in numbers)

print(len(numbers))

numbers.clear() #Clear the list
print(numbers)

#o/p
#[1, 2, 3, 4, 5, 4]
#[1, 2, 3, 4, 5, 4, 10]
#[1, 2, 3, 4, 5, 4]
#[1, 2, 3, 4, 4, 5, 10]
#[10, 5, 4, 4, 3, 2, 1]
#2
#2
#[1, 2, 3, 4, 5]
#[1, 2, 3, 4, 5, 6]
#[6, 1, 2, 3, 4, 5, 6]
#[6, 1, 2, 4, 5, 6]
#True
#False
#6
#[]